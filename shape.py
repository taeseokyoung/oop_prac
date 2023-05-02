# 추상클래스 : 붕어빵의 틀을 위한 틀
class Shape:
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        

    def get_area(self):   
        # print(type(self.radius))
        self.radius / 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):    
        self.length * self.width

# 여기 어렵습니다...ㅠㅠ 
my_circle = Circle(50)
print(my_circle.get_area())