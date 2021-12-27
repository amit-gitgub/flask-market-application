class Person:

    state = "UP"
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f" Hi my name is {self.name}"

    def setaddress(self, address):
        self.address = address
    def getaddress(self):
        return self.address

p = Person("Amit")
print(p.greeting())
p.setaddress("modinagar")
print(p.getaddress())
print(p.state)
print(Person.state)

