class Car:
    manufacturer = ""
    model=""
    year=0
    price=0.0
    has_abs =False

    def print_details(self):
        print( self.manufacturer+ " "  + self.model + " " +   str(self.year) + " " +   str(self.price) + " "   + str(self.has_abs))

car1 = Car()
car1.manufacturer ="Toyota"
car1.model="Corolla"
car1.year = 2022
car1.price= 85000.25
car1.has_abs = True
car1.print_details()



car2=Car()
car2.manufacturer ="Mazda"
car2.model="Cx5"
car2.year = 2004
car2.price= 35000.55
car2.has_abs = False
car2.print_details()
