class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def division(self, x, y):
        if y == 0:
            print("division  by zero error")
            return None
        return x / y

def main():
    calc = Calculator()

    while True:
        # Ask user if they want to quit
        choice = input("Do you want to perform a calculation? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Goodbye guys!")
            break

        try:
            a = int(input("first integer value: "))
            b = int(input("second integer value: "))
        except ValueError:
            print("Invalid input: please enter integers.")
            continue  # back to the top of the loop

        print("sum:      ", calc.add(a, b))
        print("subtract: ", calc.subtract(a, b))
        print("multiply: ", calc.multiply(a, b))
        print("divide:   ", calc.division(a, b))

if __name__ == "__main__":
    main()
