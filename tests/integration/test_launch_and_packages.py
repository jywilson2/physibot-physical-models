#!/usr/bin/env python3
"""Lightweight integration checks (host, no ROS runtime).

Validates that bringup launch files parse as Python and that package manifests
list the expected course packages and launch entry points.
"""

from __future__ import annotations

import ast
from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

ROOT = Path(__file__).resolve().parents[2]
WS = ROOT / "code" / "ros2_ws" / "src"
LAUNCH_DIR = WS / "physibot_bringup" / "launch"

EXPECTED_LAUNCHES = [
    "description.launch.py",
    "sim_diff_drive.launch.py",
    "sim_stub.launch.py",
    "localization.launch.py",
    "mapping.launch.py",
    "nav2.launch.py",
]


@pytest.mark.parametrize("name", EXPECTED_LAUNCHES)
def test_launch_file_parses(name: str) -> None:
    path = LAUNCH_DIR / name
    assert path.is_file(), path
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    # Launch files must define generate_launch_description
    fn_names = {
        node.name
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }
    assert "generate_launch_description" in fn_names


def test_package_xml_names() -> None:
    expected = {
        "physibot_bringup": WS / "physibot_bringup" / "package.xml",
        "physibot_description": WS / "physibot_description" / "package.xml",
        "physibot_sim": WS / "physibot_sim" / "package.xml",
    }
    for name, path in expected.items():
        root = ET.parse(path).getroot()
        pkg_name = root.findtext("name")
        assert pkg_name == name
        assert root.findtext("license") in {"Apache-2.0", "Apache 2.0"}


def test_sim_setup_registers_console_scripts() -> None:
    setup = (WS / "physibot_sim" / "setup.py").read_text(encoding="utf-8")
    assert "diff_drive_odom" in setup
    assert "stub_laser" in setup


def test_bringup_installs_launch_config_maps() -> None:
    cmake = (WS / "physibot_bringup" / "CMakeLists.txt").read_text(encoding="utf-8")
    for needle in ("launch", "config", "maps"):
        assert needle in cmake


def test_chapters_cross_link_labs_where_expected() -> None:
    """Narrative (when present) or stubs should mention the labs ladder."""
    labs_readme = (ROOT / "labs" / "README.md").read_text(encoding="utf-8")
    assert "01-docker-hello" in labs_readme
    assert "09-nav2" in labs_readme
    # Capstone chapter should exist for professor review packaging
    assert (ROOT / "chapters" / "14-capstone.md").is_file()
    # At least one early chapter should reference Docker / labs path
    ch01 = (ROOT / "chapters" / "01-welcome-and-docker.md").read_text(encoding="utf-8")
    assert "docker" in ch01.lower()
