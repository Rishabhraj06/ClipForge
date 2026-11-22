"""Vertical 9:16 video frame generator for mobile short-form video."""

import math
from pathlib import Path
from typing import List
from PIL import Image, ImageDraw, ImageFont

from clipforge.syntax_styler import SyntaxStyler, Token


class FrameEngine:
    """Renders 9:16 vertical video frames optimized for TikTok and YouTube Shorts."""

    def __init__(self, width: int = 720, height: int = 1280):
        self.width = width
        self.height = height

        try:
            self.font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 22)
            self.font_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 24)
            self.font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 32)
            self.font_caption = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 20)
        except Exception:
            self.font_code = ImageFont.load_default()
            self.font_bold = self.font_code
            self.font_title = self.font_code
            self.font_caption = self.font_code

    def render_frame(
        self,
        full_code: str,
        chars_revealed: int,
        title: str = "⚡ PYTHON SPEED RUN",
        caption: str = "Follow for daily engineering tips",
        progress_pct: float = 0.0,
        wave_phase: float = 0.0
    ) -> Image.Image:
        img = Image.new("RGB", (self.width, self.height), (10, 12, 18))
        draw = ImageDraw.Draw(img)

        # 1. Subtle Radial Glow Background
        cx, cy = self.width // 2, self.height // 2
        for r in range(400, 100, -60):
            alpha_color = (25 + (400 - r) // 15, 20 + (400 - r) // 18, 45 + (400 - r) // 10)
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=alpha_color)

        # 2. Viral Header Banner
        banner_box = [40, 90, self.width - 40, 170]
        draw.rounded_rectangle(banner_box, radius=18, fill=(244, 63, 94))
        draw.text((60, 112), title.upper(), font=self.font_title, fill=(255, 255, 255))

        # 3. Floating Code Card
        card_box = [40, 210, self.width - 40, self.height - 240]
        draw.rounded_rectangle(card_box, radius=24, fill=SyntaxStyler.THEME["card_bg"], outline=(48, 54, 66), width=2)

        # Window Controls
        draw.ellipse([64, 234, 76, 246], fill=(239, 68, 68))
        draw.ellipse([86, 234, 98, 246], fill=(234, 179, 8))
        draw.ellipse([108, 234, 120, 246], fill=(34, 197, 94))
        draw.text((self.width // 2 - 45, 230), "main.py", font=self.font_caption, fill=(148, 163, 184))

        # Divider line
        draw.line([40, 266, self.width - 40, 266], fill=(38, 44, 56), width=1)

        # 4. Render Typing Code
        visible_code = full_code[:chars_revealed]
        lines = visible_code.splitlines() or [""]
        start_y = 286
        line_height = 34

        cursor_x, cursor_y = 70, start_y

        for idx, line in enumerate(lines):
            y_pos = start_y + (idx * line_height)
            if y_pos > card_box[3] - 40:
                break

            # Line number
            draw.text((60, y_pos), f"{idx+1:2d}", font=self.font_code, fill=(80, 90, 110))

            # Code tokens
            x_pos = 110
            tokens = SyntaxStyler.tokenize_line(line)
            for t in tokens:
                draw.text((x_pos, y_pos), t.text, font=self.font_code, fill=t.color)
                # approx width per monospace char
                x_pos += len(t.text) * 12

            if idx == len(lines) - 1:
                cursor_x = x_pos
                cursor_y = y_pos

        # Draw glowing cursor
        if chars_revealed < len(full_code) or int(wave_phase * 2) % 2 == 0:
            draw.rectangle([cursor_x + 2, cursor_y + 4, cursor_x + 14, cursor_y + 26], fill=(56, 189, 248))

        # 5. Audio Waveform Simulator Bars at Bottom
        bars_count = 24
        bar_w = 12
        bar_gap = 12
        total_w = bars_count * (bar_w + bar_gap)
        start_bx = (self.width - total_w) // 2
        base_by = self.height - 140

        for b in range(bars_count):
            h_bar = 8 + int(24 * abs(math.sin(wave_phase + (b * 0.4))))
            bx = start_bx + b * (bar_w + bar_gap)
            draw.rounded_rectangle([bx, base_by - h_bar, bx + bar_w, base_by + h_bar], radius=4, fill=(99, 102, 241))

        # 6. Bottom Caption & Brand
        draw.text((self.width // 2 - 140, self.height - 90), caption, font=self.font_caption, fill=(203, 213, 225))

        # 7. Progress Bar at bottom
        prog_w = int(self.width * min(1.0, max(0.0, progress_pct)))
        draw.rectangle([0, self.height - 6, prog_w, self.height], fill=(52, 211, 153))

        return img
