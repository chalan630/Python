class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name.title()
    
    def read_odometer(self):
        print(self.odometer_reading)

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

# 继承
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery(40000)                  # 将实例用作属性
    
    """多态"""
    def describe_battery(self):
        print(self.battery_size)

    """Override"""
    def get_descriptive_name(self):
        print("Override method")
    
my_tesla = ElectricCar('tesla', 'model s', 2016)
