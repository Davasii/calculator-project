# Jose Lopez first project
# Index as Calculator Mark 1


class Calculator:
    def __init__(self):
        self.current_value = 0
    def add(self, number):
        self.current_value += number
        return self.current_value
    def subtract(self, number):
        self.current_value -= number
        return self.current_value
    def multiply(self, number):
        self.current_value *= number
        return self.current_value 
    def divide(self, number):
        if number == 0:
            print("Error: Cannot divide by zero")
            return self.current_value
        self.current_value /= number
        return self.current_value
    def reset(self):
        self.current_value = 0
        return self.current_value


    

if __name__ == "__main__":
    calc = Calculator()  # Create an instance of the Calculator class

    while True:
        print(f"\nCurrent Value: {calc.current_value}")
        print("Choose an Operation")
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
        print("5 - Reset")
        print("6 - Exit")

        choice = input("Enter your choice (1-6): ")
        
        if choice == "6":
            print("Exiting Calculator, Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num = float(input("Enter a number: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            if choice == "1":
                    print(f"Result: {calc.add(num)}")
            elif choice == "2":
                    print(f"Result: {calc.subtract(num)}")
            elif choice == "3":
                    print(f"Result: {calc.multiply(num)}")
            elif choice == "4":
                    print(f"Result: {calc.divide(num)}")


        elif choice == "5":
            print("Calculator reset.")
            calc.reset()
        else:
            print("Invalid choice. Please enter a number between 1-6.")


                


