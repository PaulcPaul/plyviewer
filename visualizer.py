from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np

from reader import read_model_points

points, tris, num_points, num_faces = read_model_points()
flat_tris = [item for sublist in tris for item in sublist]
num_tris = len(flat_tris)

spin = 0

def init():
    global points, num_points
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_SMOOTH)

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, points)

def draw_axis():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES) # X
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES) # Y
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES) # Z
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)
    glEnd()

def display():
    global spin, tris, points, num_points, num_faces, flat_tris, num_tris

    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 0.0, 1.0)
    glLoadIdentity()

    draw_axis()

    glScalef (7.0, 7.0, 7.0)
    glTranslatef(0, -.05, -.05)
    glRotatef(spin, 0, 1, 0)

    glDrawElements(GL_TRIANGLES, num_tris, GL_UNSIGNED_INT, flat_tris)

    #glDrawArrays(GL_POINTS, 0, num_points)

    glutSwapBuffers()

def Timer(value):
    global spin

    spin += 2.0
    if spin == 360.0:
       spin = 0

    glutPostRedisplay()
    glutTimerFunc(33, Timer, 1)

def reshape (w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(90.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize (500, 500)
    glutInitWindowPosition (100, 100)
    glutCreateWindow ("Stuff")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(33, Timer, 1)
    glutMainLoop()