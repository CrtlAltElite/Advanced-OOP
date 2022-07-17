from abc import ABC, abstractmethod

class Duck(ABC):

    def swim(self):
        print("float in pond")

    @abstractmethod
    def display(self):
       pass

class Quackable(ABC):

    def quack():
        print("quack")

class Flyable(ABC):

    def fly():
        print("flap flap flap")



class Mallard(Duck, Quackable, Flyable):
    def display(self):
        print("I am a Mallard")

class RedHead(Duck, Quackable, Flyable):
    def display(self):
        print("I am a Read Headed Duck")

class Rubberduck(Duck, Quackable):
    def quack(self):
        print("Squeak")

    def display(self):
        print("I am a rubber ducky")


class DecoyDuck(Duck):

    def display(self):
        print("I am a decoy")

