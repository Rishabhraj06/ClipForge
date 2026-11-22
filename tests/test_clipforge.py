"""Unit tests for ClipForge syntax styler and frame rendering engine."""

import pytest
from PIL import Image
from clipforge.syntax_styler import SyntaxStyler
from clipforge.frame_engine import FrameEngine


SAMPLE_CODE = """
def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    return [x for x in arr[1:] if x < pivot] + [pivot] + [x for x in arr[1:] if x >= pivot]
"""


def test_syntax_styler_keywords():
    line = "def calculate_tax(amount: float) -> float:"
    tokens = SyntaxStyler.tokenize_line(line)
    texts = [t.text for t in tokens]
    assert "def" in texts
    
    def_token = next(t for t in tokens if t.text == "def")
    assert def_token.color == SyntaxStyler.THEME["keyword"]


def test_syntax_styler_comments():
    line = "x = 42 # Lucky number"
    tokens = SyntaxStyler.tokenize_line(line)
    comment_token = next((t for t in tokens if "#" in t.text), None)
    assert comment_token is not None
    assert comment_token.color == SyntaxStyler.THEME["comment"]


def test_frame_engine_dimensions():
    engine = FrameEngine(width=360, height=640)
    img = engine.render_frame(
        full_code=SAMPLE_CODE,
        chars_revealed=40,
        title="TEST RUN",
        caption="Unit Test Caption",
        progress_pct=0.5,
        wave_phase=1.0
    )
    assert isinstance(img, Image.Image)
    assert img.size == (360, 640)
