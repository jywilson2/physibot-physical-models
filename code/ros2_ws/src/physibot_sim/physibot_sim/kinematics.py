"""Planar differential-drive kinematics for PhysiBot labs.

Pure Python (no ROS import) so unit tests run on the host without Docker.
Limo Pro defaults: tread 0.175 m (published); wheel radius 0.04 m (teaching estimate).
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Pose2D:
    x: float = 0.0
    y: float = 0.0
    yaw: float = 0.0


def wrap_to_pi(angle: float) -> float:
    """Wrap angle to (-pi, pi]."""
    a = (angle + math.pi) % (2.0 * math.pi) - math.pi
    return a if a != -math.pi or angle <= 0 else math.pi


def integrate_unicycle(pose: Pose2D, v: float, omega: float, dt: float) -> Pose2D:
    """Integrate unicycle kinematics for one timestep.

    x' = v cos(yaw), y' = v sin(yaw), yaw' = omega
    """
    if dt < 0.0:
        raise ValueError("dt must be non-negative")
    if abs(omega) < 1e-9:
        return Pose2D(
            x=pose.x + v * math.cos(pose.yaw) * dt,
            y=pose.y + v * math.sin(pose.yaw) * dt,
            yaw=wrap_to_pi(pose.yaw),
        )
    # Exact integration on a circular arc
    yaw_new = wrap_to_pi(pose.yaw + omega * dt)
    return Pose2D(
        x=pose.x + v / omega * (math.sin(yaw_new) - math.sin(pose.yaw)),
        y=pose.y - v / omega * (math.cos(yaw_new) - math.cos(pose.yaw)),
        yaw=yaw_new,
    )


def wheel_speeds_from_twist(
    v: float, omega: float, wheel_separation: float, wheel_radius: float
) -> tuple[float, float]:
    """Inverse differential kinematics → left/right wheel angular rates (rad/s)."""
    if wheel_radius <= 0.0 or wheel_separation <= 0.0:
        raise ValueError("wheel_radius and wheel_separation must be positive")
    v_l = v - omega * wheel_separation / 2.0
    v_r = v + omega * wheel_separation / 2.0
    return v_l / wheel_radius, v_r / wheel_radius


def twist_from_wheel_speeds(
    omega_l: float, omega_r: float, wheel_separation: float, wheel_radius: float
) -> tuple[float, float]:
    """Forward differential kinematics → (v, omega)."""
    if wheel_radius <= 0.0 or wheel_separation <= 0.0:
        raise ValueError("wheel_radius and wheel_separation must be positive")
    v_l = omega_l * wheel_radius
    v_r = omega_r * wheel_radius
    v = 0.5 * (v_l + v_r)
    omega = (v_r - v_l) / wheel_separation
    return v, omega
