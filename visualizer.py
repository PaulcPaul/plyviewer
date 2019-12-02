from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np

from reader import read_model_points
from plymodel import PlyModel

w, h = 700, 700

model = PlyModel(*read_model_points())

zoom = 1.0

spin = 0

def init():
    global model

    luzDifusa    = [0.7, 0.7, 0.7, 1.0]
    luzEspecular = [1.0, 1.0, 1.0, 1.0] 
    posicaoLuz   = [60.0, 60.0, 0.0, 1.0]

    especularidade = [1.0, 1.0, 1.0, 1.0]
    especMaterial  = 40

    glClearColor(0.2, 0.2, 0.2, 0.3)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade)
    glMateriali(GL_FRONT, GL_SHININESS, especMaterial)

    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular)
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

    glEnableClientState(GL_NORMAL_ARRAY)
    glEnableClientState(GL_VERTEX_ARRAY)

    glVertexPointer(3, GL_FLOAT, 0, model.vertex_list)
    glNormalPointer(GL_FLOAT, 0, model.normal_list)

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
    global model, zoom

    glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0.0, -0.5, 0.0)

    draw_axis()

    glColor3f (1.0, 0.0, 1.0) # rabbit's color

    glScalef (zoom, zoom, zoom)
    glTranslatef(0, 0, 0)
    glRotatef(spin, 0, 1, 0)

    glDrawElements(GL_TRIANGLES, model.flattened_face_num, GL_UNSIGNED_INT, model.flattened_face_list)

    glutSwapBuffers()

def GerenciaTeclado(key, x, y):
    global zoom, spin

    key = key.decode("utf-8")
    
    if key == 'W' or key == 'w':
        zoom += 0.1
    if key == 'S' or key == 's':
        zoom -= 0.1
    if key == 'A' or key == 'a':
        spin += 10
    if key == 'D' or key == 'd':
        spin -= 10

    if zoom <= 0.0:
        zoom = 0.1

    glutPostRedisplay()

def reshape (w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(0.0, w/h, 1.0, 500.0)
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
    glutKeyboardFunc(GerenciaTeclado)
    #glutTimerFunc(33, Timer, 1)
    glutMainLoop()