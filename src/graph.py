from heapq import heappop, heappush
import math

class Grafo:   
    def __init__(self, grafo):
        self.grafo = grafo
        
    def adyacentes(self, nodo):
        return self.grafo[nodo]
    
    def añadirNodo(self, dato, adyacencias = {}):
        if dato not in self.grafo:
            self.grafo[dato] = adyacencias
            
    def añadirArista(self, origen, destino, peso):
        if origen in self.grafo:
            if (origen, destino, peso) not in self.grafo[origen]:
                self.grafo[origen].append((origen, destino, peso))
                
    def costoAristasArbol(self, arbol):
        suma = 0
        for origen, destino in arbol.items():
            suma += self.grafo[origen][destino[0]]
        return suma
    
    def dijkstra(self, inicio):
        solucion, camino, cola, visitados = {inicio: 0}, {}, [(0, inicio)], set()
        while cola:
            _, u = heappop(cola)
            if u in visitados: continue
            visitados.add(u)
            for v in self.adyacentes(u):
                self.relajacion(u, v, solucion, camino)
                heappush(cola, (solucion[v], v))
        return solucion, camino
                
    def eliminarNodo(self, dato):
        del self.grafo[dato] 
        
    def eliminarArista(self, origen, destino, peso):
        if origen in self.grafo:
            for i in range(len(self.grafo[origen])):
                if self.grafo[origen][i] == (origen, destino, peso):
                    del self.grafo[origen][i]
    
    def encontrarCamino(self, origen, destino, camino = []):
        camino = camino + [origen]
        if origen == destino:
            return camino
        for nodo in self.adyacentes(origen):
            if nodo not in camino:
                nuevoCamino = self.encontrarCamino(nodo, destino, camino)
                if nuevoCamino:
                    return nuevoCamino
                return None
    
    def encontrarCaminos(self, origen, destino, camino = []):
        camino = camino + [origen]
        if origen == destino:
            return camino
        caminos = []
        for nodo in self.adyacentes(origen):
            if nodo not in camino:
                nuevoCamino = self.encontrarCamino(nodo, destino, camino)
                if nuevoCamino:
                    #print(nuevoCamino)
                    caminos.append(caminos)
                    return caminos
                    
    def encontrarCaminoCorto(self, origen, destino, camino = []):
        camino = camino + [origen]
        if origen == destino:
            return camino
        caminoCorto = None
        for nodo in self.adyacentes(origen):
            if nodo not in camino:
                nuevoCamino = self.encontrarCaminoCorto(nodo, destino, camino)
                if nuevoCamino:
                    if not caminoCorto or len(nuevoCamino) < len(caminoCorto):
                        caminoCorto = nuevoCamino
        return caminoCorto
                    
    def encontrarTodosCaminos(self, origen, destino, camino = []):
        camino = camino + [origen]
        if origen == destino:
            return camino
        caminos = []
        for nodo in self.adyacentes(origen):
            if nodo not in camino:
                nuevosCaminos = self.encontrarTodosCaminos(nodo, destino, camino)
                for nc in nuevosCaminos:
                    caminos.append(nc)
        return caminos
    
    def floydWarshall(self):
        pass
    
    def kruskal(self):
        mst = []
        costo = 0
        solucion = {}
        cola = [(0, None, None)]
        for origen, ady in self.grafo.items():
            for destino, peso in ady.items():
                heappush(cola, (peso, origen, destino))
                
        while len(cola) > 0:
            peso, origen, destino = heappop(cola)
            print(peso, origen, destino)
            if origen is None and destino is None:
                continue
            elif len(mst) == 0:
                mst.append((origen, destino))
                costo += peso
                
            t1 = False #Comprobar si el origen y el destino ya están en el conjunto solución
            t2 = False
            for conjunto in mst:
                if origen in conjunto:
                    t1 = True
                if destino in conjunto:
                    if origen in self.grafo[destino].keys():
                        t2 = True
                if t1 and t2:
                    break
            
            if not t1 and not t2:
                mst.append((origen, destino))
                costo += peso
            
        solucion['árbol recubridor'] = mst
        solucion['costo'] = costo
        return solucion
        #return mst
    
    def prim(self, inicio):
        vertices, mst = [], {}
        cola = [(0, None, inicio)]
        while len(cola) > 0:
            print(cola)
            _, origen, destino = heappop(cola)
            if destino in vertices:
                continue
            vertices.append(destino)
            if origen is None:
                pass
            elif origen in mst:
                mst.add(destino)
            else:
                mst[origen] = [destino]
            for ady, peso in self.adyacentes(destino).items():
                heappush(cola, (peso, destino, ady))
        return mst
                    
    def recorridoAnchura(self, nodo):
        cola = []
        marcas = {}
        for k in self.grafo.keys():
            marcas[k] = False
        cola.append(nodo)
        while len(cola) > 0:
            temp = cola.pop(0)
            print(temp, end=" ")
            marcas[temp] = True
            for ady in self.adyacentes(temp):
                if ady not in cola:
                    if not marcas[ady]:
                        cola.append(ady)


    def recorridoProfunidad(self, nodo):
        pila = []
        marcas = {}
        for k in self.grafo.keys():
            marcas[k] = False
        pila.append(nodo)
        while len(pila) > 0:
            temp = pila.pop()
            print(temp, end=" ")
            marcas[temp] = True
            for ady in self.adyacentes(temp):
                if ady not in pila:
                    if not marcas[ady]:
                        pila.append(ady)
                        
    def relajacion(self, u, v, solucion, camino):
        d = solucion.get(u, math.inf) + self.grafo[u][v]
        if d < solucion.get(v, math.inf):
            solucion[v] = d
            camino[v] = u

    def getGrafo(self):
        return self.grafo

     
'''g = {'L': {'B': 5, 'P': 2},
     'P': {'E': 3, 'B': 10, 'L': 2},
     'E': {'P': 3, 'B': 1},
     'B': {'L': 5, 'P': 10, 'E': 1}}

g ={1:{2:1,3:1},
    2:{1:1,4:1},
    3:{1:1},
    4:{2:1,3:1}}


grafo = Grafo(g)
print(grafo.dijkstra(2))
'''