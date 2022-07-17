class Animal():
    acc = 9.8
    def __init__(self, name, species, legs=4):
        self.name = name
        self.species = species
        self.legs = legs
        self.random = 55
        
    def speak(self):
        print("Some Generic Animal Sound")
        
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

class Cat(Animal):
    speed = 12
    
    def __init__(self, is_litter_box_trained, name, species, legs=4):
        super().__init__(name,species, legs)
        self.is_litter_box_trained = is_litter_box_trained
    
    def describe(self):
        print(f'the cat has {self.speed} m/s speed and {self.acc} m/s**2 acceleration ans is a {self.species} \
is housetrained : {self.is_litter_box_trained}')

nala = Dog(True, 'Nala', 'Black Lab')
nala.describe()
nala.speak()
nala.run()

        
zebra = Animal('Zee', 'Zebra')
zebra.speak()
zebra.run()

class Mutt(Dog):
    def __init__(self, second_species, is_house_trained, name, species, legs=4):
        super().__init__( is_house_trained, name, species, legs)
        self.second_species = second_species
        
    def describe(self):
        print(f"the mutt is a mix of {self.species} and {self.second_species}")
        
tippi = Mutt("boxer", True, "Tippi", "Pitbull")
tippi.describe()
tippi.run()
tippi.speak()
