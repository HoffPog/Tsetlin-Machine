class Automata:
    def __init__(self):

        # +ve = Include
        # -ve = Exclude
        self.max_state = 100 # changes the resolution of the automata
        self.state = 0
        pass

    def reward(self):
        boundary = self.max_state // 2
        if self.state < boundary:
            self.state += 1

    def penalize(self):
        boundary = self.max_state // 2
        if self.state > -boundary:
            self.state -= 1


    def output(self):
        return self.state > 0