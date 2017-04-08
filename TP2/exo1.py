from os import chdir
import os

#importation du module graphique
import cng

class point:
	def __init__(self,x,y):
		self.x = x
		self.y = y


x1,x2,y1,y2 = None, None, None, None

def grosPoint(x,y) :
	cng.box(x-2,y-2,x+2,y+2)

def initWindow(px1,py1,px2,py2):
	global x1,x2,y1,y2 
	x1, x2, y1, y2 = px1, px2, py1 ,py2
	cng.init_window(pnom='Ecran', pla=800, pha=600, color='white')
	cng.rectangle(x1,y1,x2,y2)
	 
	 
def mooveWindow(x,y):
	
	#cng.clear_screen()
	cng.rectangle(x1 + x, y1 + y, x2 +x, y2 + y)
	  

def displayPoint(px,py, pfx1,pfy1,pfx2,pfy2, pvx1,pvy1,pvx2,pvy2):
	#cng.init_window('Exercice2', 800, 600, 'white')
	#cng.rectangle(pvx1,pvy1,pvx2,pvy2)
	
	Xdc = pvx2 - pvx1
	Ydc = pvy2 - pvy1
	Xwc = pfx2 - pfx1
	Ywc = pfy2 - pfy1
	
	xScreen = px * (Xdc/float(Xwc)) - pfx1 * (Xdc/float(Xwc)) + pvx1
	yScreen = py * (Ydc/float(Ywc)) - pfy1 * (Ydc/float(Ywc)) + pvy1
	
	#print "x = %d et y = %d" % (xScreen, yScreen)
	grosPoint(xScreen,yScreen)


def calculPoint(px,py, pfx1,pfy1,pfx2,pfy2, pvx1,pvy1,pvx2,pvy2):
	
	Xdc = pvx2 - pvx1
	Ydc = pvy2 - pvy1
	Xwc = pfx2 - pfx1
	Ywc = pfy2 - pfy1
	
	xScreen = px * (Xdc/Xwc) - pfx1 * (Xdc/Xwc) + pvx1
	yScreen = py * (Ydc/Ywc) - pfy1 * (Ydc/Ywc) + pvy1
	
	print "x = %d et y = %d" % (xScreen, yScreen)
	
	 
def getLines(nameFile):
	fi = open(nameFile,'r')
	lignes = fi.readlines()
	fi.close
	return lignes
	
def transformPoints(nameFile):
	pointsList = []
	points = getLines(nameFile)
	for filePoint in points:
		splitTab = filePoint.split()
		x = int(splitTab[0])
		y = int(splitTab[1])
		pointsList.append(x)
		pointsList.append(y)
	print(pointsList)
	
	taille = len(pointsList)
	i=0
	while i < taille -1:
		calculPoint(pointsList[i],pointsList[i+1], 2,2,38,56,  30,50,468,743)
		i += 2


# fonction qui calcul le polynome de Horner a partir d'une liste de coef
# et d'une variable
# listCoef : liste des coeficients
# x0 : variable
#	
def Horner(listCoef, x0):
	degre = len(listCoef)-1
	value =0
	i = 0
	while degre >= i :
		value = listCoef[degre] + x0 * value
		#print value
		degre -= 1
	return value

# fonction qui trace uune courbe de Horner
# xmin : debut de l'intervalle
# xmax : fin de l'intervalle
# nbPoints : nombre de points a afficher dans l'intervalle
# listCoef : liste des coeficients du polynome
def courbeHorner(xmin, xmax, nbpoints, listCoef):
	cng.init_window('Exercice2', 800, 600, 'white')
	cng.rectangle(50,50,250,350)
	
	pas = (xmax-xmin)/float(nbpoints)
	currentX = xmin
	while currentX < xmax :
		displayPoint(currentX, Horner(listCoef,currentX+pas),  -4,-6,4,6,  50,50,250,350)
		currentX += pas
	




if __name__ == "__main__" :
	#initWindow(50,50,200,200)
	#mooveWindow(50,100)
	
	#displayPoint(5,3,  2,2,10,8,  50,50,250,350)
	
	#transformPoints('file')
	
	#courbeHorner(-5,5,10000,[0,0,1])
	
	
	
	
	cng.main_loop()
