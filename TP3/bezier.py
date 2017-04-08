# coding: utf-8

#
# HILLER Stéphane
#
#Programme permettant de dessiner des courbes de Bezier selon deux méthodes, Bernstein et 
#barycentres. 
#


import cng



#définition des variable globale définnisant l'espace euclidien ainsi que la fenètre
global xFen1, yFen1, xFen2, yFen2, xEuc1, yEuc1, xEuc2, yEuc2

#fonction permettant d'initialiser l'écran et la fenetre à l'intérieur de l'écran
def init_window() :
	cng.init_window('Exercice2', 550, 550, 'white')
	global xFen1, yFen1, xFen2, yFen2 
	xFen1, yFen1, xFen2, yFen2 = 50,50, 500,500
	cng.current_color("red");
	cng.rectangle(xFen1, yFen1, xFen2, yFen2)
	cng.current_color("black");
	
#fonction permettant d'initialiser l'espace euclidien
def init_euclidien_space(x1, y1, x2, y2):
	global xEuc1, yEuc1, xEuc2, yEuc2
	xEuc1, yEuc1, xEuc2, yEuc2 = x1, y1, x2, y2

#fonction permettant de calculer !n
def fact(n):
	res = 1
	for i in range(1, n+1):
		res *= i
	return res


#Calcul de B_(n,p) (t) le p eme polynome de Bernstein d'ordre n, en t
def bernstein(n,p,t):
	result = fact(n)/(fact(p)*fact(n-p)) * t**p * (1 - t)**(n - p)
	return result 

#fonction permettant de calculer le point de paramètre u et tableau de points "points"
def calcPoint(u, points):
	res = 0
	for i in range(len(points)):
		res += (bernstein(len(points)-1,i,u) * points[i])
	return res


#fonction permettant de convertir des points de l'espace euclidien vers l'espace ecran
def convertPoint(x ,y):
	global xFen1, yFen1, xFen2, yFen2, xEuc1, yEuc1, xEuc2, yEuc2
	dFx = xFen2-xFen1
	dFy = yFen2-yFen1
	dCx = xEuc2-xEuc1
	dCy = yEuc2-yEuc1
	
	xScreen = int(x*dFx/float(dCx) - xEuc1*dFx/float(dCx) + xFen1)
	yScreen = int(y*dFy/float(dCy) - yEuc1*dFy/float(dCy) + yFen1) 
	
	return (xScreen, yScreen)

#Calculs les points d'interpolations avec les barycentres
def calcRecur(u, points):
	point01 = points[0] * (1 - u) + points[1] * u;
	point11 = points[1] * (1 - u) + points[2] * u;
	point21 = points[2] * (1 - u) + points[3] * u;
	
	point02 = point01 * (1 - u) + point11 * u;
	point12 = point11 * (1 - u) + point21 * u;
	
	res = point02 * (1 - u) + point12 * u;
	
	return res;


#fonction appliquand un test et affiche une courbe de Bézier
def test():
	k = 0
	
	init_euclidien_space(-10.0, -10.0, 10.0, 10.0)
	myXEuc = [-10.0, -10.0, 10.0, 10.0]
	myYEuc = [-10.0, 10.0, 10.0, -10.0]
	myX = []
	myY = []
	
	i = 0
	#converti tous les points qui sont dans l'espace euclidien vers l'espace ecran
	while i < len(myXEuc):
		(X,Y) = convertPoint(myXEuc[i],myYEuc[i])
		myX.append(X)
		myY.append(Y)
		i += 1
	
	print "tableau des X = "
	print myX
	print "tableau des Y = "
	print myY
	
	xCurb = []
	yCurb = []
	
	pas = 0.01
	while k < 1:
		#Avec calcRecur, on utilise la méthode des barycentres
		x = calcRecur(k, myX)
		y = calcRecur(k, myY)
		#Avec calcPoint, on utilise la méthode des polynomes Bernstein
		#   x = calcPoint(k, myX)
		#   y = calcPoint(k, myY)
		xCurb.append(x)
		yCurb.append(y)
		k += pas
		#print("[ %d ; %d ]" % (x,y))
		
	for i in range(len(xCurb)-1):
		cng.line(xCurb[i],yCurb[i],xCurb[i+1],yCurb[i+1])


if __name__ == "__main__" :
	
	init_window()
	
	test()
	
	cng.main_loop()
