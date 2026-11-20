#!/usr/bin/env python3
"""Keep Limo Pro teaching constants consistent across URDF, sim, and Nav2 config.

Student-runnable on the host (no ROS / Docker).
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]

# Published AgileX Limo Pro teaching numbers used in course materials.
EXPECTED = {
    "body_length": 0.322,
    "body_width": 0.220,
    "tread": 0.175,
    "wheel_radius": 0.040,
    "wheelbase": 0.200,
}


def _xacro_float(text: str, name: str) -> float:
    match = re.search(
        rf'<xacro:property\s+name="{re.escape(name)}"\s+value="([0-9.]+)"\s*/>',
        text,
    )
    assert match, f"missing xacro property {name}"
    return float(match.group(1))


def test_urdf_body_matches_limo_pro_spec() -> None:
    body = (ROOT / "code/ros2_ws/src/physibot_description/urdf/limo_body.xacro").read_text(
        encoding="utf-8"
    )
    for key, value in EXPECTED.items():
        assert _xacro_float(body, key) == pytest.approx(value)


def test_kinematics_module_documents_same_defaults() -> None:
    src = (
        ROOT / "code/ros2_ws/src/physibot_sim/physibot_sim/kinematics.py"
    ).read_text(encoding="utf-8")
    assert "0.175" in src
    assert "0.04" in src


def test_odom_node_default_params_match_urdf() -> None:
    src = (
        ROOT / "code/ros2_ws/src/physibot_sim/physibot_sim/diff_drive_odom_node.py"
    ).read_text(encoding="utf-8")
    assert 'declare_parameter("wheel_separation", 0.175)' in src
    assert 'declare_parameter("wheel_radius", 0.04)' in src


def test_nav2_params_mention_limo_footprint() -> None:
    text = (
        ROOT / "code/ros2_ws/src/physibot_bringup/config/nav2_params.yaml"
    ).read_text(encoding="utf-8")
    assert "175" in text or "0.175" in text
    assert "322" in text or "0.322" in text
    assert "base_footprint" in text


def test_demo_map_yaml_is_parseable() -> None:
    yaml_path = ROOT / "code/ros2_ws/src/physibot_bringup/maps/demo_map.yaml"
    pgm_path = ROOT / "code/ros2_ws/src/physibot_bringup/maps/demo_map.pgm"
    text = yaml_path.read_text(encoding="utf-8")
    assert "image: demo_map.pgm" in text
    assert "resolution:" in text
    assert "origin:" in text
    assert pgm_path.is_file()
    assert pgm_path.stat().st_size > 0
