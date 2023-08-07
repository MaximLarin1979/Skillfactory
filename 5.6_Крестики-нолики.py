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
while X_win_condition == False and O_win_condition == False: #цикл действует, пока не выполнится условие победы одного из игроков
    X_coord = input("Игрок X, ваш ход:") #игрок Х вводит координаты
    if int(X_coord[0]) < 1: #проверка диапазона, если введенная координата меньше 1, то приравниваем к 1, если больше 3 то приравниваем к 3
        X_coord_i = 1
    elif int(X_coord[0]) > 3:
        X_coord_i = 3
    else:
        X_coord_i = int(X_coord[0])
    if int(X_coord[1]) < 1:
        X_coord_j = 1
    elif int(X_coord[1]) > 3:
        X_coord_j = 3
    else:
        X_coord_j = int(X_coord[1])
    if my_matrix[X_coord_i][X_coord_j] == " ": #проверка, не занята ли данная клетка, если занята - то ничего не произойдет
        my_matrix[X_coord_i][X_coord_j] = "X" #если клетка свободна, то её значение заменяется Х
    O_coord = input("Игрок O, ваш ход:") #игрок O вводит координаты
    if int(O_coord[0]) < 1: #проверка диапазона, если введенная координата меньше 1, то приравниваем к 1, если больше 3 то приравниваем к 3
        O_coord_i = 1
    elif int(O_coord[0]) > 3:
        O_coord_i = 3
    else:
        O_coord_i = int(O_coord[0])
    if int(O_coord[1]) < 1:
        O_coord_j = 1
    elif int(O_coord[1]) > 3:
        O_coord_j = 3
    else:
        O_coord_j = int(O_coord[1])
    if my_matrix[O_coord_i][O_coord_j] == " ": #проверка, не занята ли данная клетка, если занята - то ничего не произойдет
        my_matrix[O_coord_i][O_coord_j] = "O" #если клетка свободна, то её значение заменяется O
    for i in range(4):  # вывод измененного игрового поля
        for j in range(4):
            print(my_matrix[i][j], end=" ")
        print()
    print("_______________")
    X_win_condition = my_matrix[1].count("X") == 3 \
                      or my_matrix[2].count("X") == 3 \
                      or my_matrix[3].count("X") == 3 \
                      or my_matrix[1][1] == "X" and my_matrix[2][2] == "X" and my_matrix[3][3] == "X" \
                      or my_matrix[1][3] == "X" and my_matrix[2][2] == "X" and my_matrix[3][1] == "X" \
                      or my_matrix[1][1] == "X" and my_matrix[2][1] == "X" and my_matrix[3][1] == "X" \
                      or my_matrix[1][2] == "X" and my_matrix[2][2] == "X" and my_matrix[3][2] == "X" \
                      or my_matrix[1][3] == "X" and my_matrix[2][3] == "X" and my_matrix[3][3] == "X"  # проверка условия победы игрока с крестиком
    O_win_condition = my_matrix[1].count("O") == 3 \
                      or my_matrix[2].count("O") == 3 \
                      or my_matrix[3].count("O") == 3 \
                      or my_matrix[1][1] == "O" and my_matrix[2][2] == "O" and my_matrix[3][3] == "O" \
                      or my_matrix[1][3] == "O" and my_matrix[2][2] == "O" and my_matrix[3][1] == "O" \
                      or my_matrix[1][1] == "O" and my_matrix[2][1] == "O" and my_matrix[3][1] == "O" \
                      or my_matrix[1][2] == "O" and my_matrix[2][2] == "O" and my_matrix[3][2] == "O" \
                      or my_matrix[1][3] == "O" and my_matrix[2][3] == "O" and my_matrix[3][3] == "O"  # проверка условия победы игрока с ноликом
if X_win_condition: #проверка кто победил, если оба выстроили линию то в любом случае побеждает Х, т.к. ходил первый
    print("ПОБЕДА ИГРОКА Х!")
else:
    print("ПОБЕДА ИГРОКА О!")