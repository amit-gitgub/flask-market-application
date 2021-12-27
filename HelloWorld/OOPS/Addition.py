class Addition:

    def __init__(self, first, second):
        self.result = None
        self.first = first
        self.second = second

    def calculate(self):
        self.result = int(self.first) + int(self.second)

    def display(self):
        print("First number is " + str(self.first))
        print("Second number is " + str(self.second))
        print("Result is " + str(self.result))


add = Addition(input("Enter first number: "), input("Enter second number: "))
add.calculate()
add.display()
