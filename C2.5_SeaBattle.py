# class Exeptions:  # класс исключений
#     # def __init__(self, ship, board, shot, contour, twice_shot):
#     #     self.ship = ship
#     #     self.board = board
#     #     self.shot = shot
#     #     self.contour = contour
#     #     self.twice_shot = twice_shot
#
#     def is_shot_in_board(self, shot, board):  # точка выстрела проверяется, соответствует ли списку точек доски
#         if shot not in board:
#             raise ValueError()
#
#     def is_ship_in_board(self, ship_dots, board):  # точки корабля проверяются, соответствуют ли списку точек доски
#         for i in ship_dots:
#             if i not in board:
#                 raise ValueError()
#
#     def is_ship_out_contour(self, ship_dots, contour):  # точки корабля проверяются, соответствуют ли списку точек контуров
#         for i in ship_dots:
#             if i not in contour:
#                 raise ValueError()
#
#     def is_twice_shot(self, shot, shot_list):  # этот метод будет проверять, не произведен ли выстрел в точку, куда уже стреляли
#         None


class Dot:  # класс точек
    type = 'dot'
    empty_dot = "O"
    ship_dot = "■"
    destroyed_ship_dot = "X"
    missed_dot = "T"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # метод сравнения, возможно пригодится в дальнейшем
        return self.x == other.x and self.y == other.y


class Ship:  # класс корабля
    def __init__(self, size, x, y, direction, ship_dots=None):
        self.size = size
        self.x = x
        self.y = y
        self.direction = direction
        self.hp = size
        self.ship_dots = ship_dots
        self.ship_contour = []

    def dots(self):  # метод формирует список с точками корабля (класса Dot)
        self.ship_dots = []  # чтобы избежать накопления точек в списке, перед формированием точек каждого корабля список "обнуляется"
        if self.direction == 0:  # если корабль горизонтальный
            for i in range(self.size):
                self.ship_dots = self.ship_dots + [Dot(self.x - 1, self.y + i - 1)]
        else:  # если корабль вертикальный
            for i in range(self.size):
                self.ship_dots = self.ship_dots + [Dot(self.x + i - 1, self.y - 1)]
        return self.ship_dots

    def contour(self, ship_dots):  # метод формирует контур корабля (список класса Dot)
        for i in ship_dots:  # обводим корабль контуром в виде списка точек
            for a in range((i.x - 1), (i.x + 2)):
                for b in range(i.y - 1, i.y + 2):
                    if Dot(a, b) not in self.ship_contour and Dot(a, b) not in ship_dots and 0<=a<6 and 0<=b<6 :  # избегаем дублирования точек "контура"
                        self.ship_contour = self.ship_contour + [Dot(a, b)]  # формируем список точек "контура", куда корабли ставить нельзя
        return self.ship_contour

    def hit_points(self):  # метод будет считать уменьшение здоровья корабля при попадании
        self.hp = self.hp - 1
        return self.hp


class Board:  # класс игровой доски
    def __init__(self, board=None, ships=[], hid=False, live_ships=None):
        self.board = [[Dot.empty_dot] * 6 for _ in range(6)]
        self.ships = ships
        self.hid = hid
        self.live_ships = 7

    def generate_board(self):  # метод вывода доски (с красивой графикой)
        if self.hid == False:
            for i in range(7):
                if i == 0:
                    i = " "
                print(i, end=" | ")
            print()
            for i in range(6):
                for j in range(6):
                    if j == 0:
                        print(i + 1, "|", self.board[i][j], end=" | ")
                    else:
                        print(self.board[i][j], end=" | ")
                print()
        print(f"\n{self.live_ships} кораблей в строю")  # показываем игроку, сколько у него живых кораблей осталось

    def add_ship(self, ship_dots, ship_contour):  # метод добавления корабля на игровую доску
        self.ships = self.ships + [ship_dots]  # дополняем список кораблей списком точек очередного корабля
        for i in ship_dots:  # ставим корабль на доску
            self.board[i.x][i.y] = i.ship_dot
        for i in ship_contour:  # ставим корабль на доску
            self.board[i.x][i.y] = i.destroyed_ship_dot
        return self.board, self.ships



b = Board()
s = Ship(3, int(input('x')), int(input('y')), int(input('направление')))
b.add_ship(s.dots(), s.contour(s.dots()))
b.generate_board()
print(b.ships)
