import numpy as np

class Nodo:
    def __init__(self,valor,hijos=[]):
        self.valor=valor
        self.hijos=hijos

class pos:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def IdentificarInicio(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i][j]=='x':
                return pos(i,j)

def Posiblecamino(matriz,pos):
    posible=[]
    if pos.x-1>0 and matriz[pos.x-1][pos.y]=='0':
        posible=posible+[pos(pos.x-1,pos.y)]
    if pos.x+1<len(matriz) and matriz[pos.x+1][pos.y]=='0':
        posible[1]=True
    if pos.y-1>0 and matriz[pos.x][pos.y-1]=='0':
        posible[2]=True
    if pos.y+1<len(matriz[pos.x]) and matriz[pos.x][pos.y+1]=='0':
        posible[3]=True
    
    return posible

def GenerarArbol(matriz,arbol,pos):
    if arbol==None:
        for
        arbol=Nodo(pos,hijos[])

    else:
        
            


    
def main():
    matriz = [[1,2],[3,2],[4,5]]
    print(matriz)
    print(len(matriz))
    print(len(matriz[0]))


main()