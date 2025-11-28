import random

class Automata:
    def __init__(self):

        # +ve = Include
        # -ve = Exclude
        self.N = 10 # changes the resolution of the automata
        self.state = random.randint(-1,1)
        pass

    def reward(self):
        if self.state < 2 * self.N:
            self.state += 1

    def penalize(self):
        if self.state > 1:
            self.state -= 1


    def output(self):
        return self.state > self.N