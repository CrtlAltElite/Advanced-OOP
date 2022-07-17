from abc import ABC, abstractmethod
class Animal(ABC):
    acc = 9.8
    def __init__(self, name, species, legs=4):
        self.name = name
        self.species = species
        self.legs = legs
        self.random = 55
    
    @abstractmethod
    def speak(self):
        print("Some Generic Animal Sound")
    
    @abstractmethod
    def run(self):
        print("Animal Moves")


class Dog(Animal):
    speed = 15
    def __init__(self, is_house_trained, name, species, legs=4):
        super().__init__(name,species, legs)
        self.is_house_trained = is_house_trained
        
    def describe(self):
        print(f'the dog has {self.speed} m/s speed and {self.acc} m/s**2 acceleration ans is a {self.species} \
is housetrained : {self.is_house_trained}')
    
    #method overriding .. this will override the method in the parent class
    def speak(self):
        print("BAARRRRKKKK!!!!!!!")

    def run(self):
        print("gallops on four legs")

nala = Dog(True, 'Nala', 'Black Lab')
nala.describe()
nala.speak()
nala.run()
