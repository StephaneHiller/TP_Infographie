#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

###############################################################
# portage de planet.c

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import time

###############################################################
# variables globales

quadric = None
pas = 0.5
eyeX, eyeY, eyeZ, camX, camY, camZ = 80,60,-50,0,0,0
canonGD, canonHB, canonRotHB = 0, 0, 0
rot = 0
bouletMvt = 0
t = 0



###############################################################
# 

def init():
	global quadric
	glClearColor (0.0, 0.0, 0.0, 0.0)
	glShadeModel(GL_SMOOTH)
	quadric = gluNewQuadric()
	gluQuadricDrawStyle(quadric, GLU_FILL)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_COLOR_MATERIAL)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_POSITION, [100,100,0,0])
	

def champDeBataille():
	########## PREMIER PAVE DE TERRE ##########
	glPushMatrix()
	glScalef(1,0.3,1)
	glutSolidCube(3)
	glPopMatrix()
	
	########## PAVE D'EAU ##########
	glPushMatrix()
	glScalef(1,0.25,1)
	glTranslatef(0,-0.3,3)
	glColor4f(0,0,1,1)
	glutSolidCube(3)
	glPopMatrix()
	
	########## SECOND PAVE DE TERRE ##########
	glPushMatrix()
	glScalef(1,0.3,1)
	glTranslatef(0,0,6)
	glColor4f(0,1,0,1)
	glutSolidCube(3)
	glTranslatef(0,2.5,1)
	glScalef(0.1,0.35,0.1)
	# Dessine la cible #
	glPushMatrix()
	glColor4f(1,1,1,1)
	gluDisk(gluNewQuadric(),1.5,2,100,100)
	glColor4f(1,0,0,1)
	gluDisk(gluNewQuadric(),1,1.5,100,100)
	glColor4f(1,1,1,1)
	gluDisk(gluNewQuadric(),0.5,1,100,100)
	glColor4f(1,0,0,1)
	gluDisk(gluNewQuadric(),0,0.5,100,100)	
	glPopMatrix()
	glPopMatrix()
	
	
def canon():
	
	#parametres physiques
	global t
	alpha = -canonRotHB * 2 * math.pi /360
	v0 = 55
	m = 1
	g = 9.81
	k = 0.000018*6*math.pi*2.8/2
	myConst = v0*math.sin(alpha)+(g*m)/k
	myZ = (m/k)*(myConst*(1-math.exp(-k*t/m))-g*t)


	
	glPushMatrix()
	glColor4f(0.4,0.4,0.4,1)
	glScalef(0.02,0.02,0.02)
	
	glPushMatrix()
	glTranslatef(0,0,3.5)
	glutSolidTorus(1.0, 2.0, 100, 100);
	glPopMatrix()

	glPushMatrix()	
	glTranslatef(0,0,-3.5)
	glutSolidTorus(1.0, 2.0, 100, 100);
	glPopMatrix()
	
	glPushMatrix()
	glRotate(-90,0,1,0)
	glRotate(canonRotHB,1,0,0)
	gluCylinder(gluNewQuadric(),2.6,1.5 ,13,100,100)
	glPopMatrix()
	
	glPushMatrix()
	gluSphere(gluNewQuadric(), 2.8, 50, 16)
	glPopMatrix()

	glPushMatrix()
	glTranslate(-(math.cos(alpha)*v0*t - (m/k) * (math.exp(-k * t / m) - 1)), max(myZ,0), 0)
	gluSphere(gluNewQuadric(), 2.8/2, 50, 16)
	glPopMatrix()

	glPopMatrix()
	

#Fonction qui dessine les deux sphères, gère leurs dimensions ainsi que leurs couleurs
#En plus de cela, les lignes glRotate et glTranslate gèrent respectivement la rotation et la translation des sphères
def display():
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
	
	
    #Définie la couleur de la première planète
	glColor4f (0, 1, 0, 1 )
	
	#Context 1: context initial
	glPushMatrix()
	
   	gluLookAt(eyeX,eyeY,eyeZ,camX,camY,camZ, 0.0, 1.0, 0.0)

	champDeBataille()
	
	glPushMatrix()
	glTranslate(canonGD,0.5,canonHB)
	
	glTranslate(0,-0.5,0)
	glRotate(rot,0,1,0)
	glTranslate(0,0.5,0)

	canon()
	glPopMatrix()
	
		
	glPopMatrix()
	

	glutSwapBuffers()


#Permet aux sphères de se redimensionner lorsque l'on change la taille de la fenètre
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if width <= height:
	glOrtho(-2.5, 2.5, -2.5*height/width, 2.5*height/width, -10.0, 1000.0)
    else:
	glOrtho(-2.5*width/height, 2.5*width/height, -2.5, 2.5, -10.0, 1000.0)
    glMatrixMode(GL_MODELVIEW)


#permet de reconnaître les entrées claviers et d'animer les planêtes
def keyboard(key, x, y):
    global eyeX, eyeY, eyeZ, camX, camY, camZ, pas, canonGD, canonHB, rot, canonRotHB, bouletMvt, t 

    if key == 's':
		camY -= pas
    elif key == 'z':
		camY += pas
    elif key == 'q':
		camX -= pas
    elif key == 'd':
		camX += pas
    elif key == 'a':
		camZ -= pas
    elif key == 'e':
		camZ += pas
    elif key == 't':
		eyeY -= pas
    elif key == 'g':
		eyeY += pas
    elif key == 'f':
		eyeX -= pas
    elif key == 'h':
		eyeX += pas
    elif key == 'r':
		eyeZ -= pas
    elif key == 'y':
		eyeZ += pas
    elif key == 'p':
		pas += 0.5
    elif key == 'm':
		pas -= 0.5
    elif key == 'r':
		eyeX, eyeY, eyeZ, camX, camY, camZ = 0,6.7,7,0,0,0
    elif key == 'k':
		canonHB -= 0.05
		rot = -90
    elif key == 'i':
		canonHB += 0.05
		rot = 90
    elif key == 'j':
		canonGD += 0.05
		rot = 180
    elif key == 'l':
		canonGD -= 0.05
		rot = 0
    elif key == 'u':
		canonRotHB += 1
    elif key == 'o':
		canonRotHB -= 1
    elif key == ' ':
		t += 0.1
    elif key == 'c':
		t = 0
        
    elif key == '\033':
        sys.exit( )
    glutPostRedisplay()  # indispensable en Python
    

 

###############################################################
# MAIN


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

#Créer 
glutCreateWindow('Canon')
glutReshapeWindow(1600, 1000)

glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)

init()

glutMainLoop()
