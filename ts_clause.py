from ts_automata import Automata
import numpy as np
import random

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

    def set_feedback_params(self, s, T):

        self.S1 = (random.random() <= (1 // s))
        self.S2 = (random.random() >= (1 // s))

    def type1_feedback(self, cl: bool,literal: bool, automata: Automata):
        if cl:
            if literal:
                if self.S2:
                    automata.reward()
                else:
                    pass
            else:
                if self.S1:
                    automata.penalize()
                else:
                    pass
        else:
            if self.S1:
                automata.penalize()
            else:
                pass

    def type2_feedback(self, cl: bool, literal: bool, automata: Automata):
        if cl:
            if literal:
                pass
            else:
                if automata.output():
                    automata.reward()
                else:
                    pass
        else:
            pass


    def eval_clause(self, arr: list, training: bool):

        #create inverse literals
        lits = np.array(arr)
        inv_lits = np.invert(lits)

        literals = np.append(lits, inv_lits)

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