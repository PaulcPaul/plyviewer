from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np

from reader import read_model_points

w, h = 700, 700

# variables for bunny model
points, tris, normals, num_normals, num_points, num_faces = read_model_points()

# for glDrawElements
flat_tris = [item for sublist in tris for item in sublist] 
num_tris = len(flat_tris)

spin = 0

def init():
    global points, normals, num_points

    luzAmbiente  = [0.2, 0.2, 0.2, 1.0]
    luzDifusa    = [0.7, 0.7, 0.7, 1.0]
    luzEspecular = [1.0, 1.0, 1.0, 1.0] 
    posicaoLuz   = [60.0, 60.0, 0.0, 1.0]

    especularidade = [1.0, 1.0, 1.0, 1.0]
    especMaterial  = 60

    glClearColor (0.2, 0.2, 0.2, 0.3)
    glShadeModel (GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade)
    glMateriali(GL_FRONT, GL_SHININESS, especMaterial)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular)
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

    glEnableClientState(GL_NORMAL_ARRAY)
    glEnableClientState(GL_VERTEX_ARRAY)

    glVertexPointer(3, GL_FLOAT, 0, points)
    glNormalPointer(GL_FLOAT, 0, normals)

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
    global spin, flat_tris, num_tris

    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, -0.5, 0.0)

    draw_axis()

    glColor3f (1.0, 0.0, 1.0) # rabbit's color

    glScalef (5.0, 5.0, 5.0)
    #glTranslatef(0, 0, 0)
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
    glutInitWindowSize (w, h)
    glutInitWindowPosition (100, 0)
    glutCreateWindow ("Stuff")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(33, Timer, 1)
    glutMainLoop()