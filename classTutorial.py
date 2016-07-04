people = {}

class Person:
    def setName(self, name):
        self.name = name
        self.hit = 100
        
    def setAge(self, age):
        people[self.name] = [age,self.hit]
    
    def attack(self, power):
        self.hit = people[self.name][1]
        self.hit -= power
        if self.hit <= 0:
            del people[self.name]

one = Person()
one.setName('Eugene')
one.setAge(17)
one.attack(50)

two = Person()
two.setName('Bluetooth')
two.setAge(50)
two.attack(500)
