#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

###############################################################
# portage de planet.c

from OpenGL.GL import *  # exception car prefixe systematique
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

###############################################################
# variables globales
year, day = 0, 0
year2 = 0
quadric = None

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
	


#Fonction qui dessine les deux sphères, gère leurs dimensions ainsi que leurs couleurs
#En plus de cela, les lignes glRotate et glTranslate gèrent respectivement la rotation et la translation des sphères
def display():
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
	
    #Définie la couleur de la première planète
	glColor4f (0.627451, 0.321569, 0.176471, 1.0)
	
	#Context 1: context initial
	glPushMatrix()
	#Dessine la première planête dans le contexte 1
	gluSphere(quadric, 1.0, 50, 16)
	
	#Conntext 2: le soleil
	glPushMatrix()
	
	#Effectue les rotations et translation correspondant au déplacement de la lune
	glRotatef(year, 0.0, 1.0, 0.0)
	glTranslatef(2.7, 0.0, 0.0)
	glRotatef(day, 0.0, 1.0, 0.0)
	
	#Dessine la première planête avec une nouvelle couleur
	glColor4f (0.8 , 0.4 , 0.0, 1.0)
	gluSphere(quadric, 0.2, 50, 8)
	
	#Effectue les rotations et translation afin de placer une lune
	glRotatef(year, 0.0, 1.0, 0.0)
	glTranslatef(0.5, 0.0, 0.0)
	glRotatef(day, 0.0, 1.0, 0.0)
	
	#Dessine une lune avec une nouvelle couleur
	glColor4f (0.4 , 0.7 , 0.2, 1.0)
	gluSphere(quadric, 0.1, 50, 8)
	
	#Retour au context ou l'origine est le soleil
	glPopMatrix()
	
	#Effectue les rotations et translation afin de placer une seconde planête qui tourne à une vitesse différente de la première
	glRotatef(year2, 0.0, 1.0, 0.0)
	glTranslatef(1.8, 0.0, 0.0)
	
	#Dessine une seconde planête avec une nouvelle couleur
	glColor4f (0.4, 0.3 , 0.2, 1.0)
	gluSphere(quadric, 0.3, 50, 8)

	#Retour au context initial
	glPopMatrix()

	glutSwapBuffers()


#Permet aux sphères de se redimensionner lorsque l'on change la taille de la fenètre
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if width <= height:
	glOrtho(-2.5, 2.5, -2.5*height/width, 2.5*height/width, -10.0, 10.0)
    else:
	glOrtho(-2.5*width/height, 2.5*width/height, -2.5, 2.5, -10.0, 10.0)
    glMatrixMode(GL_MODELVIEW)


#permet de reconnaître les entrées claviers et d'animer les planêtes
def keyboard(key, x, y):
    global day, year, year2
    if key == 'd':
        day = (day + 10) % 360
    if key == 't':
        day = (day + 8) % 360
        year = (year + 3) % 360
        year2 = (year2 + 2) % 360
    elif key == 'y':
        year = (year + 5) % 360
    
    elif key == '\033':
        sys.exit( )
    glutPostRedisplay()  # indispensable en Python
    

 

###############################################################
# MAIN


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)

#Créer 
glutCreateWindow('planet')
glutReshapeWindow(512,512)

glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)

init()

glutMainLoop()
