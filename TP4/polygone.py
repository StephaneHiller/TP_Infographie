# coding: utf-8

import cng


global xFen1, yFen1, xFen2, yFen2, xEuc1, yEuc1, xEuc2, yEuc2

#fonction permettant d'initialiser l'écran et la fenetre à l'intérieur de l'écran
def init_window() :
	cng.init_window('Exercice2', 550, 550, 'white')
	global xFen1, yFen1, xFen2, yFen2 
	xFen1, yFen1, xFen2, yFen2 = 50,50, 500,500
	cng.current_color("red");
	cng.rectangle(xFen1, yFen1, xFen2, yFen2)
	cng.current_color("black");

#fonction permettant de tracer des polygones
def polygon(nbSommets, sommets, color):
	i=0
	for i in range(len(sommets)-1):
		x1, y1 = sommets[i]
		x2, y2 = sommets[(i+1)%len(sommets)]
		cng.line(x1, y1, x2, y2)
		
	
#fonction permettant d'initialiser l'espace euclidien
def init_euclidien_space(x1, y1, x2, y2):
	global xEuc1, yEuc1, xEuc2, yEuc2
	xEuc1, yEuc1, xEuc2, yEuc2 = x1, y1, x2, y2
	
if __name__ == "__main__" :
	
	init_window()
	
	sommets = [ (50,100) , (200,200), (40,250) ]
	polygon(len(sommets),sommets,"red")
	
	cng.main_loop()
