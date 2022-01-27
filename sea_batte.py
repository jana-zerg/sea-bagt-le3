#тип данных точка

class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other and self.y == other

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'

#собственные исключения

class BoardException (Exception):
    pass

class BoardOutException (BoardException):
    def __str__(self):
        return "Вы стреляете мимо доски!"

class BoardUserException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException (BoardException):
    pass

#кораблики
# bow - координаты носа
# deck - размер корабля или длина (deck-палуба), o - ориентация

class Ship:
    def __init__(self, bow, deck, o):
        self.bow = bow
        self.size = deck
        self.o = o
        self.lives = deck

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.d):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0: #горизонталь
                cur_x += i

            elif self.o == 1: #вертикаль
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooting(self, shot):
        return shot in self.dots

# поле игры

class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["O"] * size for _ in range(size)]

        self.busy = []
        self.ships = [] #список кораблей доски

# вид поля
    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate (self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

# выстрел за границу поля

    def out(self, d):
        return not ((0 <= d.x <= self.size) and (0 <= d.y <= self.size))