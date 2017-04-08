# coding: utf-8

import os
import cng
import math
import random
import time

LARGEUR_ECRAN = 1000
HAUTEUR_ECRAN = 1000

#Coordonnées de la fenetre dans l'ecran
global xFen1, yFen1, xFen2, yFen2

#Coordonnées de l'espace continu observé
global xCon1, yCon1, xCon2, yCon2

def bigPoint(x,y) :
	cng.disc(x,y,5)

#initialise un écran hauteur HAUTEUR_ECRAN et de largeur LARGEUR_ECRAN
#px1, py1 correspondent au coin inférieur gauche de la fenetre à l'intérieur de l'écran
#px2, py2 correspondent au coin supérieur droit de la fenètre ç l'intérieur de l'écran
def init_fenetre(px1, py1, px2, py2):
	global xFen1, yFen1, xFen2, yFen2
	xFen1, yFen1, xFen2, yFen2 = px1, py1, px2, py2
	
	cng.init_window('Bresenham', LARGEUR_ECRAN, HAUTEUR_ECRAN, 'white')
	cng.rectangle(px1,py1,px2,py2)		



#Initialise l'espace euclidien
#x1, y1 correspondent au coin inférieur gauche de l'espace euclidien
#x2, y2 correspondent au coin supérieur droit de l'espace euclidien 
def init_euclidien_space(x1, y1, x2, y2):
	global xCon1, yCon1, xCon2, yCon2
	xCon1, yCon1, xCon2, yCon2 = x1, y1, x2, y2

#Définie l'origine du repère en y placant un gros point rouge	
def origin():
	cng.current_color("red")
	(x0, y0) = convertPoint(0,0)
	bigPoint(x0,y0)
	cng.current_color("black")
	
#Convertit les coordonnées du point (x, y) en sa position dans la fenêtre
def convertPoint(x ,y):
	global xFen1, yFen1, xFen2, yFen2, xCon1, yCon1, xCon2, yCon2
	dFx = xFen2-xFen1
	dFy = yFen2-yFen1
	dCx = xCon2-xCon1
	dCy = yCon2-yCon1
	
	xScreen = int(x*dFx/float(dCx) - xCon1*dFx/float(dCx) + xFen1)
	yScreen = int(y*dFy/float(dCy) - yCon1*dFy/float(dCy) + yFen1) 
	
	return (xScreen, yScreen)

#Algorithme de Breseham appliqué à tous les octants
def Bresenham(xA, yA, xB, yB):
	
	#On convertit les données de l'espace continu à l'espace discret
	(xA, yA) = convertPoint(xA, yA)
	(xB, yB) = convertPoint(xB, yB)
	
	dx = xB - xA
	dy = yB - yA
	if(dx != 0):
		rapport = abs(dy/dx)
	else:
		rapport = float('inf')
	
	#Cas ou l'on se trouve dans l'octant 1
	if(dx >= 0 and dy >= 0 and rapport <= 1):
		dx = xB - xA
		dy = yB - yA
		dec = dx - 2*dy
		x, y = xA, yA
		while x <= xB:
			cng.point(x, y)
			if dec < 0:
				dec += 2*dx
				y += 1
			dec -= 2*dy
			x += 1		
	#Cas ou l'on se trouve dans l'octant 2
	elif(dx >= 0 and dy >= 0 and rapport > 1):
		xA, yA = yA, xA
		xB, yB = yB, xB
		
		dx = xB - xA
		dy = yB - yA
		dec = dx - 2*dy
		x, y = xA, yA
		while x <= xB:
			cng.point(y, x)
			if dec < 0:
				dec += 2*dx
				y += 1
			dec -= 2*dy
			x += 1	
	#Cas ou l'on se trouve dans l'octant 3
	elif(dx < 0 and dy >= 0 and rapport > 1):
		xA, yA = yA, xA
		xB, yB = yB, xB
		
		dx = xB - xA
		dy = yA - yB
		dec = dx - 2*dy
		x, y = xA, yA
		while x <= xB:
			cng.point(y, x)
			if dec < 0:
				dec += 2*dx
				y -= 1
			dec -= 2*dy
			x += 1	
	#Cas ou l'on se trouve dans l'octant 4
	elif(dx < 0 and dy >= 0 and rapport <= 1):		
		dx = xA - xB
		dy = yB - yA
		dec = dx - 2*dy
		x, y = xA, yA
		while x >= xB:
			cng.point(x, y)
			if dec < 0:
				dec += 2*dx
				y += 1
			dec -= 2*dy
			x -= 1		
	#Cas ou l'on se trouve dans l'octant 5	
	elif(dx < 0 and dy < 0 and rapport <= 1):		
		dx = xA - xB
		dy = yA - yB
		dec = dx - 2*dy
		x, y = xA, yA
		while x >= xB:
			cng.point(x, y)
			if dec < 0:
				dec += 2*dx
				y -= 1
			dec -= 2*dy
			x -= 1	
	#Cas ou l'on se trouve dans l'octant 6
	elif(dx < 0 and dy < 0 and rapport > 1):
		xA, yA = yA, xA
		xB, yB = yB, xB
		
		dx = xA - xB
		dy = yA - yB
		dec = dx - 2*dy
		x, y = xA, yA
		while x >= xB:
			cng.point(y, x)
			if dec < 0:
				dec += 2*dx
				y -= 1
			dec -= 2*dy
			x -= 1
	#Cas ou l'on se trouve dans l'octant 7
	elif(dx >= 0 and dy < 0 and rapport > 1):		
		xA, yA = yA, xA
		xB, yB = yB, xB
		
		dx = xA - xB
		dy = yB - yA
		dec = dx - 2*dy
		x, y = xA, yA
		while x >= xB:
			cng.point(y, x)
			if dec < 0:
				dec += 2*dx
				y += 1
			dec -= 2*dy
			x -= 1	
	#Cas ou l'on se trouve dans l'octant 8
	elif(dx >= 0 and dy < 0 and rapport <= 1):			
		dx = xB - xA
		dy = yA - yB
		dec = dx - 2*dy
		x, y = xA, yA
		while x <= xB:
			cng.point(x, y)
			if dec < 0:
				dec += 2*dx
				y -= 1
			dec -= 2*dy
			x += 1	
	else:
		print("Coordonnée incorect")				


#Effectue un test pour savoir si le dessin fonctionne dans tous les octants
def test_bresenham():
	Bresenham(0.1, 0.1, 8, 1)
	Bresenham(0.1, 0.1, 1, 8)
	Bresenham(-0.1, 0.1, -1, 8)
	Bresenham(-0.1, 0.1, -8, 1)
	Bresenham(-0.1, -0.1, -8, -1)
	Bresenham(-0.1, -0.1, -1, -8)
	Bresenham(0.1, -0.1, 1, -8)
	Bresenham(0.1, -0.1, 8, -1)


#Génère nbSegments aléatoires 		
def random_generation(nbSegments):
	for i in range(nbSegments):
		x1, y1 = random.uniform(xCon1, xCon2), random.uniform(yCon1, yCon2)
		x2, y2 = random.uniform(xCon1, xCon2), random.uniform(yCon1, yCon2)
		Bresenham(x1, y1, x2, y2)
	

if __name__ == "__main__":
	start_time = time.time()
	
	init_fenetre(50, 50, 950, 950)
	init_euclidien_space(-10.0, -10.0, 10.0, 10.0)
	
	#test_bresenham()
	
	random_generation(1000)
	
	origin()

	end_time = (time.time() - start_time)
	print "Time : %s" % (end_time)
	
		
	cng.mainloop()
