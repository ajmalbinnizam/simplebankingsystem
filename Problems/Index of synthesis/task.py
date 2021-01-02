# n = float(input())
# if n < 2:
#     print("Analytic")
# elif n <= 2 or n <= 3:
#     print("Synthetic")
# elif n > 3:
#     print("Polysynthetic")


class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print("vroom vroom")

my_car = Car("Volkswagen")


my_car.drive()

Car.drive(my_car)