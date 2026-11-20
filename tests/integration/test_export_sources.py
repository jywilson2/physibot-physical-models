#!/usr/bin/env python3
"""Ensure textbook export sources stay wired for PDF/DOCX builds."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

CHAPTER_FILES = [
    "00-outline.md",
    "01-welcome-and-docker.md",
    "02-linear-algebra-refresh.md",
    "03-mobile-robot-kinematics.md",
    "04-dynamics-and-physical-models.md",
    "05-sensing-and-observation-models.md",
    "06-estimation-fundamentals.md",
    "07-localization.md",
    "08-mapping-and-slam.md",
    "09-navigation-with-nav2.md",
    "10-learning-with-isaac-lab.md",
    "11-sim-to-real.md",
    "12-orin-nano-deploy.md",
    "13-dgx-spark-training.md",
    "14-capstone.md",
]


def test_all_chapters_exist_and_nonempty() -> None:
    for name in CHAPTER_FILES:
        path = ROOT / "chapters" / name
        assert path.is_file(), name
        assert path.stat().st_size > 100, f"{name} looks like a stub remnant"


def test_qmd_includes_every_chapter() -> None:
    qmd = (ROOT / "textbook" / "physibot.qmd").read_text(encoding="utf-8")
    for name in CHAPTER_FILES:
        assert name in qmd, f"physibot.qmd missing include for {name}"


def test_export_script_lists_every_chapter() -> None:
    script = (ROOT / "docs" / "export-tools" / "export-stub.sh").read_text(
        encoding="utf-8"
    )
    for name in CHAPTER_FILES:
        assert name in script


def test_export_math_extensions_enabled() -> None:
    script = (ROOT / "docs" / "export-tools" / "export-stub.sh").read_text(
        encoding="utf-8"
    )
    assert "tex_math_single_backslash" in script


def test_docker_textbook_recipe_present() -> None:
    assert (ROOT / "docker" / "Dockerfile.textbook").is_file()
    assert (ROOT / "docs" / "export-tools" / "export-pdf-docker.sh").is_file()


def test_sample_pdf_or_documented_path() -> None:
    """Prefer a committed sample PDF; otherwise docs must point at the recipe."""
    sample = ROOT / "textbook" / "exports" / "physibot.pdf"
    readme = (ROOT / "docs" / "export-tools" / "README.md").read_text(encoding="utf-8")
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    if sample.is_file():
        assert sample.stat().st_size > 10_000
        assert sample.stat().st_size < 5_000_000  # keep repo lean
    else:
        assert "export-pdf-docker.sh" in readme
        assert "PDF" in status
