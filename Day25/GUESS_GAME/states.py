import pandas

class States():
    def __init__(self):
        self.states = pandas.read_csv('./us-states-game-start/50_states.csv')

    def check_state(self,state_name):
        return self.states.state[self.states.state == state_name]