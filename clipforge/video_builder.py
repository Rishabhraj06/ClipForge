"""FFmpeg video compilation engine."""

import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional

from clipforge.frame_engine import FrameEngine


class VideoBuilder:
    """Builds MP4 and GIF short videos from code typing animation."""

    @classmethod
    def render_short(
        cls,
        code_text: str,
        output_mp4: Path,
        output_gif: Optional[Path] = None,
        title: str = "⚡ PYTHON SPEED RUN",
        caption: str = "Follow @Rishabhraj06 for dev tips",
        fps: int = 15,
        duration_sec: float = 6.0,
        resolution: tuple = (720, 1280)
    ):
        engine = FrameEngine(width=resolution[0], height=resolution[1])
        temp_dir = Path(output_mp4).parent / ".temp_clipforge_frames"
        temp_dir.mkdir(parents=True, exist_ok=True)

        total_frames = int(fps * duration_sec)
        total_chars = len(code_text)

        # Typing takes first 65% of the video, remaining 35% is pause/inspect
        type_frames = int(total_frames * 0.65)

        for f_idx in range(total_frames):
            if f_idx < type_frames:
                chars = int((f_idx / type_frames) * total_chars)
            else:
                chars = total_chars

            prog = f_idx / total_frames
            phase = f_idx * 0.35

            frame = engine.render_frame(
                full_code=code_text,
                chars_revealed=chars,
                title=title,
                caption=caption,
                progress_pct=prog,
                wave_phase=phase
            )

            frame.save(temp_dir / f"f_{f_idx:04d}.png")

        # Compile MP4
        cmd_mp4 = [
            "ffmpeg", "-y", "-framerate", str(fps),
            "-i", str(temp_dir / "f_%04d.png"),
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-crf", "22", str(output_mp4)
        ]
        subprocess.run(cmd_mp4, check=True)

        # Compile GIF if requested
        if output_gif:
            cmd_gif = [
                "ffmpeg", "-y", "-i", str(output_mp4),
                "-vf", f"fps=10,scale={resolution[0] // 2}:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=64[p];[s1][p]paletteuse=dither=bayer",
                str(output_gif)
            ]
            subprocess.run(cmd_gif, check=True)

        shutil.rmtree(temp_dir, ignore_errors=True)
