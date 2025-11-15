class Rectangle:
    height =0.0
    width=0.0

    def calculation_rectangle(self):
        return self.width*self.height

rectangle1=Rectangle()
rectangle1.height=5.8
rectangle1.width=3.5
print(rectangle1.calculation_rectangle())





class Triangle:
    height = 0.0
    width = 0.0

    def calculation_triangle(self):
        return (self.width * self.height)/2

triangle1=Triangle()
triangle1.height=6.8
triangle1.width=3.8
print(triangle1.calculation_triangle())





class Circle:
    pi = 0.0
    radius = 0.0

    def calculation_circle(self):
        return self.pi * self.radius*self.radius

circle1=Circle()
circle1.pi=3.16
circle1.radius=180
print(circle1.calculation_circle())