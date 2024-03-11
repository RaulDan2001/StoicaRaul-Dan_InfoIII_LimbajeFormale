class ParkingLot:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces

    def park_car(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            return True
        else:
            return False

    def leave_parking(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1
            return True
        else:
            return False

    def get_available_spaces(self):
        return self.available_spaces


class ParkingAutomaton:
    def __init__(self, total_spaces):
        self.parking_lot = ParkingLot(total_spaces)

    def park_car(self):
        if self.parking_lot.park_car():
            print("Masina a parcat cu succes!")
        else:
            print("Parcarea este plina. Masina nu a putut parca")

    def leave_parking(self):
        if self.parking_lot.leave_parking():
            print("Masina a plecat cu succes!")
        else:
            print("Parcarea e goala. Nu are ce masina sa plece")

    def check_available_spaces(self):
        print(f"Locuri de parcare valabile: {self.parking_lot.get_available_spaces()}")



if __name__ == "__main__":
    parking_automaton = ParkingAutomaton(5)  

    parking_automaton.check_available_spaces()
    parking_automaton.park_car()
    parking_automaton.park_car()
    parking_automaton.check_available_spaces()
    parking_automaton.leave_parking()
    parking_automaton.check_available_spaces()
    parking_automaton.leave_parking()
