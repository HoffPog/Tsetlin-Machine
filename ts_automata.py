class Automata:
    def __init__(self, max_state):

        # +ve = Include
        # -ve = Exclude
        self.state = 0
        self.max_state = max_state # changes the resolution of the automata
        pass

    def reward(self):
        if (self.state or -self.state) is not self.max_state // 2:
            if self.state > 0:
                self.state += 1
            else:
                self.state -= 1
        
        else:
            # the automata is at a max value
            pass
    
    def penalise(self):
        if (self.state or -self.state) is not self.max_state // 2:
            if self.state > 0:
                self.state -= 1
            else:
                self.state += 1
        
        else:
            # the automata is at a max value
            pass