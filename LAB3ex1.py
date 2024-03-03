class CoffeeMachine:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4'}
        self.initial_state = 'q0'
        self.final_state = 'q4'
        self.current_state = self.initial_state

        self.transition_function = {
            ('q0', 'C'): 'q1',
            ('q0', 'T'): 'q2',
            ('q0', 'A'): 'q3',
            ('q0', 'H'): 'q4',
            ('q0', 'OK'): 'q0',
            ('q1', 'OK'): 'q4',
            ('q2', 'OK'): 'q4',
            ('q3', 'OK'): 'q4',
            ('q4', 'OK'): 'q0'
        }

    def process_input(self, input_char):
        if (self.current_state, input_char) in self.transition_function:
            self.current_state = self.transition_function[(self.current_state, input_char)]

    def is_final(self):
        return self.current_state == self.final_state


def main():
    coffee_machine = CoffeeMachine()
    while True:
        print("Alegeți o băutură: C - cafea, T - ceai, A - cappuccino, H - ciocolată caldă, OK - confirmare")
        user_input = input("Introduceți opțiunea dvs.: ").strip().upper()
        if user_input in {'C', 'T', 'A', 'H', 'OK'}:
            coffee_machine.process_input(user_input)
            if coffee_machine.is_final():
                print("Comanda finalizată. Vă mulțumim!")
                break
        else:
            print("Opțiune invalidă. Vă rugăm să selectați una dintre opțiunile valide.")


if __name__ == "__main__":
    main()
