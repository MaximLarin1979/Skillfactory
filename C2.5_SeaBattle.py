
class Dot:
    type = 'dot'
    empty_dot = "O"
    ship_dot = "◼︎"
    destroyed_ship_dot = "X"
    missed_dot = "T"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, size, x, y, direction):
        self.size = size
        self.x = x
        self.y = y
        self.direction = direction
        self.hp = size
        self.ship_dots = []

    def dots(self):
        if self.direction == 0:
            for i in range(self.size):
                self.ship_dots = self.ship_dots + [Dot(self.x, self.y + i)]
        else:
            for i in range(self.size):
                self.ship_dots = self.ship_dots + [Dot(self.x + i, self.y)]
        return self.ship_dots


class Board:
    def __init__(self, board=None, ships = None, hid = False, live_ships = None):
        if board is None:
            board = []
        self.board = [[Dot] * 6] * 6
        self.ships = ships
        self.hid = hid
        self.live_ships = live_ships

    def generate_board(self):
        for i in range(6): #генерируем точки
            for j in range(6):
                self.board[i][j] = Dot(i, j).empty_dot
        if self.hid == False:
            for i in range(6):
                for j in range(6):
                    print(self.board[i][j], end="")
                print()

    def add_ship(self, ship_dots):
        for i in ship_dots:
            print(ship_dots[i].x)
        return self.board

b = Board()
print(b.board)
b.generate_board()


ship = Ship(3, int(input('x')), int(input('y')), int(input('направление')))
print(ship.dots())

b.add_ship(ship.dots())



