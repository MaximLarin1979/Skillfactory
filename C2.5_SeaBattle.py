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
import random


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
    def __init__(self, size, x, y, direction=0, ship_dots=None):
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
                    if Dot(a, b) not in self.ship_contour and Dot(a,b) not in ship_dots and 0 <= a < 6 and 0 <= b < 6:  # избегаем дублирования точек "контура"
                        self.ship_contour = self.ship_contour + [
                            Dot(a, b)]  # формируем список точек "контура", куда корабли ставить нельзя
        return self.ship_contour

    def hit_points(self):  # метод будет считать уменьшение здоровья корабля при попадании
        self.hp = self.hp - 1
        return self.hp


class Board:  # класс игровой доски
    def __init__(self, board=None, ships=[], hid=False, live_ships=None):
        self.board = [[Dot.empty_dot] * 6 for _ in range(6)]
        self.ships = ships
        self.hid = hid
        self.live_ships = 0
        self.ship_contours = []

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
        try:
            for i in ship_dots:  # проверяем, не находится ли какая-то из точек корабля в "запретном диапазоне"
                if i in self.ships or i in self.ship_contours or 0 > i.x >= 6 or 0 > i.y >= 6:
                    raise IndexError("Диапазон занят либо некорректен попробуйте еще раз")
            self.ships = self.ships + ship_dots  # дополняем список кораблей списком точек очередного корабля
            for i in ship_dots:  # ставим корабль на доску
                self.board[i.x][i.y] = i.ship_dot
            for i in ship_contour:  # добавляем контур корабля в список контуров доски
                self.ship_contours = self.ship_contours + [i]
            self.live_ships = self.live_ships + 1
            return self.board, self.ships, self.ship_contours, self.live_ships
        except IndexError:
            print("Диапазон занят либо некорректен, попробуйте еще раз")


class Player:
    def __init__(self, player_b=None, ai_b=None):
        self.player_b = player_b
        self.ai_b = ai_b


class Game:
    def __init__(self, player=None, ai=None):
        self.player = player
        self.player_board = Board()
        self.ai = ai
        self.ai_board = Board()

    def gen_player_board(self):
        print("Устанавливаем крейсер (3 точки)")
        while True:
            cruiser = Ship(3, int(input('Введите координату X')), int(input('Введите координату Y')), int(input('Введите направление')))
            self.player_board.add_ship(cruiser.dots(), cruiser.contour(cruiser.dots()))
            if self.player_board.live_ships == 1:
                break
        self.player_board.generate_board()
        print("Устанавливаем эсминец 1 (2 точки)")
        while True:
            destroyer1 = Ship(2, int(input('Введите координату X')), int(input('Введите координату Y')), int(input('Введите направление')))
            self.player_board.add_ship(destroyer1.dots(), destroyer1.contour(destroyer1.dots()))
            if self.player_board.live_ships == 2:
                break
        self.player_board.generate_board()
        print("Устанавливаем эсминец 2 (2 точки)")
        while True:
            destroyer2 = Ship(2, int(input('Введите координату X')), int(input('Введите координату Y')),
                              int(input('Введите направление')))
            self.player_board.add_ship(destroyer2.dots(), destroyer2.contour(destroyer2.dots()))
            if self.player_board.live_ships == 3:
                break
        self.player_board.generate_board()
        print("Устанавливаем катер 1 (1 точка)")
        while True:
            boat1 = Ship(1, int(input('Введите координату X')), int(input('Введите координату Y')))
            self.player_board.add_ship(boat1.dots(), boat1.contour(boat1.dots()))
            if self.player_board.live_ships == 4:
                break
        self.player_board.generate_board()
        print("Устанавливаем катер 2 (1 точка)")
        while True:
            boat2 = Ship(1, int(input('Введите координату X')), int(input('Введите координату Y')))
            self.player_board.add_ship(boat2.dots(), boat2.contour(boat2.dots()))
            if self.player_board.live_ships == 5:
                break
        self.player_board.generate_board()
        print("Устанавливаем катер 3 (1 точка)")
        while True:
            boat3 = Ship(1, int(input('Введите координату X')), int(input('Введите координату Y')))
            self.player_board.add_ship(boat3.dots(), boat3.contour(boat3.dots()))
            if self.player_board.live_ships == 6:
                break
        self.player_board.generate_board()
        print("Устанавливаем катер 4 (1 точка)")
        while True:
            boat4 = Ship(1, int(input('Введите координату X')), int(input('Введите координату Y')))
            self.player_board.add_ship(boat4.dots(), boat4.contour(boat4.dots()))
            if self.player_board.live_ships == 7:
                break
        self.player_board.generate_board()
        print()
        print('Расстановка кораблей успешно завершена')
        return self.player_board

    def gen_ai_board(self):
        while True:
            cruiser = Ship(3, random.randint(0, 6), random.randint(0, 6), random.randint(0, 1))
            self.ai_board.add_ship(cruiser.dots(), cruiser.contour(cruiser.dots()))
            if self.ai_board.live_ships == 1:
                break
        self.ai_board.generate_board()
        while True:
            destroyer1 = Ship(2, random.randint(0, 6), random.randint(0, 6), random.randint(0, 1))
            self.ai_board.add_ship(destroyer1.dots(), destroyer1.contour(destroyer1.dots()))
            if self.ai_board.live_ships == 2:
                break
        self.ai_board.generate_board()
        while True:
            destroyer2 = Ship(2, random.randint(0, 6), random.randint(0, 6), random.randint(0, 1))
            self.ai_board.add_ship(destroyer2.dots(), destroyer2.contour(destroyer2.dots()))
            if self.ai_board.live_ships == 3:
                break
        self.ai_board.generate_board()
        while True:
            boat1 = Ship(1, random.randint(0, 6), random.randint(0, 6))
            self.ai_board.add_ship(boat1.dots(), boat1.contour(boat1.dots()))
            if self.ai_board.live_ships == 4:
                break
        self.ai_board.generate_board()
        while True:
            boat2 = Ship(1, random.randint(0, 6), random.randint(0, 6))
            self.ai_board.add_ship(boat2.dots(), boat2.contour(boat2.dots()))
            if self.ai_board.live_ships == 5:
                break
        self.ai_board.generate_board()
        while True:
            boat3 = Ship(1, random.randint(0, 6), random.randint(0, 6))
            self.ai_board.add_ship(boat3.dots(), boat3.contour(boat3.dots()))
            if self.ai_board.live_ships == 6:
                break
        self.ai_board.generate_board()
        while True:
            boat4 = Ship(1, random.randint(0, 6), random.randint(0, 6))
            self.ai_board.add_ship(boat4.dots(), boat4.contour(boat4.dots()))
            if self.ai_board.live_ships == 7:
                break
        self.ai_board.generate_board()
        print()
        print('Расстановка кораблей успешно завершена')
        return self.ai_board

g = Game()
g.gen_ai_board()

# b = Board()
# s = Ship(3, int(input('x')), int(input('y')), int(input('направление')))
# b.add_ship(s.dots(), s.contour(s.dots()))
# b.generate_board()
# print(b.ships)
# s2 = Ship(3, int(input('x')), int(input('y')), int(input('направление')))
# b.add_ship(s2.dots(), s2.contour(s2.dots()))
# b.generate_board()
# print(b.ships)