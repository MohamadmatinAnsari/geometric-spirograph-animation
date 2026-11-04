# Geometric Spirograph & Wave Animation

A modern 2D geometric animation built with Python and the **Pygame** library, showcasing visual harmonic wave patterns driven by mathematical trigonometric functions.

## Features

- Smooth 60 FPS rendering.
- 18 dynamic orbiting circles with oscillating radii.
- Real-time color transitions between vibrant cyan and pink.
- Geometric connecting lines linking the centers of consecutive circles.
- On-screen HUD displaying live FPS and exit instructions.

## Prerequisites

To run this project, you need Python installed along with the `pygame` library:
```bash
pip install pygame
```

## How to Run
Navigate to the project directory in your terminal or PowerShell and run:

```bash
python main.py
```

##Controls
ESC: Exit the application.
Window Close Button (X): Quit the program.

##Mathematical Concepts Used
This project leverages trigonometric functions for:
Oscillating radii: math.sin
Orbital positioning: math.cos and math.sin
Color interpolation: Weighted blending of primary and secondary colors using sine waves over time.
