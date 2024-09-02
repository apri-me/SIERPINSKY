# Computer Graphics Project

This project showcases three classic computer graphics examples: Sierpinski triangles, Mandelbrot sets, and a bouncing ball animation.

## Installation

1. **Create a virtual environment:**

   ```bash
   python3 -m venv env
   ```

2. **Activate the environment:**

   ```bash
   source env/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. **Start the main menu:**

   ```bash
   python app.py
   ```

2. **Choose a program from the menu:**

   - **Sierpinski Curves:** Generates a fractal Sierpinski triangle. You can select the level of recursion.
   - **Mandelbrot Sets:** Displays a visualization of the Mandelbrot set. You can adjust the number of iterations and color palette.
   - **Ball Animation:** Shows a bouncing ball moving across the screen.

3. **Press ESC or close the window to exit.**

## Code Structure

- **`app.py`:** Main application file, handles user input and menu navigation.
- **`sections/`:** Contains modules for each program:
    - **`ball_anim.py`:** Bouncing ball animation.
    - **`mandelbrot.py`:** Mandelbrot set generation.
    - **`sierpinsky.py`:** Sierpinski triangle generation.
- **`__init__.py`:** Initializes the `sections` package.

## Dependencies

- **pygame:** A library for creating games and multimedia applications.
- **pygame-menu:** A library for creating menus in Pygame.

## Notes

- This project is designed for Python 3.8 or later.
- The `__pycache__` directory contains compiled bytecode files and can be ignored.
- The `.gitignore` file lists files and directories that should be excluded from version control.