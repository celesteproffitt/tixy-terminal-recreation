# Tixy.land Terminal Recreation

A terminal-based recreation inspired by [tixy.land](https://tixy.land/), written in Python.

## About

This program generates animated patterns in the terminal using mathematical expressions based on position, index, and time. Each point in an 8×8 grid is evaluated and converted into a character from a text gradient to create a simple animated display.

Users can enter their own equation when the program starts, or use the default animation.

## Features

* 8×8 animated terminal display
* User-defined mathematical expressions
* Variables for `x`, `y`, index (`i`), and time (`t`)
* Character gradient used to represent different calculated values
* Adjustable animation speed, runtime, screen size, and gradient
* Works with Windows and Unix-style terminal clearing

## Example Equation

```python
math.sin(t + y)
```

Other expressions can be entered when the program starts to generate different animations.

## Technologies

* Python
* Python `math` module
* Terminal/console output

## Running the Program

1. Install Python 3.
2. Download or clone this repository.
3. Run:

```bash
python tixy_terminal.py
```

4. Enter a mathematical expression when prompted, or press Enter to use the default expression.

## Inspiration

This project was inspired by [tixy.land](https://tixy.land/), a minimalist creative coding environment for generating mathematical animations.

## Note

The program uses Python's `eval()` function to evaluate entered expressions. Only enter expressions you trust when running the program.
