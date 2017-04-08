import cng
import exo1
import bresenham

# definition d'une classe point 
class point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	





def dumbLine(pointA, pointB, nbPoints):
	cng.init_window('Exercice2', 800, 600, 'white')
	
	pente = (pointB.y - pointA.y) / float(pointB.x - pointA.x)
	pas = (pointB.x - pointA.x) / float(nbPoints)
	currentX = pointA.x
	currentY = pointA.y
	while currentX < pointB.x :
		exo1.grosPoint(currentX, currentY + pente * currentX)
		currentX += pas
	




if __name__ == "__main__" :
	
	cng.init_window('Exercice2', 800,600, 'white')
	
	bresenham.generic(0,0, 50, 350)
	
	#A = point(0,0)
	#B = point(600,750)
	#dumbLine(A,B,200)
	
	cng.main_loop()
