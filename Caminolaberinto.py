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
arbol=Nodo(0,0,[])

def ComenzarArbol(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i][j]=="x":
                raiz.setPos((i,j))
                arbol.setPos((i,j))
                raiz.setSons([arriba(i,j,arbol),abajo(i,j,arbol),izquierda(i,j,arbol),derecha(i,j,arbol)])
                break

def buscar(arbol,pos):
    if arbol.pos==pos:
        return True
    else:
        if arbol.hijos==[]:
            return False
        else:
            return buscarHijos(arbol.hijos,pos)

def buscarHijos(hijos,pos):
    if hijos==[]:
        return False
    else:
        return buscar(hijos[0],pos) or buscarHijos(hijos[1:],pos) 

def buscarValor(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    return buscarHijosValor(arbol.hijos,valor) 


def buscarHijosValor(hijos,valor):
    if hijos==[]:
        return False
    return buscarValor(hijos[0],valor) or buscarHijosValor(hijos[1:],valor)

def abajo(x,y,nodo):
    if(x+1<=len(laberinto)-1 and laberinto[x+1][y]!=1):
        if(buscar(nodo,(x+1,y))!=True):
            print("abajo: "+str(x+1)+","+str(y))
            nodo.appendSon(Nodo(laberinto[x+1][y],(x+1,y),[]))
            return Nodo(laberinto[x+1][y],(x+1,y),[arriba(x+1,y,nodo),abajo(x+1,y,nodo),izquierda(x+1,y,nodo),derecha(x+1,y,nodo)])
        else:
            return None
    else:
        return None

def arriba(x,y,nodo):
    if(x-1>=0 and laberinto[x-1][y]!=1):
        if(buscar(nodo,(x-1,y))!=True):
            print("arriba: "+str(x-1)+","+str(y))
            nodo.appendSon(Nodo(laberinto[x-1][y],(x-1,y),[]))
            return Nodo(laberinto[x-1][y],(x-1,y),[arriba(x-1,y,nodo),abajo(x-1,y,nodo),izquierda(x-1,y,nodo),derecha(x-1,y,nodo)])
        else:
            return None
    else:
        return None

def izquierda(x,y,nodo):
    if(y-1>=0 and laberinto[x][y-1]!=1):
        if(buscar(nodo,(x,y-1))!=True):
            print("izq: "+str(x)+","+str(y-1))
            nodo.appendSon(Nodo(laberinto[x][y-1],(x,y-1),[]))
            return Nodo(laberinto[x][y-1],(x,y-1),[arriba(x,y-1,nodo),abajo(x,y-1,nodo),izquierda(x,y-1,nodo),derecha(x,y-1,nodo)])
        else:
            return None
    else:
        return None

def derecha(x,y,nodo):
    if(y+1<=len(laberinto[x])-1 and laberinto[x][y+1]!=1):
        if(buscar(nodo,(x,y+1))!=True):
            print("abajo: "+str(x)+","+str(y+1))
            nodo.appendSon(Nodo(laberinto[x][y+1],(x,y+1),[]))
            return Nodo(laberinto[x][y+1],(x,y+1),[arriba(x,y+1,nodo),abajo(x,y+1,nodo),izquierda(x,y+1,nodo),derecha(x,y+1,nodo)])
        else:
            return None
    else:
        return None

    
def main():
    print(laberinto)
    ComenzarArbol(laberinto)
    
    if(buscarValor(raiz,"y")==True):
        print("si tiene solucion")
    else:
        print("no tiene solucion")

main()