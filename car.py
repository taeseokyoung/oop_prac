class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def speedUp(self, up):
        self.speed += up

    def brake(self, down):
        self.speed -= down

    def get_speed(self):
        return self.speed


my_car = Car('volvo', 'gray')
print(my_car.model)
print(my_car.color)
print(my_car.speed)
my_car.speedUp(100)
my_car.brake(50)
print(my_car.get_speed())