from datetime import datetime as dt

class Person():

    def __init__(self,first_name,last_name,age):
        '''Initialize class with persons attributes'''
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.created_on=dt.now().strftime("%c")
        print(self.first_name,"is alive!!!!")

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        '''Human Readable output'''
        return f'<Person | {self.full_name}>'
    
    def __repr__(self):
        '''machine readable unique output'''
        return f'<Person|{self.last_name} {self.created_on}>'

    def __eq__(self, __o) -> bool:
        return self.age ==__o.age
    
    def __bool__(self):
        return self.age>0

    def __del__(self):
        print("Our person has died") 
    
    def __le__(self,__o):
        return self.age <= __o.age
    
    def __ge__(self,__o):
        return self.age >= __o.age

    def __lt__(self,__o):
        return self.age < __o.age

    def __gt__(self,__o):
        return self.age > __o.age

    def __hash__(self):
        return hash(self.last_name+self.created_on)
    
steve = Person(first_name="Steve", last_name="Nash", age=55)
jenny = Person(first_name="Jenny", last_name="Green", age=35)
lisa = Person(first_name="Lisa", last_name="Kudrow", age=55)
bambam = Person(first_name="BamBam", last_name="Rubble", age=0)

print(steve)
print(steve.full_name)
print(repr(steve))
print(hash(steve))
print(steve==lisa)
print(steve==jenny)
print(lisa==jenny)

print(steve>=lisa)
print(steve>lisa)
print(steve<=lisa)
print(steve<lisa)

print(steve>=jenny)
print(steve>jenny)
print(steve<=jenny)
print(steve<jenny)

print(steve.__dict__)

if steve:
    print('Steve has been born')
else:
    print('steve is not alive yet')


if bambam:
    print('BamBam has been born')
else:
    print('BamBam is not alive yet')
test=[jenny,steve,bambam,lisa]
print(sorted(test, reverse=True))
