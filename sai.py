class vehicle:
    def info(self):
        print("This vehicle")

class Car(vehicle):
    def car_info(self, name):
             print("Car name is:", name)

class Truck(vehicle):  
    def truck_info(self, name):
            print("Truck name is:", name)

obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')
