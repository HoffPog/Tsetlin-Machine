from ts_automata import Automata
from ts_clause import Clause

class Class:
    def __init__(self):
        self.pos_clauses = []
        self.neg_clauses = []
        self.sum = 0
        self.index = -1
        pass

    def spawn_class(self, features: int, s, T, index: int):
        claus_count = 10 #adjustable
        self.index = index

        for x in range(claus_count // 2):
            self.pos_clauses.append(Clause())

        for x in range(claus_count // 2):
            self.neg_clauses.append(Clause())

        for claus in self.pos_clauses:
            claus.spawn_automata(features)
            claus.set_feedback_params(s, T)

        for claus in self.neg_clauses:
            claus.spawn_automata(features)
            claus.set_feedback_params(s, T)

    def eval_class(self, data: list):

        self.sum = 0

        for claus in self.pos_clauses:

            if claus.eval_clause(data):
                self.sum = self.sum + 1

        for claus in self.neg_clauses:

            if claus.eval_clause(data):
                self.sum = self.sum - 1

        #print(self.sum)
        return self.sum
    
    def train_downstream(self, yc: bool):
        #print(self.sum)

        for claus in self.pos_clauses:
            claus.train_claus(yc, self.sum)

        for claus in self.neg_clauses:
            claus.train_claus(yc, self.sum)
