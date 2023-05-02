# 슈퍼, 부모 클래스
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("내칭구 울음소리를 들어봐요")

# 서브, 자식 클래스
class Dog(Animal):  
    def __init__(self, name, age, color): 
        super().__init__(name, age)
        self.color = color

    # def speak(self):
    #     print('아우')

class Cat(Animal): 
    def __init__(self, name, age, breed): 
        super().__init__(name, age)
        self.breed= breed
    # 다형성
    # 같은 이름의 메서드를 다른 클래스에서 다르게 구현할 수 있도록 함
    # 가독성, 유지보수성을 높인다.
    def speak(self):
        print('먀아아아앙')


myCat = Cat('들레', 0.9,'스트릿')
myDog = Dog('달구', 11, '흰색')
myCat.speak()
myDog.speak()
