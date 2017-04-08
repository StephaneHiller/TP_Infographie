import cng
import bresenham

#Gestion des points
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def drawDumbLine(p1,p2,nbPoints):
	pente = (p2.y-p1.y)/float(p2.x-p1.x)
	pas = (p2.x-p1.x)/float(nbPoints)
	currentX=0
	
	while currentX<p2.x:
		myY = currentX*pente+p1.y
		cng.point(currentX,myY)
		currentX += pas	
	
if __name__ == "__main__":
	print('hi')
	cng.init_window('my_window', 800, 600, 'white')
	bresenham.generic(0,200,100,100)
	bresenham.generic(100,100,200,200)
	bresenham.generic(100,100,200,0)
	bresenham.generic(0,0,100,100)
	bresenham.generic(0,200,100,100)
	bresenham.generic(0,200,100,100)
	bresenham.generic(0,200,100,100)
	bresenham.generic(0,200,100,100)
	#for i in range(500):
		#drawDumbLine(Point(2,2+i),Point(40+i,500), 1000)
	cng.mainloop()
	
