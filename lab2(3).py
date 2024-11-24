from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BAR_THICKNESS = 30  # Increased bar thickness

# Data for histogram
frequencies = [30, 50, 20, 60, 40, 70, 10, 35, 45, 55]

# Colors for histogram bars (normalized to 0-1 for OpenGL)
BAR_COLORS = [
    (0.55, 0.07, 0.72), (0.2, 0.24, 0.58), (0.0, 0.5, 0.0),
    (1.0, 0.27, 0.0), (1.0, 0.84, 0.0), (1.0, 0.08, 0.58),
    (0.0, 0.75, 1.0), (1.0, 0.41, 0.7), (0.5, 0.5, 0.5),
    (0.0, 0.0, 0.0)
]

def dda_line(x1, y1, x2, y2, color):
    """
    Draws a line using the DDA algorithm.
    Args:
        x1, y1: Starting coordinates of the line
        x2, y2: Ending coordinates of the line
        color: The color to draw the line in (tuple of RGB values)
    """
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return
    x_inc = dx / steps
    y_inc = dy / steps
    x = x1
    y = y1
    for _ in range(int(steps)):
        glColor3f(*color)
        glBegin(GL_POINTS)
        glVertex2f(int(x), int(y))
        glEnd()
        x += x_inc
        y += y_inc

def draw_bar(x, y, height, color):
    """
    Draws a single vertical bar using DDA line algorithm.
    The bar thickness is now effectively controlled by drawing several points vertically.
    """
    for i in range(BAR_THICKNESS):
        dda_line(x + i, y, x + i, y + height, color)  # Slightly offset the x to make it thicker

def draw_histogram():
    """
    Draws the histogram bars using DDA for each bar.
    """
    ##This function iterates over frequencies and uses draw_bar to draw each bar on the screen.
    x = 10  # Starting x-coordinate for the bars
    max_freq = max(frequencies)
    for freq, color in zip(frequencies, BAR_COLORS):
        # Scale the bar height to fit the window
        bar_height = freq * (WINDOW_HEIGHT - 100) / max_freq
        draw_bar(x, 50, bar_height, color)
        x += BAR_THICKNESS + 10  # Space between bars

def display():
    """
    OpenGL display callback function.
    """
    glClear(GL_COLOR_BUFFER_BIT)
    draw_histogram()
    glFlush()

def init():
    """
    Initialize the OpenGL environment.
    """
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)

def main():
    """
    Main function to set up the OpenGL application.
    """
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(b"Histogram using DDA")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
