# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:36:11 2019

@author: Simón
"""
from automata.graphic import controller
from heapq import heappop, heappush
import json
import time

class automata:

    def __init__(self,ruta):
        self.ruta=ruta
        try:
            with open('src/auto_input.JSON') as file:
                model = json.load(file)

        except Exception as e:
            print(e)

        
        self.variables = {variable: 0 for variable in model['variables'].keys()}
        self.variables_copy = {variable: 0 for variable in model['variables'].keys()}
        self.domain = [dom for _, dom in model['variables'].items()]
        self.transitions = model['transitions']
        self.restrictions = model['restrictions']
        self.q0 = tuple(model['Q0'])
        self.f = tuple(model['F'])
        #            print(f)
        self.state = self.q0
        #solution = {q0: []}
        self.solution = {self.q0: {}}
        
        self.solve4()
        
        self.traversal =self.encontrarCaminoCorto(self.q0, self.f)
        self.graph = controller(self.solution)
        self.graph.graph_all(str(self.q0), str(self.f))
        #graph.graph_shortest(self.traversal, str(self.q0), str(self.f))
        #graph.stepbstep(self.traversal,str(self.q0), str(self.f))



    def genera_paso_a_paso(self):
        self.graph.stepbstep(self.traversal,str(self.q0), str(self.f))

    def genera_camino(self):
        self.graph.graph_shortest(self.traversal, str(self.q0), str(self.f))

    def get_transversal(self):
        return self.traversal

    def get_q0(self):
        return self.q0

    def get_f(self):
        return self.f

    def get_solution(self):
        return self.solution
           

    def update_variables(self,values):
        i = 0
        for var in self.variables:
            self.variables[var] = values[i]
            i+=1
        self.variables_copy.update(self.variables)
        if '__builtins__' in self.variables_copy:
            del(self.variables_copy['__builtins__'])

    def check_state(self,state):
        for i in range(len(state)):
            value = state[i]
    #        print("domain:", state, value, ": ", domain[i][0], domain[i][1])..
            if value < self.domain[i][0] or value > self.domain[i][1]:
                return False
        return True

    def operate_states(self,state1, state2):
        new_state = []
        for i in range(len(state1)):
            if(state1[i] != state2[i]):
                value = state1[i] + state2[i]
                new_state.append(value)
            else:
                value = state1[i]
                new_state.append(value)
        return tuple(new_state)

    def eval_transition(self,state, transition):
        state2 = []
        for element in transition:
            if isinstance(element, int):
                state2.append(element)
            else:
                value = eval(element, self.variables_copy)
    #            print("valor eval: ", value)
                state2.append(value)
        #new_state = operate_states(state, state2)
        if self.check_state(state2):
            self.update_variables(state2)
            return tuple(state2)
        else:
            return None
            
    def solve4(self):
        candidates = []
        pending = []
        pending.append(self.q0)
        candidates.append(self.q0)
        while len(pending) > 0:
            candidate = pending.pop(0)
            self.update_variables(candidate)
            for word, transition in self.transitions.items():
                #print(candidate, candidates)
                #print(eval(restrictions[word], variables_copy))
                if eval(self.restrictions[word], self.variables_copy):
                    new_candidate = self.eval_transition(candidate,  transition)
                    if new_candidate in candidates:
    #                    solution[candidate].append([new_candidate, word])
                        self.solution[candidate].update({new_candidate: word})
                    else:
                        pending.append(new_candidate)
                        candidates.append(new_candidate)
    #                    solution[candidate].append([new_candidate, word])
    #                    solution[new_candidate] = {}
                        self.solution[candidate].update({new_candidate: word})
                        self.solution[new_candidate] = {}
                self.update_variables(candidate)
        return self.solution


    ################ OPERATIONS OVER THE FINAL GRAPH ################
    def adjacencies(self,node):
            return self.solution[node]
        
    def encontrarCaminoCorto(self,origen, destino, camino = []):
            camino = camino + [origen]
            if origen == destino:
                return camino
            caminoCorto = None
            for nodo in self.adjacencies(origen):
                if nodo not in camino:
                    nuevoCamino = self.encontrarCaminoCorto(nodo, destino, camino)
                    if nuevoCamino:
                        if not caminoCorto or len(nuevoCamino) < len(caminoCorto):
                            caminoCorto = nuevoCamino
            return caminoCorto

    #traversal = encontrarCaminoCorto(q0, f)

    #graph = controller(solution)
    #graph.graph_all(str(q0), str(f))
    #graph.graph_shortest(traversal, str(q0), str(f))
