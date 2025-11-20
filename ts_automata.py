class Automata:
    def __init__(self):

        # +ve = Include
        # -ve = Exclude
        self.state = 0
        self.max_state = 10 # changes the resolution of the automata
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
    
    def penalize(self):
        if (self.state or -self.state) is not self.max_state // 2:
            if self.state > 0:
                self.state -= 1
            else:
                self.state += 1
        
        else:
            # the automata is at a max value
            pass

    def output(self):
        if self.state > 0:
            return True
        else:
            return False