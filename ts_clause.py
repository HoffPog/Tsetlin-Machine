from ts_automata import Automata
import numpy as np
import random

class Clause:
    def __init__(self):
        self.automata = []
        self.AT_states = []
        self.state = False
        self.active_literal = 0
        self.T = 0
        self.literals = []

        pass

    def spawn_automata(self, features: int):
        
        # create automata and initialize corresponding AT_states entries
        for x in range(features*2):
            self.automata.append(Automata())
            # default AT state True so the clause evaluation lets literals decide
            self.AT_states.append(True)

    def eval_automata(self):

        for i,automaton in enumerate(self.automata):
            self.AT_states[i] = automaton.output()

    def set_feedback_params(self, s, T):

        self.T = T

        # self.S1 = (random.random() <= (1 / s))
        # self.S2 = (random.random() >= (1 / s))

        self.s = s

    def type1_feedback(self, cl: bool, literal: bool, automata: Automata):

        S1 = (random.random() <= (1 / self.s))
        S2 = (random.random() >= (1 / self.s))

        if cl:
            if literal:
                if S2:
                    automata.reward()
                else:
                    pass
            else:
                if S1:
                    automata.penalize()
                else:
                    pass
        else:
            if S1:
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

    def train_claus(self, yc: bool, class_sum: int):
        
        csum_clip = np.clip(class_sum, -self.T, self.T)

        p = (self.T - csum_clip) / (2 * self.T)
        c1 = random.random() <= p
        c2 = random.random() <= p
        #print(f"P: {p} | c1: {c1} | c2: {c2} | yc: {yc} | c_sum: {csum_clip}")
        if yc:
            if c1:
                if self.state:

                    for literal, automata in zip(self.literals, self.automata):
                        self.type1_feedback(self.state, literal, automata)
                
                else:

                    for literal, automata in zip(self.literals, self.automata):
                        self.type2_feedback(self.state, literal, automata)

            else:
                pass

        else:
            if c2:
                if self.state:

                    for literal, automata in zip(self.literals, self.automata):
                        self.type2_feedback(self.state, literal, automata)

                else:

                    for literal, automata in zip(self.literals, self.automata):
                        self.type1_feedback(self.state, literal, automata)



    def eval_clause(self, arr: list):

        #create inverse literals
        lits = np.array(arr)
        inv_lits = np.logical_not(lits, )

        self.literals = np.concatenate((lits, inv_lits))

        out_AND = []

        self.eval_automata()    

        for literal, state in zip(self.literals, self.AT_states):
            # AT doesnt exclude, allow whatever literal
            if state:
                out_AND.append(literal)
            else:
                # AT excluded, be true so others can decide
                out_AND.append(True)

        result = all(out_AND)
        self.state = bool(result)
        # if self.state:
        #     print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        # else:
        #     print("eeeee")
        return result

        # if all(out_AND):
        #     return True
        # else:
        #     return False