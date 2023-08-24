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
        self.ship_dots = []  # чтобы избежать накопления точек в списке,
        # перед формированием точек каждого корабля список "обнуляется"
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
                    if Dot(a, b) not in self.ship_contour and Dot(a, b) not in ship_dots and 0 <= a < 6 and 0 <= b < 6:
                        # избегаем дублирования точек "контура"
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
        if not self.hid:
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

    def add_ship(self, ship_dots, ship_contour, hid):  # метод добавления корабля на игровую доску
        try:
            for i in ship_dots:  # проверяем, не находится ли какая-то из точек корабля в "запретном диапазоне"
                if i in self.ships or i in self.ship_contours or i.x < 0 or i.x > 5 or i.y < 0 or i.y > 5:
                    raise IndexError  # если да, то инициируем ошибку
            self.ships = self.ships + ship_dots  # дополняем список кораблей списком точек очередного корабля
            for i in ship_dots:  # ставим корабль на доску
                self.board[i.x][i.y] = i.ship_dot
            for i in ship_contour:  # добавляем контур корабля в список контуров доски
                self.ship_contours = self.ship_contours + [i]
            self.live_ships = self.live_ships + 1  # добавляем установленный корабль в счетчик "живых кораблей"
            return self.board, self.ships, self.ship_contours, self.live_ships
        except IndexError:
            if hid is False:  # этот параметр для расстановки доски игрока-компьютера, сообщение не выводим
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
        self.ships_sizes = (3, 2, 2, 1, 1, 1, 1)  # список размеров кораблей
        self.ship_names = ('крейсер (3 точки)', "эсминец 1 (2 точки)", "эсминец 2 (2 точки)",
                           "катер 1 (1 точка)", "катер 2 (1 точка)", "катер 3 (1 точка)", "катер 4 (1 точка)")  # список
                            # названий кораблей

    def gen_player_board(self):  # метод устанавливает корабли и формирует игровую доску игрока-человека
        ship_count = 0  # начальное значение счетчика кораблей
        ship_name_count = -1  # начальное значение счетчика названий кораблей
        for ship_size in self.ships_sizes:
            ship_count = ship_count + 1  # счетчик кораблей
            ship_name_count = ship_name_count + 1  # счетчик названий
            while True:
                print("Устанавливаем ", self.ship_names[ship_name_count])
                if ship_size > 1:
                    ship = Ship(ship_size, int(input('Введите координату X')), int(input('Введите координату Y')),
                                int(input('Введите направление')))
                else:  # если корабль из одной точки, направление спрашивать не нужно
                    ship = Ship(ship_size, int(input('Введите координату X')), int(input('Введите координату Y')))
                self.player_board.add_ship(ship.dots(), ship.contour(ship.dots()), False)
                if self.player_board.live_ships == ship_count:
                    self.player_board.generate_board()
                    break
        return self.player_board

    def gen_ai_board(self):  # метод устанавливает корабли и формирует игровую доску игрока-компьютера
        attempt_count = 0  # задаем начальное количество попыток установки корабля
        while self.ai_board.live_ships != 7:  # цикл будет повторяться, пока успешно не установим все 7 кораблей
            ship_count = 0  # начальное значение счетчика кораблей
            for ship_size in self.ships_sizes:
                ship_count = ship_count + 1  # счетчик кораблей
                if attempt_count > 100:  # если неудачных попыток больше 100, цикл прерывается и уходит на while
                    attempt_count = 0  # если уходим на "большой" цикл - счетчик сбрасываем
                    break
                while True:
                    ship = Ship(ship_size, random.randint(1, 6), random.randint(1, 6), random.randint(0, 1))
                    self.ai_board.add_ship(ship.dots(), ship.contour(ship.dots()), True)
                    attempt_count = attempt_count + 1  # счетчик попыток
                    if attempt_count > 100:  # если неудачных попыток больше 100, цикл прерывается и уходит на for,
                        # где тоже прерывается и уходит на while
                        self.ai_board = Board()  # "обнуляем" доску от ранее расставленных кораблей на "неудачной" доске
                        break
                    if self.ai_board.live_ships == ship_count:
                        attempt_count = 0  # если корабль установлен - счетчик сбрасываем
                        break
        self.ai_board.generate_board()
        return self.ai_board


g = Game()
g.gen_player_board()
g.gen_ai_board()
