
class Dot:
    type = 'dot'
    empty_dot = "O"
    ship_dot = "◼︎"
    destroyed_ship_dot = "X"
    missed_dot = "T"
    column_dot = "|"

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
                self.ship_dots = self.ship_dots + [Dot(self.x, self.y + i).ship_dot]
        else:
            for i in range(self.size):
                self.ship_dots = self.ship_dots + [Dot(self.x + i, self.y).ship_dot]
        return self.ship_dots


class Board:
    def __init__(self, board=None, ships = None, hid = False, live_ships = None):
        if board is None:
            board = []
        self.board = [[" " * 7] * 13]
        self.ships = ships
        self.hid = hid
        self.live_ships = live_ships

    def empty_board(self):
        for i in range(7): #генерируем нумератор строк
            self.board[i][0] = i
        for j in range(2, 13, 2): #генерируем нумератор столбцов
                self.board[0][j] = i
        for i in range(1, 7): #генерируем разделители ("|")
            for j in range(1, 11, 2):
                print([i], [j])
                self.board[i][j] = Dot.column_dot
        for i in range(7): #генерируем пустые точки
            for j in range(2, 13, 2):
                self.board[i][j] = Dot(i, j).empty_dot
        if self.hid == False:
            for i in range(7):
                for j in range(13):
                    print(self.board[i][j], end=" ")
                print()

    def add_ship(self, ship_dots):
        for i in ship_dots:
            self.board[i] = Dot.ship_dot
        return self.board

b = Board()
b.empty_board()

# for i in range(7):
#     for j in range(13):
#         print(b.board[i][j], end=" ")
#     print()

b.empty_board()

# battleship = Ship(3, int(input('x')), int(input('y')), int(input('направление')))
# print(battleship.dots())
#
#
# b = Board.add_ship(battleship.dots)
#
# for i in range(7):
#     for j in range(13):
#         print(b.board[i][j], end=" ")
