# Truck Class
# Zoe Jin

from Vehicle import Vehicle

class Truck(Vehicle):
    def _init_(self):
        self.no_of_trailers = no_of_trailers
        super(Truck,self)._init_()
        

# Unique Method
    def ContainerCapacity(self):
        cc = self.no_of_trailers + 1
        return cc

# Overriden method
    def Detail(self):
       detail = "make:"+ self.make +",year:"+ str(self.year) + ",price:"+ str(self.price) + ",trailers:"+ str(self.no_of_trailers)
       return detail
