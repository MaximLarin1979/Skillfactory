print("Правила игры:"
      "\n1. Игроки ходят по очереди, сначала игрок Х, потом игрок О"
      "\n2. Игроки вводят координаты двузначным числом, первая цифра - горизонтальная координата, вторая цифра - вертикальная координата, цифры в диапазоне от 1 до 3"
      "\n3. Если введенная координата меньше 1 или больше 3, то присваивается значение соответственно 1 или 3"
      "\n4. Если ячейка, которую задает игрок, уже занята, то получится пропущеный ход, будьте внимательны"
      "\n5. Выигрывает тот, кто первый полностью заполнит линию тремя Х или О по горизонтали, вертикали либо диагонали"
      "\nУдачи!"
      "\n_______________")
my_matrix = [[" ","1","2","3"], ["1"," "," "," "],["2"," "," "," "],["3"," "," "," "]] #начальная матрица (игровое поле)
X_win_condition = False #условие победы игрока с крестиком
O_win_condition = False #условие победы игрока с ноликом
for i in range(4): #вывод начального игрового поля
    for j in range(4):
        print(my_matrix[i][j], end=" ")
    print()
print("_______________")
def coord_input(coord): #функция ввода координат игроками (в виде строки) и трансформация их в 2 координаты - натуральные числа от 1 до 3
    if int(coord[0]) < 1: #проверка диапазона, если введенная координата меньше 1, то приравниваем к 1, если больше 3 то приравниваем к 3
        coord_i = 1
    elif int(coord[0]) > 3:
        coord_i = 3
    else:
        coord_i = int(coord[0])
    if int(coord[1]) < 1:
        coord_j = 1
    elif int(coord[1]) > 3:
        coord_j = 3
    else:
        coord_j = int(coord[1])
    return [coord_i, coord_j]
def winner_check(player): #функция проверки условия победы того или иного игрока
    if my_matrix[1].count(player) == 3 \
    or my_matrix[2].count(player) == 3 \
    or my_matrix[3].count(player) == 3 \
    or my_matrix[1][1] == player and my_matrix[2][2] == player and my_matrix[3][3] == player \
    or my_matrix[1][3] == player and my_matrix[2][2] == player and my_matrix[3][1] == player \
    or my_matrix[1][1] == player and my_matrix[2][1] == player and my_matrix[3][1] == player \
    or my_matrix[1][2] == player and my_matrix[2][2] == player and my_matrix[3][2] == player \
    or my_matrix[1][3] == player and my_matrix[2][3] == player and my_matrix[3][3] == player:
        return True
    else:
        return False
while X_win_condition == False and O_win_condition == False: #цикл действует, пока не выполнится условие победы одного из игроков
    X_coord = input("Игрок X, ваш ход:") #игрок Х вводит координаты
    if my_matrix[coord_input(X_coord)[0]][coord_input(X_coord)[1]] == " ": #проверка, не занята ли данная клетка, если занята - то ничего не произойдет
        my_matrix[coord_input(X_coord)[0]][coord_input(X_coord)[1]] = "X" #если клетка свободна, то её значение заменяется Х
    O_coord = input("Игрок O, ваш ход:") #игрок O вводит координаты
    if my_matrix[coord_input(O_coord)[0]][coord_input(O_coord)[1]]: #проверка, не занята ли данная клетка, если занята - то ничего не произойдет
        my_matrix[coord_input(O_coord)[0]][coord_input(O_coord)[1]] = "O" #если клетка свободна, то её значение заменяется O
    for i in range(4):  # вывод измененного игрового поля
        for j in range(4):
            print(my_matrix[i][j], end=" ")
        print()
    print("_______________")
    X_win_condition = winner_check("X")  # проверка условия победы игрока с крестиком
    O_win_condition = winner_check("O")  # проверка условия победы игрока с ноликом
if X_win_condition: #проверка кто победил, если оба выстроили линию то в любом случае побеждает Х, т.к. ходил первый
    print("ПОБЕДА ИГРОКА Х!")
else:
    print("ПОБЕДА ИГРОКА О!")