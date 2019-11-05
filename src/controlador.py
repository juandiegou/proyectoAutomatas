#import networkx as nx

import graphviz as gv
import solucionador



class controlador:


    def __init__(self,grafo):
        self.grafo=grafo
        gr = gv.Digraph(format='png',directory="C:/Users/juand/Desktop",strict=True)
        gr.graph_attr['rankdir'] = 'LR'
        gr.node('ini',shape="point")
        



        for g in grafo:
            print(g,grafo[g])
            if g == 'f':
                gr.node(g, shape="doublecircle",color='blue',size ="1,1")

            if g=='a':
                gr.edge('ini',g)
            gr.node(g,label=g)
        gr.render(view=True,directory="C:/Users/juand/Desktop/proyecto automatas1/src/imgs",cleanup=False,filename="nodes")

        for t in grafo:
            print(t,end=":")
            for y in grafo[t]:
                gr.edge(t,y, label=str(grafo[t][y]),color='red')
                nombre="arista"+t+y
                gr.render(view=False,directory="C:/Users/juand/Desktop/proyecto automatas1/src/imgs",cleanup=False,filename=nombre)




#c= controlador(grafo={'a': {'a': 0, 'c': 1}, 'b': {'b': 0, 'e': 1}, 'c': {'b': 1, 'd': 0}, 'd': {'f': 1, 'e': 0}, 'e': {'f': 1, 'g': 0}, 'f': {'f': 0, 'g': 0}, 'g': {'g': 0, 'd': 1}} )







