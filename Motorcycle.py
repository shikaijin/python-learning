# Motorcycle Class
# Zoe Jin

from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def _init_(self):
        self.no_of_trims = no_of_trims
        super(Motorcycle,self)._init_()

# Unique Method
    def WheelNumber(self):
        wn = self.no_of_trims
        return wn

# Overriden method
    def Detail(self):
        detail = "make:"+ self.make +", year:"+ str(self.year) + ", price:"+ str(self.price) + ", trims:"+ str(self.no_of_trims)
        return detail
