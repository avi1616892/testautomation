class MobileDevice:
    model=""
    os=""
    version=0.0
    has_flash =False
    price=0
    screen_width = 0.0
    screen_height = 0.0

    def print_parameters(self):
        # print(self.model + " " + self.os + " " + str(self.version) + " " + str(self.has_flash) + " " + str(self.price))
        print(f"{self.model} {self.os} {self.version} {self.has_flash} {self.price}")

    def calculate_area(self):
        surface_area = self.screen_width*self.screen_height
        return surface_area

    def picture_quality(self):
        if self.has_flash:
            print("Good Quality")
        else:
            print("Bad Quality")



iphone=MobileDevice()
iphone.model="pro-max"
iphone.os="IOS"
iphone.version=16.6
iphone.has_flash=True
iphone.price=6000
iphone.print_parameters()
iphone.screen_width=5.5
iphone.screen_height=4.5
print(iphone.calculate_area())
print(iphone.picture_quality())



galaxy=MobileDevice()
galaxy.model="s25"
galaxy.os="Android"
galaxy.version=14.6
galaxy.has_flash=False
galaxy.price=5000
galaxy.print_parameters()
galaxy.screen_width=6.5
galaxy.screen_height=3.5
print(galaxy.calculate_area())
print(galaxy.picture_quality())

