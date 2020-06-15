

class Shape:
    def __init__(self, length):
        self.length = length

    def get_area(self):
        pass


class Triangle(Shape):

    # def __init__(self, length):
    #     super().__init__(length)
    #
    # def get_area(self):
    #     print(3*self.length)
    pass


class Square(Shape):

    def __init__(self, length):
        super().__init__(length)

    def get_area(self):
        print(4 * self.length)


shape = Shape(50)
print(shape.length)

triangle = Triangle(10)
triangle.get_area()

square = Square(10)
square.get_area()