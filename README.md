# 🎬 ClipForge

> **Autonomous Code-to-Vertical-Shorts generator.** Turn clean code snippets and git diffs into high-converting **9:16 vertical videos** for YouTube Shorts, Instagram Reels, and TikTok in seconds.

[![CI](https://github.com/Rishabhraj06/ClipForge/actions/workflows/ci.yml/badge.svg)](https://github.com/Rishabhraj06/ClipForge/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=flat&logo=ffmpeg&logoColor=white)](https://ffmpeg.org)
[![Pillow](https://img.shields.io/badge/Pillow-3776AB?style=flat&logo=python&logoColor=white)](https://python-pillow.org/)

---

## 🎬 Demo Preview

<p align="center">
  <img src="assets/demo.gif" alt="ClipForge Animated Vertical Preview" width="320"/>
</p>

---

## ⚡ The Creator Problem ClipForge Solves

Developers, technical educators, and dev-rel advocates want to share coding tips on Shorts & TikTok. But the current workflow is painful:
1. Recording terminal screens manually with OBS.
2. Importing files into Adobe Premiere or CapCut.
3. Cropping to vertical 9:16 and keyframing zoom animations.
4. Spending 45 minutes on a 15-second snippet.

**ClipForge automates everything headlessly with Python + FFmpeg:**
- 🎨 **Syntax Styler**: Multi-token code syntax highlighting (keywords, strings, comments, numbers).
- ⌨️ **Animated Typing**: Realistic keystroke typing cadence with blinking glowing cursor.
- 📐 **Mobile 9:16 Layout**: High-contrast card with macOS window chrome, header hook banner, and audio waveform visualizer.
- ⚡ **Instant Render**: Renders 1080x1920 or 720x1280 `.mp4` and compressed `.gif` previews in under 5 seconds.

---

## 🚀 Quickstart

### 1. Installation
```bash
git clone https://github.com/Rishabhraj06/ClipForge.git
cd ClipForge
pip install -r requirements.txt
pip install -e .
```

### 2. Generate a Vertical Short
```bash
clipforge render algorithm.py \
  --output algorithm_reel.mp4 \
  --gif \
  --title "🔥 100x SPEEDUP IN PYTHON" \
  --caption "Follow @Rishabhraj06 for dev tips" \
  --duration 5.0
```

---

## 🧪 Testing

```bash
python -m pytest tests/ -v
```

---

## 👤 Author

**Rishabh Raj**
- GitHub: [@Rishabhraj06](https://github.com/Rishabhraj06)
- Portfolio: [https://github.com/Rishabhraj06](https://github.com/Rishabhraj06)
