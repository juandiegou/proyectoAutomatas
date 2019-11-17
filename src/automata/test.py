# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:31:06 2019

@author: Simón
"""
class test:


    def solve(candidate, last_candidate = (-500, -500), last_transition = [], candidates = [], trans = [0]):
    #    print(candidate)
    #    print()
    #    input("Press Enter to continue...")
    #    print("variables:", variables_copy)
    #    time.sleep(1)    
        last_candidate = candidate
        if candidate == f:
    #        print("SOLUTION!!!:", candidate)
            return solution
        else:
            for word, transition in transitions.items():
    #            print("transition: ", word)
                if transition != last_transition:
                    if word not in trans:
                        trans.append(word)
    #                    print(restrictions[word], eval(restrictions[word], variables_copy))
                        if eval(restrictions[word], variables_copy):
                            new_candidate = eval_transition(candidate, transition)
    #                        print(new_candidate)
                            if new_candidate is not None:
                                if new_candidate not in candidates:
    #                                print("actual candidate/ new candidate: ", candidate, new_candidate)
    #                                print("solution:", solution)
                                    candidates.append(new_candidate)
                                    solution[candidate].append(new_candidate)
                                    solution[new_candidate] = []
    #                                print("solution:", solution)
                                if candidate != new_candidate:
                                    new_sol = solve(new_candidate, candidate, transition, candidates, trans)
                                    if new_sol is not None:
                                        solution.update(new_sol)
            update_variables(last_candidate) #backtracking
            try:
                trans.pop()
            except:
                pass
            
    def solve2(candidate, last_candidate, last_transition = [], candidates = [], trans = []):
        if candidate == f:
            return solution
        else:
            for word, transition in transitions.items():
                if word not in trans:
                    trans.append(word)
                    if eval(restrictions[word], variables_copy):
                        new_candidate = eval_transition(candidate, transition)
                        if new_candidate == q0:
                            break
                        if new_candidate is not None:
                            if new_candidate not in candidates:
                                candidates.append(new_candidate)
                                solution[candidate].append(new_candidate)
                                solution[new_candidate] = []
                                if last_candidate != new_candidate:
                                    solve2(new_candidate, candidate, word, candidates, trans)
            update_variables(candidate)
            trans.pop()
            
    def get_possible_transitions(state, states, last_transition):
        possible_transitions = {}
        for word, transition in transitions.items():
            if word not in last_transition:
                if eval(restrictions[word], variables_copy):
                        new_state = eval_transition(state, transition)
                        solution[state].append(new_state)
                        if new_state not in states:
                            states.append(new_state)
                            possible_transitions[word] = transition
                        update_variables(state)
        return possible_transitions, states
                        
            
    def solve3(candidate, last_candidate, last_transition = [], candidates = [q0], trans = {}):
        time.sleep(1)
        print(candidate, last_transition)
        print(candidates)
        if candidate == f:
            return
        else:
            trans, candidates = get_possible_transitions(candidate, candidates, last_transition)
            for word, transition in trans.items():
                last_transition.append(word) if len(last_transition) < 2 else last_transition.pop(0)
                new_candidate = eval_transition(candidate, transition)
                if new_candidate in candidates:
                    print(True)
                    continue
                #solution[candidate].append(new_candidate)
                solution[new_candidate] = []
                solve3(new_candidate, candidate, last_transition, candidates, {})
    #            last_transition.pop(0)
            update_variables(candidate)
            
