import re 
import json
from graph import Grafo


class Lector:

    def __init__(self,ruta):
        self.Inicio=None
        self.Fin=None
        with open (ruta) as file:
            self.data= json.load(file)

    

    def getInicial(self):
        return self.data['Automata']['inicial']['estado']

    def getAceptacion(self):
        return self.data['Automata']['aceptacion']['estado']

    def leer(self):
        inf=self.data
        estados=inf['Automata']['estados']
        dic={}
        #s of state
        for s in estados:
            
            #print(self.data['Automata']['transiciones'][i])        
            dic[s]=[]
            #print(self.data['Automata']['transiciones'][i])
    
        inicio=self.data['Automata']['inicial']['estado']
        #e of edge
        for e in  dic:
            dic[e]=self.data['Automata']['transiciones'][e]
        #print(dic)
        g= Grafo(dic)
        #print("dijsktra")
        #print( g.dijkstra(inicio))
        #print("inicio",inicio)
        #g.recorridoProfunidad(inicio)
        

    def getGrafo(self):
        inf=self.data
        estados=inf['Automata']['estados']
        dic={}
        #s of state
        for s in estados:
            
            #print(self.data['Automata']['transiciones'][i])        
            dic[s]=[]
            #print(self.data['Automata']['transiciones'][i])
    
        inicio=self.data['Automata']['inicial']['estado']
        #e of edge
        for e in  dic:
            dic[e]=self.data['Automata']['transiciones'][e]
        #print(dic)
        g= Grafo(dic)
        return g.getGrafo()


        
        