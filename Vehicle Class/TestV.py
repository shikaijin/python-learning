# Test
# Zoe Jin

import Car
import Truck
import Motorcycle

# Car Class
c = Car.Car()
c.make = "BMW"
c.year = 2017
c.price = 90000
c.no_of_seats = 4

# Truck Class
t = Truck.Truck()
t.make = "VOLVO"
t.year = 2018
t.price = 190000
t.no_of_trailers = 1

# Motorcycle Class
m = Motorcycle.Motorcycle()
m.make = "YAMAHA"
m.year = 2019
m.price = 10000
m.no_of_trims = 2

# accessing inherited variables
print("Car status:",c.status())
print("Truck status:",t.status())
print("Motocycle status:",m.status())

# accessing inherited methods
print("The car is sold in",c.SoldYear())
print("The truck is sold in",t.SoldYear())
print("The motocycle is sold in",m.SoldYear())

# accessing overridden methods
print("Car details:",c.Detail())
print("Truck details:",t.Detail())
print("Motorcycle details:",m.Detail())


# accessing unique methods
print("PassengerCapacity:",c.PassengerCapacity())
print("ContainerCapacity:",t.ContainerCapacity())
print("WheelNumber:",m.WheelNumber())
