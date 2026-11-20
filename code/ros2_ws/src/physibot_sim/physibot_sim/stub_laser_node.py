"""Publish a minimal LaserScan for mapping/localization smoke labs.

Not a physics sensor — enough for TF/frame teaching and Nav2 bringup smoke.
Replace with Gazebo/Isaac/real Limo LiDAR for realistic SLAM.
"""

from __future__ import annotations

import math

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class StubLaserNode(Node):
    def __init__(self) -> None:
        super().__init__("stub_laser")
        self.declare_parameter("frame_id", "laser_link")
        self.declare_parameter("rate_hz", 10.0)
        self.declare_parameter("range_min", 0.12)
        self.declare_parameter("range_max", 8.0)
        self.declare_parameter("wall_distance", 2.0)

        self._pub = self.create_publisher(LaserScan, "scan", 10)
        period = 1.0 / float(self.get_parameter("rate_hz").value)
        self.create_timer(period, self._on_timer)
        self.get_logger().info("stub_laser publishing on /scan (teaching stub)")

    def _on_timer(self) -> None:
        wall = float(self.get_parameter("wall_distance").value)
        n = 360
        scan = LaserScan()
        scan.header.stamp = self.get_clock().now().to_msg()
        scan.header.frame_id = str(self.get_parameter("frame_id").value)
        scan.angle_min = -math.pi
        scan.angle_max = math.pi
        scan.angle_increment = (2.0 * math.pi) / n
        scan.time_increment = 0.0
        scan.scan_time = 1.0 / float(self.get_parameter("rate_hz").value)
        scan.range_min = float(self.get_parameter("range_min").value)
        scan.range_max = float(self.get_parameter("range_max").value)
        # Axis-aligned square room centered on the robot at origin pose.
        ranges = []
        for i in range(n):
            angle = scan.angle_min + i * scan.angle_increment
            c = abs(math.cos(angle))
            s = abs(math.sin(angle))
            # Distance to square walls at ±wall
            denom = max(c, s, 1e-6)
            r = wall / denom
            r = min(max(r, scan.range_min), scan.range_max)
            ranges.append(float(r))
        scan.ranges = ranges
        self._pub.publish(scan)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = StubLaserNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
