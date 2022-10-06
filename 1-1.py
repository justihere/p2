import operator

class Rectangle():


    def __init__(self, length, width):
        self.length = length
        self.width = width

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


rec = Rectangle(float(1.0), float(1.0))

if operator.and_(rec.length > 0.0, rec.width < 20.0) :

    print(rec.length)
    print(rec.width)

    rec.Perymetr(rec.length, rec.width)
    rec.Square(rec.length, rec.width)
