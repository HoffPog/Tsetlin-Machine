from ts_automata import Automata
from ts_clause import Clause

class Class:
    def __init__(self):
        self.pos_clauses = []
        self.neg_clauses = []
        self.sum = 0
        pass

    def spawn_class(self):
        claus_count = 10 #adjustable

        for x in range(claus_count // 2):
            self.pos_clauses.append(Clause())

        for x in range(claus_count // 2):
            self.neg_clauses.append(Clause())

    def eval_class(self, data: list, training: bool):

        for claus in self.pos_clauses:
            if claus.eval_clause(data, training):
                self.sum += 1
            else:
                self.sum -= 1

        return self.sum