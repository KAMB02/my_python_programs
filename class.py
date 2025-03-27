

class Car:
    color="rouge"
    state="arret"
    def start(self):
        self.state="marche"
    def  stop(self):
        self.state="arret"


car=Car()
a=car.state
b=car.start()
print(car.state)
       