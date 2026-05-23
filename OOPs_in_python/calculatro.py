class Calculator:
    def __init__(self, a):
        self.a = a   # first number
        self.menu()

    def menu(self):
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        choice = int(input("Enter choice: "))
        self.b = int(input("Enter second number: "))

        if choice == 1:
            self.add()
        elif choice == 2:
            self.sub()
        elif choice == 3:
            self.multiply()
        elif choice == 4:
            self.divide()
        else:
            print("Invalid choice")

    def add(self):
        print("Result:", self.a + self.b)

    def sub(self):
        print("Result:", self.a - self.b)

    def multiply(self):
        print("Result:", self.a * self.b)

    def divide(self):
        if self.b != 0:
            print("Result:", self.a / self.b)
        else:
            print("Cannot divide by zero")


# run continuously
while True:
    c = int(input("Enter first number: "))
    cal = Calculator(c)