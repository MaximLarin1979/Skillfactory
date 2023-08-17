
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
                self.ship_dots = self.ship_dots + [Dot(self.x - 1, self.y + i - 1)]
        else:
            for i in range(self.size):
                self.ship_dots = self.ship_dots + [Dot(self.x + i - 1, self.y - 1)]
        return self.ship_dots


class Board:
    def __init__(self, board=None, ships = None, hid = False, live_ships = None):
        if board is None:
            board = []
        self.board = [[Dot.empty_dot] * 6 for _ in range(6)]
        self.ships = ships
        self.hid = hid
        self.live_ships = live_ships

    def generate_board(self):
        if self.hid == False:
            for i in range(6):
                for j in range(6):
                    print(self.board[i][j], end="  ")
                print()

    def add_ship(self, ship_dots):
        for i in ship_dots:
            self.board[i.x][i.y] = i.ship_dot
        return self.board

b = Board()
b.generate_board()

ship = Ship(3, int(input('x')), int(input('y')), int(input('направление')))
b.add_ship(ship.dots())
b.generate_board()