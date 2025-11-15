class MobileDevice:
    def __init__(self, model, os, version, has_flash, price, screen_width, screen_height):
        self.model = model
        self.os = os
        self.version = version
        self.has_flash = has_flash
        self.price = price
        self.screen_width = screen_width
        self.screen_height = screen_height
        if screen_width < 0:
            print("Screen width is a negative number")
        if screen_height < 0:
            print("Screen height is a negative number")

    def print_parameters(self):
        print('Model is: ' + self.model + ', Operating System is: ' + self.os + ', Version is: ' + str(self.version) + ', Has Flash ? ' + str(self.has_flash) + ', Price is: ' + str(self.price))

    def calculate_area(self):
        return self.screen_width * self.screen_height

    def picture_quality(self):
        if self.has_flash:
            print('Good Quality')
        else:
            print('Bad Quality')


device1 = MobileDevice('Samsung', 'Android', 8.8, False, 250, 3.5, 6.0)
device1.print_parameters()
print(device1.calculate_area())
device1.picture_quality()

device2 = MobileDevice('Apple', 'IOS', 10.3, True, 3100, 4.0, 7.0)
device2.print_parameters()
print(device2.calculate_area())
device2.picture_quality()
