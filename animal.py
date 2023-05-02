class Animal:
    def __init__(self, name, age, speak):
        self.name = name
        self.age = age
    
    def speak(self, sound):
        self.sound = sound



class Dog(Animal):  
    def __init__(self, name, age): 
        self.name = '달구'
        self.age = 11

    def speak(self):
        self.sound = '멍멍'

class Cat(Animal):   
    name = '들레' 
    age = 0.9
    
    def speak(self):
        self.sound = '먀아아아앙'


print(Dog.name)
print(Cat.age)
print(Cat.speak())
