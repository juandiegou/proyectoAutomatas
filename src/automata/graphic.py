# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:31:29 2019

@author: Simón
"""

import graphviz as g

class controller:
    def __init__(self, graph):
        self.graph = graph    
        
    def convert_graph(self):
#        new_graph = {}
#        for node in self.graph:
#            new_node = str(node)
#            new_graph[new_node] = {}
#            for adj in self.graph[node]:
#                value = self.graph[node][adj]
#                new_adj = str(adj)
#                new_graph[new_node].update({new_adj, value})
#        self.graph = new_graph
        new_graph = {}
        for node in self.graph:
            new_node = ''.join(str(node))
            new_graph[new_node] = {}
            for adj in self.graph[node]:    
                new_adj = ''.join(str(adj))
                value = self.graph[node][adj]
                new_graph[new_node].update({new_adj: value})
        self.graph = new_graph
        
    def graph_all(self, q0, f):
        self.convert_graph()
        gr = g.Digraph(format = 'png', directory = 'C:/Users/juand/Desktop/proyecto automatas1/src',strict = True)
        gr.graph_attr['rankdir'] = 'LR'
        gr.node('ini', shape = 'point')
        
        for node in self.graph:
            if node == f:
                gr.node(node, shape = 'doublecircle', color = 'green', size = '1,1')
            if node == q0:
                gr.node(node, color = 'blue')
                gr.edge('ini', node)
            gr.node(node, label = node)
        
        for node in self.graph:
            for adj in self.graph[node]:
                label_name = self.graph[node][adj]
                gr.edge(node, adj, color = 'red', label = label_name)
#                name = 'aista' + node + adj
#                gr.render(view = False, directory = 'D:\Programming\Python\Automata1', cleanup = True, filename = name)
        gr.render(view = False, directory = 'C:/Users/juand/Desktop/proyecto automatas1/src/imgs', cleanup = True, filename = 'Full automata')
        
    def graph_shortest(self, traversal, q0, f):
        print(traversal)
#        self.convert_graph()
        new_graph = {}
        last_node = None
        for step in traversal:
            for node in self.graph:
                if str(step) == node:
                    new_graph[node] = {}
                    if last_node is not None:
                        new_graph[last_node] = {node: self.graph[last_node][node]}
                    last_node = node
                    break
              
        self.graph = new_graph
        self.convert_graph()
        gr = g.Digraph(format = 'png', directory = 'C:/Users/juand/Desktop/proyecto automatas1/src/imgs', strict = True)
        gr.graph_attr['rankdir'] = 'LR'
        gr.node('ini', shape = 'point')
        
        for node in new_graph:
            if node == f:
                gr.node(node, shape = 'doublecircle', color = 'green', size = '1,1')
            if node == q0:
                gr.node(node, color = 'blue')
                gr.edge('ini', node)
            gr.node(node, label = node)
        
        for node in new_graph:
            for adj in new_graph[node]:
                label_name = new_graph[node][adj]
                gr.edge(node, adj, color = 'red', label = label_name)
#                name = 'aista' + node + adj
#                gr.render(view = False, directory = 'D:\Programming\Python\Automata1', cleanup = True, filename = name)
        gr.render(view = False, directory = 'C:/Users/juand/Desktop/proyecto automatas1/src/imgs', cleanup = True, filename = 'Shortest traversal')

    def stepbstep(self, traversal, q0, f):
        #print(traversal)
#       self.convert_graph()
        new_graph = {}
        last_node = None
        for step in traversal:
            for node in self.graph:
                if str(step) == node:
                    new_graph[node] = {}
                    if last_node is not None:
                        new_graph[last_node] = {node: self.graph[last_node][node]}
                    last_node = node
                    break
              
        self.graph = new_graph
        self.convert_graph()
        gr = g.Digraph(format = 'png', directory = 'C:/Users/juand/Desktop/proyecto automatas1/src/imgs', strict = True)
        gr.graph_attr['rankdir'] = 'LR'
        gr.node('ini', shape = 'point')
        
        for node in new_graph:
            if node == f:
                gr.node(node, shape = 'doublecircle', color = 'GREEN', size = '1,1')
            if node == q0:
                gr.node(node, color = 'BLUE')
                gr.edge('ini', node)
            gr.node(node, label = node)
            
        i=0
        for node in new_graph:
            for adj in new_graph[node]:
                label_name = new_graph[node][adj]
                gr.edge(node, adj, color = 'YELLOW', label = label_name)
#               name = 'aista' + node + adj
#                gr.render(view = False, directory = 'D:\Programming\Python\Automata1', cleanup = True, filename = name)
                gr.render(view = False, directory = 'C:/Users/juand/Desktop/proyecto automatas1/src/imgs', cleanup = True, filename = 'img'+str(i))
                i+=1