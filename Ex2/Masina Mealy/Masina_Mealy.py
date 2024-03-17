class MealyMachine:
    def __init__(self):
        self.current_state = 'Q1'

    def transition(self, input):
        if self.current_state == 'Q1':
            if input == 'X':
                self.current_state = 'Q2'
                return 'O1'
            elif input == 'Y':
                return 'O1'
        elif self.current_state == 'Q2':
            if input == 'X':
                return 'O2'
            elif input == 'Y':
                self.current_state = 'Q2'
                return 'O2'

# Testare
machine = MealyMachine()
inputs = ['X', 'Y', 'X', 'Y', 'X']
for inp in inputs:
    output = machine.transition(inp)
    print(f'Input: {inp}, Output: {output}')

