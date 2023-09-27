class Square:
    def __init__(self, side):
        self.side = side

class SquareFactory:
    @staticmethod
    def create_square(side):
        return Square(side)

sq1 = SquareFactory.create_square(1)
print(sq1.side)