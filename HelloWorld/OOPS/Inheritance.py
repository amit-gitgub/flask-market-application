class Person:
    def __init__(self, name, married):
        self.name = name
        self.married = married

    def isemployee(self):

        return False


class Employee(Person):
    def __init__(self, name, married, dept, id):
        self.dept = dept
        self.id = id
        Person.__init__(self, name, married)

    def display(self):
        return self.name, self.dept, self.married, self.id




emp = Employee("amit", "married", "computer", 100)

print(emp.display())








