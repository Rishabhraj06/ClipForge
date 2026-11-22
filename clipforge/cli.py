"""ClipForge CLI: Autonomous Code-to-Shorts generator."""

import argparse
import sys
from pathlib import Path

from clipforge.video_builder import VideoBuilder


def main():
    parser = argparse.ArgumentParser(
        prog="clipforge",
        description="Autonomous code-to-vertical-shorts video generator for YouTube Shorts, Reels, and TikTok."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    render_parser = subparsers.add_parser("render", help="Render code snippet into vertical 9:16 video")
    render_parser.add_argument("file", help="Path to Python or code file")
    render_parser.add_argument("-o", "--output", default="short.mp4", help="Output MP4 file path")
    render_parser.add_argument("--gif", action="store_true", help="Also generate an animated GIF preview")
    render_parser.add_argument("--title", default="⚡ PYTHON SPEED RUN", help="Hook title displayed at top")
    render_parser.add_argument("--caption", default="Follow @Rishabhraj06 for tech tips", help="Bottom caption")
    render_parser.add_argument("--duration", type=float, default=6.0, help="Video duration in seconds")
    render_parser.add_argument("--fps", type=int, default=15, help="Video frames per second")

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"[Error] Target code file not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        code_text = f.read().strip()

    out_mp4 = Path(args.output).resolve()
    out_gif = out_mp4.with_suffix(".gif") if args.gif else None

    print(f"🎬 [ClipForge] Rendering vertical short for {file_path.name} ({len(code_text)} chars) ...")
    VideoBuilder.render_short(
        code_text=code_text,
        output_mp4=out_mp4,
        output_gif=out_gif,
        title=args.title,
        caption=args.caption,
        fps=args.fps,
        duration_sec=args.duration
    )
    print(f"🎉 [ClipForge] Successfully exported -> {out_mp4}")
    if out_gif:
        print(f"🎉 [ClipForge] Exported GIF preview  -> {out_gif}")


if __name__ == "__main__":
    main()
