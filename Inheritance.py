#Create a base class vehicle with derived class car and bike Show how inheritance works by overriding methods.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def vehicle_info(self):
        return f"Make: {self.make}, Model: {self.model}"
    
    def start(self):
        return "vehicle started"
    
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    #Overriden method
    def start(self):
        return f"{self.make} car started"

class Bike(Vehicle):
    def __init__(self, make, model, type_of_bike):
        super().__init__(make, model)
        self.type_of_bike = type_of_bike
        
    #Overriden method
    def start(self):
        return f"{self.make} bike started"


car = Car("Toyota", "Corolla", 4)
bike = Bike("Honda", "CBR", "Sports")

print(car.start())
print(bike.start())
        
    
    