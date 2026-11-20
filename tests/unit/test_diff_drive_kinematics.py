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
    sep, radius = 0.175, 0.04  # Limo Pro tread / course wheel radius
    v, omega = 0.3, 0.4
    w_l, w_r = wheel_speeds_from_twist(v, omega, sep, radius)
    v2, omega2 = twist_from_wheel_speeds(w_l, w_r, sep, radius)
    assert v2 == pytest.approx(v)
    assert omega2 == pytest.approx(omega)


def test_rejects_negative_dt() -> None:
    with pytest.raises(ValueError):
        integrate_unicycle(Pose2D(), 0.1, 0.0, -0.01)
