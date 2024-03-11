class FiniteAutomaton:
    def __init__(self):
        
        self.states = {'A', 'B'}
        self.symbols = {'0', '1'}
        
        self.initial_state = 'A'
        self.final_states = {'A'}
        
        self.transitions = {
            ('A', '0'): 'B',
            ('A', '1'): 'A',
            ('B', '0'): 'A',
            ('B', '1'): 'B'
        }

    def process_input_sequence(self, sequence):
        current_state = self.initial_state
        for symbol in sequence:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                
                raise ValueError(f"Invalid transition for state {current_state} and symbol {symbol}")
        return current_state


if __name__ == "__main__":
    automaton = FiniteAutomaton()
    sequences = ["010", "110", "1001"]
    for sequence in sequences:
        final_state = automaton.process_input_sequence(sequence)
        print(f"For sequence {sequence}, final state is {final_state}")
