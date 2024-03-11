class NFA:
    def __init__(self):
        self.states = {'S0', 'S1', 'S2', 'S3'}
        self.alphabet = {'a', 'b'}
        self.transitions = {
            'S0': {'a': {'S2'}, 'b': {'S3'}},
            'S1': {},
            'S2': {'a': {'S2'}, 'b': {'S1', 'S2'}},
            'S3': {'a': {'S1'}, 'b': {'S3'}}
        }
        self.initial_state = 'S0'
        self.accept_states = {'S1'}

    def is_accepted(self, state):
        return state in self.accept_states

    def process_input(self, input_string):
        current_states = {self.initial_state}
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions[state]:
                    next_states.update(self.transitions[state][symbol])
            current_states = next_states
        return any(self.is_accepted(state) for state in current_states)



if __name__ == "__main__":
    nfa = NFA()
    input_strings = ["ab", "aab", "bb", "bba", "a", "b"]
    for string in input_strings:
        if nfa.process_input(string):
            print(f"'{string}' este acceptat de NFA.")
        else:
            print(f"'{string}' nu este acceptat de NFA.")
