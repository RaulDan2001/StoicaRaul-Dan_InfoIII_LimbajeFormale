class MooreMachine:
    def __init__(self):
        self.current_state = 'S1'

    def transition(self, input):
        if self.current_state == 'S1':
            if input == 'A':
                self.current_state = 'S1'
                return 'O1'
            elif input == 'B':
                self.current_state = 'S2'
                return 'O1'
        elif self.current_state == 'S2':
            if input == 'A':
                self.current_state = 'S1'
                return 'O2'
            elif input == 'B':
                self.current_state = 'S2'
                return 'O2'


machine = MooreMachine()
inputs = ['A', 'B', 'A', 'B', 'A']
for inp in inputs:
    output = machine.transition(inp)
    print(f'Input: {inp}, Output: {output}')

