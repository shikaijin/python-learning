# Car Class
# Zoe Jin

from Vehicle import Vehicle

class Car(Vehicle):
    def _init_(self):
        self.no_of_seats = no_of_seats
        super(Car,self)._init_()

# Unique Method
    def PassengerCapacity(self):
        pc = self.no_of_seats - 1
        return pc

# Overriden method
    def Detail(self):
        detail = "make:"+ self.make +",year:"+ str(self.year) + ",price:"+ str(self.price) + ",seats:"+ str(self.no_of_seats)
        return detail
