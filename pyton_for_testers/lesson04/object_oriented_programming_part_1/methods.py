class Car:
    manufacturer = ""
    model=""
    year=0
    price=0.0
    has_abs =False
    hand= 0
    kms= 0
    type_price={"Toyota":9,"Mazda":8}

    def print_details(self):
        print( self.manufacturer+ " "  + self.model + " " +   str(self.year) + " " +   str(self.price) + " "   + str(self.has_abs))

    def price_estimation(self,country):
        result = ((self.type_price.get(self.manufacturer) +self.year)*100 -
                  (self.hand * 100) -self.kms)
        if country=="Israel":
            return  result
        else:
            return result*0.6



car1 = Car()
car1.manufacturer ="Toyota"
car1.model="Corolla"
car1.year = 2022
car1.price= 134000.25
car1.has_abs = True
car1.hand=1
car1.kms=60000
car1.print_details()
print("Price_estimation is:" , car1.price_estimation("Israel"))



car2=Car()
car2.manufacturer ="Mazda"
car2.model="Cx5"
car2.year = 2014
car2.price= 39000.55
car2.has_abs = False
car2.hand=3
car2.kms=145000
car2.print_details()
print("Price_estimation is:" , car2.price_estimation("Portugal"))

