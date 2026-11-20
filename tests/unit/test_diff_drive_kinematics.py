#!/usr/bin/env python3
"""Unit tests for planar diff-drive kinematics (no ROS required)."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

# Allow importing from the package source without installing
ROOT = Path(__file__).resolve().parents[2]
SYS_SRC = ROOT / "code" / "ros2_ws" / "src" / "physibot_sim"
sys.path.insert(0, str(SYS_SRC))

from physibot_sim.kinematics import (  # noqa: E402
    Pose2D,
    integrate_unicycle,
    twist_from_wheel_speeds,
    wheel_speeds_from_twist,
    wrap_to_pi,
)

# Course Limo Pro stub defaults (must match URDF / STATUS hardware table)
TREAD_M = 0.175
WHEEL_RADIUS_M = 0.04


def test_wrap_to_pi() -> None:
    assert wrap_to_pi(0.0) == pytest.approx(0.0)
    assert wrap_to_pi(math.pi) == pytest.approx(math.pi)
    assert abs(wrap_to_pi(-math.pi)) == pytest.approx(math.pi)
    assert wrap_to_pi(3.0 * math.pi) == pytest.approx(math.pi)
    assert wrap_to_pi(-3.0 * math.pi / 2.0) == pytest.approx(math.pi / 2.0)


def test_straight_line() -> None:
    pose = integrate_unicycle(Pose2D(), v=0.5, omega=0.0, dt=2.0)
    assert pose.x == pytest.approx(1.0)
    assert pose.y == pytest.approx(0.0)
    assert pose.yaw == pytest.approx(0.0)


def test_spin_in_place() -> None:
    pose = integrate_unicycle(Pose2D(), v=0.0, omega=math.pi / 2.0, dt=1.0)
    assert pose.x == pytest.approx(0.0, abs=1e-9)
    assert pose.y == pytest.approx(0.0, abs=1e-9)
    assert pose.yaw == pytest.approx(math.pi / 2.0)


def test_circular_arc_closes_approximately() -> None:
    # Drive a circle of radius 1 m: v=0.5, omega=0.5 → R=1; period = 2π/ω
    pose = Pose2D()
    v, omega, dt = 0.5, 0.5, 0.01
    period = 2.0 * math.pi / omega
    steps = int(round(period / dt))
    for _ in range(steps):
        pose = integrate_unicycle(pose, v=v, omega=omega, dt=dt)
    assert pose.x == pytest.approx(0.0, abs=0.05)
    assert pose.y == pytest.approx(0.0, abs=0.05)
    assert pose.yaw == pytest.approx(0.0, abs=0.1)


def test_inverse_forward_roundtrip() -> None:
    v, omega = 0.3, 0.4
    w_l, w_r = wheel_speeds_from_twist(v, omega, TREAD_M, WHEEL_RADIUS_M)
    v2, omega2 = twist_from_wheel_speeds(w_l, w_r, TREAD_M, WHEEL_RADIUS_M)
    assert v2 == pytest.approx(v)
    assert omega2 == pytest.approx(omega)


def test_rejects_negative_dt() -> None:
    with pytest.raises(ValueError):
        integrate_unicycle(Pose2D(), 0.1, 0.0, -0.01)


def test_zero_dt_is_noop() -> None:
    start = Pose2D(1.0, 2.0, 0.3)
    pose = integrate_unicycle(start, v=1.0, omega=0.5, dt=0.0)
    assert pose.x == pytest.approx(start.x)
    assert pose.y == pytest.approx(start.y)
    assert pose.yaw == pytest.approx(start.yaw)


def test_heading_affects_straight_motion() -> None:
    pose = integrate_unicycle(Pose2D(0.0, 0.0, math.pi / 2.0), v=1.0, omega=0.0, dt=1.0)
    assert pose.x == pytest.approx(0.0, abs=1e-9)
    assert pose.y == pytest.approx(1.0)
    assert pose.yaw == pytest.approx(math.pi / 2.0)


def test_equal_wheel_speeds_give_pure_translation() -> None:
    omega_w = 2.5  # rad/s
    v, omega = twist_from_wheel_speeds(omega_w, omega_w, TREAD_M, WHEEL_RADIUS_M)
    assert omega == pytest.approx(0.0)
    assert v == pytest.approx(omega_w * WHEEL_RADIUS_M)


def test_opposite_wheel_speeds_give_pure_rotation() -> None:
    omega_w = 3.0
    v, omega = twist_from_wheel_speeds(-omega_w, omega_w, TREAD_M, WHEEL_RADIUS_M)
    assert v == pytest.approx(0.0)
    assert omega == pytest.approx(2.0 * omega_w * WHEEL_RADIUS_M / TREAD_M)


@pytest.mark.parametrize(
    "bad_sep,bad_radius",
    [
        (0.0, 0.04),
        (-0.1, 0.04),
        (0.175, 0.0),
        (0.175, -0.01),
    ],
)
def test_rejects_nonpositive_geometry(bad_sep: float, bad_radius: float) -> None:
    with pytest.raises(ValueError):
        wheel_speeds_from_twist(0.1, 0.0, bad_sep, bad_radius)
    with pytest.raises(ValueError):
        twist_from_wheel_speeds(1.0, 1.0, bad_sep, bad_radius)
