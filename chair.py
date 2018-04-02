from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import*


def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(0, 0, .5, 1)
    gluPerspective(60,1,0.1,50)
    gluLookAt(15, 15, 15 ,0, 0, 0, 0, 1, 0)


def chair():
    #center
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0,0,0)
    glTranslate(5,0,0)
    glScale(3,.5,2.5)
    glLineWidth(2)
    #glutSolidCube(2)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()
########################################

#back

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0,0,0)
    glTranslate(5 , 3.5 ,-3 )
    glScale(3,3.5,.5)
    glLineWidth(2)
    glutWireCube(2)
    #glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()
################################################
# rigt forward leg
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0,0,0)
    glTranslate(7.5 , -3.5 ,2 )
    glScale(.5,3,.5)
    glLineWidth(2)
    glutWireCube(2)
    #glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()
  ###################################################
    # left forward leg
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0,0,0)
    glTranslate(2.5 , -3.5 ,2 )
    glScale(.5,3,.5)
    glLineWidth(2)
    glutWireCube(2)
    #glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()
###########################################################
     # right backward leg
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0,0,0)
    glTranslate(7.5 , -3.5 ,-2)
    glScale(.5,3,.5)
    glLineWidth(2)
    glutWireCube(2)
    #glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()
###############################################################

 # left backward leg
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0,0,0)
    glTranslate(2.5 , -3.5 ,-2 )
    glScale(.5,3,.5)
    glLineWidth(2)
    glutWireCube(2)
    #glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()


def draw():
 #Drawing
 glMatrixMode(GL_MODELVIEW)
 glLoadIdentity()
 glClear(GL_COLOR_BUFFER_BIT)

 chair()
 glTranslate(-10,0,0)
 chair()

 glFlush()







































































glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"program")
glutDisplayFunc(draw)
myInit()
glutMainLoop()
