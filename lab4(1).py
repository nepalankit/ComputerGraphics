from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define initial translation values
translation_x = 0.5
translation_y = 0.5

# Define the vertices of a triangle
vertices = [
    [-0.5, -0.5],
    [0.5, -0.5],
    [0.0, 0.5]
]

def draw_triangle():
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()
     

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(translation_x, translation_y, 0.0)
    draw_triangle()
    glFlush()

    