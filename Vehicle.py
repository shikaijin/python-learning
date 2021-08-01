# Vehicle Class
# Zoe Jin

class Vehicle:
    def _init_(self,make,year,price):
        self.make = make
        self.year = year
        self.price = price
           
# method cannnot be overriden
    def status(self):
        self.status = "New" 
        return self.status

    def SoldYear(self):
        sy = self.year + 1
        return sy
    
# method can be overriden
    def Detail(self):
        detail = 0 
        return detail
        
        

    
