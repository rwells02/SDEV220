'''
Author: Rashan Wells
Date: 02/02/2025
Version: 1.0
Program: vehicleSelectionApp.py
'''
class vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType
        
class automobile(vehicle):
    def __init__(self, vehicleType, year, make, model, doorNum, sunRoof):
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doorNum = doorNum
        self.sunRoof = sunRoof
        
    def display(self):
        print(f"Vehicle Type: {self.vehicleType}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doorNum}")
        print(f"Roof type: {self.sunRoof}")

def main():
    print("Vehicle Information Application")
    vehicleType = "car"
    
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doorNum = input("Enter the number of doors on the car (2 or 4): ")
    sunRoof = input("Enter the type of roof (solid or sun roof) the car has: ")
    
    car = automobile(vehicleType, year, make, model, doorNum, sunRoof)
    car.display()
    
if __name__ == "__main__":
    main()
