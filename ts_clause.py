from ts_automata import Automata
import numpy as np

class Clause:
    def __init__(self):
        self.automata = []
        self.AT_states = []
        pass

    def spawn_automata(self, features: int):
        
        for x in range(features*2):
            self.automata.append(Automata())

    def eval_automata(self):

        for i,automaton in enumerate(self.automata):
            self.AT_states[i] = automaton.output()

    def eval_clause(self, arr: list):

        #create inverse literals
        lits = np.array(arr)
        inv_lits = np.invert(lits)

        literals = lits.append(inv_lits)

        out_AND = []    

        for literal, state in literals, self.AT_states:
            
            #AT excludes the literal, so be true to let other AT's decide
            if state:
                out_AND.append(True)
            
            #AT didnt exclude, let the literal decide.
            else:
                out_AND.append(literal)

        if all(out_AND):
            return True
        else:
            return False