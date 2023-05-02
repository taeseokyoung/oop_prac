class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    # def accelerate(self, up):
    #     self.speed += up

    # def brake(self, down):
    #     self.speed -= down

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed
    
    # 캡슐화 
    # 메서드로만 작동하여 객체 내부의 중요한 데이터에 접근하지 못하도록, 보다 안전하게 작업할 수 있다.

    # getter
    # def get_speed(self, unit='mph'):
    #     if unit == 'mph':
    #         return self.speed
    #     elif unit == 'kmh':
    #         return round(self.speed * 1.60934, 2)
    #     else:
    #         raise ValueError('Invalid unit')

    def set_speed(self, value):
        # value = int(value) int만을 입력할 수 있도록 가이드 제시해줄수도 있다.
        self.speed=value

my_car = Car('volvo', 'gray')


print(my_car.model)
print(my_car.color)
print(my_car.speed)
my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
# my_car.accelerate(100)
# my_car.brake(50)
print(my_car.get_speed())

# getter setter
my_car.get_speed()
my_car.set_speed(100)
# my_car.speed = 100 보다 위 형태가 안전하다. ('100' 형식이 맞지 않는 것들도 들어갈 수 있다.)