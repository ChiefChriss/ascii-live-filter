# ASCII Live Filter 👁️

Real-time webcam-to-ASCII converter. Captures a live video feed, maps each frame's pixel brightness to ASCII characters, and displays it in a terminal-style window — all in real time.

## How It Works

1. Captures frames from a webcam (local or IP camera)
2. Converts each frame to grayscale
3. Maps pixel luminance to a density-ordered set of ASCII characters (`@%#*+=-:. `)
4. Renders the result in a Tkinter window at ~15-30 FPS

## Requirements

- Python 3.7+
- OpenCV (`opencv-python`)
- NumPy
- Tkinter (included with Python on macOS/Windows)

## Installation

```bash
pip install opencv-python numpy
git clone https://github.com/ChiefChriss/ascii-live-filter.git
cd ascii-live-filter
```

## Usage

```bash
python asciifilter.py
```

By default it connects to an IP webcam at `http://10.0.0.14:4747/video`. To use your built-in webcam instead, change line 55 in `asciifilter.py` from:

```python
cap = cv2.VideoCapture('http://10.0.0.14:4747/video')
```

to:

```python
cap = cv2.VideoCapture(0)
```

Press `Ctrl+C` or close the window to exit.

## Customization

- **Character set** — edit `ASCII_CHARS` on line 7 to change the visual style
- **Output width** — change `new_width` (default 160) on line 9 for wider/narrower output
- **Font size** — adjust `font=("Courier", 6)` on line 51

## License

MIT
