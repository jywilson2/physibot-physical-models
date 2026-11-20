"""Differential-drive odometry node for PhysiBot sim labs."""

from __future__ import annotations

import math
import random

import rclpy
from geometry_msgs.msg import Quaternion, TransformStamped, Twist
from nav_msgs.msg import Odometry
from rclpy.node import Node
from tf2_ros import TransformBroadcaster

from physibot_sim.kinematics import Pose2D, integrate_unicycle


def yaw_to_quat(yaw: float) -> Quaternion:
    q = Quaternion()
    q.z = math.sin(yaw * 0.5)
    q.w = math.cos(yaw * 0.5)
    return q


class DiffDriveOdomNode(Node):
    def __init__(self) -> None:
        super().__init__("diff_drive_odom")
        self.declare_parameter("wheel_separation", 0.175)
        self.declare_parameter("wheel_radius", 0.04)
        self.declare_parameter("odom_frame", "odom")
        self.declare_parameter("base_frame", "base_footprint")
        self.declare_parameter("odom_noise_std", 0.0)
        self.declare_parameter("max_v", 1.0)
        self.declare_parameter("max_omega", 2.0)
        self.declare_parameter("rate_hz", 50.0)

        self._pose = Pose2D()
        self._v = 0.0
        self._omega = 0.0
        self._last_time = self.get_clock().now()

        self._tf_broadcaster = TransformBroadcaster(self)
        self._odom_pub = self.create_publisher(Odometry, "odom", 10)
        self.create_subscription(Twist, "cmd_vel", self._on_cmd_vel, 10)

        period = 1.0 / float(self.get_parameter("rate_hz").value)
        self.create_timer(period, self._on_timer)
        self.get_logger().info(
            "diff_drive_odom ready "
            f"(sep={self.get_parameter('wheel_separation').value}, "
            f"noise={self.get_parameter('odom_noise_std').value})"
        )

    def _on_cmd_vel(self, msg: Twist) -> None:
        max_v = float(self.get_parameter("max_v").value)
        max_w = float(self.get_parameter("max_omega").value)
        self._v = max(-max_v, min(max_v, msg.linear.x))
        self._omega = max(-max_w, min(max_w, msg.angular.z))

    def _on_timer(self) -> None:
        now = self.get_clock().now()
        dt = (now - self._last_time).nanoseconds * 1e-9
        self._last_time = now
        if dt <= 0.0 or dt > 1.0:
            return

        noise = float(self.get_parameter("odom_noise_std").value)
        v = self._v + (random.gauss(0.0, noise) if noise > 0.0 else 0.0)
        omega = self._omega + (random.gauss(0.0, noise) if noise > 0.0 else 0.0)
        self._pose = integrate_unicycle(self._pose, v, omega, dt)

        odom_frame = str(self.get_parameter("odom_frame").value)
        base_frame = str(self.get_parameter("base_frame").value)

        odom = Odometry()
        odom.header.stamp = now.to_msg()
        odom.header.frame_id = odom_frame
        odom.child_frame_id = base_frame
        odom.pose.pose.position.x = self._pose.x
        odom.pose.pose.position.y = self._pose.y
        odom.pose.pose.orientation = yaw_to_quat(self._pose.yaw)
        odom.twist.twist.linear.x = v
        odom.twist.twist.angular.z = omega
        self._odom_pub.publish(odom)

        t = TransformStamped()
        t.header.stamp = now.to_msg()
        t.header.frame_id = odom_frame
        t.child_frame_id = base_frame
        t.transform.translation.x = self._pose.x
        t.transform.translation.y = self._pose.y
        t.transform.rotation = yaw_to_quat(self._pose.yaw)
        self._tf_broadcaster.sendTransform(t)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = DiffDriveOdomNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
