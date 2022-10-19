
class Rectangle():


    def __init__(self, length, width):
        self.length = length
        self.width = width

    def setter(self, a, b):
        if (0 < a < 20) and (0 < b < 20):
            self.__lenght = a
            self.__height = b
        else:
            raise ValueError("Values out of range!")

    def getter(self):
        return self.__lenght, self.__height

    def get_lenght(self):
        return  self.length

    def get_width(self):
        self.width = self.width

    def set_lenght(self, Lenght):
        self.length = Lenght

    def set_width(self, Width):
        self.width = Width

    def Perymetr(self, length, width):
        per = (self.length + self.width) * 2
        print('Perymetr = ', per)

    def Square(self, length, width):
        per = self.length * self.width
        print('Square = ', per)


rec = Rectangle(4.3, 3)
rec.Perymetr(rec.length, rec.width)
rec.Square(rec.length, rec.width)

