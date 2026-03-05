# Human Benchmark Aim Bot

A simple Python script that automatically detects a target on the screen and clicks it using image recognition.  
Built to experiment with screen automation and reaction-time optimization.

## Features

- Detects target images on screen
- Automatically moves the mouse to the detected location
- Instantly clicks the target
- Uses OpenCV-based image matching for better accuracy

## How It Works

The script continuously scans the screen using PyAutoGUI.  
When the target image appears, the program detects its location and immediately clicks it, effectively removing human reaction delay.

## Requirements

- Python 3
- pyautogui
- opencv-python
