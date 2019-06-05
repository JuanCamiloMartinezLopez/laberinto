import numpy as np

class Nodo:
    def __init__(self,valor,pos,hijos=[]):
        self.valor=valor
        self.pos=pos
        self.hijos=hijos
    
    def appendSon(self,hijo):
        self.hijos.append(hijo)
    
    def setPos(self,pos):
        self.pos=pos
    
    def setSons(self,hijos):
        self.hijos=hijos

def Readtxt():
    return np.array([x.split() for x in open("laberinto.txt").readlines()])

laberinto=Readtxt()
raiz=Nodo(0,0,[])

def ComenzarArbol(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i][j]=='x':
                raiz.setPos((i,j))
                raiz.setSons([arriba(x,y,raiz),abajo(x,y,raiz),izquierda(x,y,raiz),derecha(x,y,raiz)])

def abajo(x,y,nodo):
    if(y+1<len(laberinto) and laberinto[x][y+1]!='1'):
        if(buscar(nodo,(x,y+1))!=True):
            return nodo.appendSon(Nodo(laberinto[x][y+1],(x,y+1),[]))
        else:
            return None
    else:
        return None

def arriba(x,y,nodo):
    

def izquierda(x,y,nodo):

def derecha(x,y,nodo):


    
def main():
    print(Readtxt())
    '''
    matriz = [[1,2],[3,2],[4,5]]
    print(matriz)
    print(len(matriz))
    print(len(matriz[0]))'''


main()