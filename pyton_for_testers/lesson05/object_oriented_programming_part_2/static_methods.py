#static_methods

class Exmpale:
    name="Avi"

    def demo1(self):
        self.name="kuku"
        print("Hello world",self.name)

    @staticmethod
    def demo2():
        # Exmpale.name="kuku"
        print("My name is:",Exmpale.name)


exmpale=Exmpale()
exmpale.demo1()
exmpale.demo2()

