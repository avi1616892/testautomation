#inheritance

class Banay:
    def sing(self):
        print("I am singer")

class Yossi(Banay):
    def play(self):
        print("I am player")

class Yubal(Yossi):
    def band(self):
        print("I am in band")

class Gavri(Banay):
    def comedian(self):
        print("I am comedian")

yossi=Yossi()
yossi.sing()
yossi.play()

yuval=Yubal()
yuval.band()
yuval.play()
yuval.sing()

gavri=Gavri()
gavri.sing()
gavri.comedian()