info = [[] for i in range(3)]  # изначальное поле
zeros = [[0, 0, 0] for i in range(3)]  # матрица наличия нулей
crosses = [[0, 0, 0] for i in range(3)]  # матрица наличия крестиков
zero_wins = 0
cross_wins = 0
zero_sum = 0  # количество клеток, на которых стоят нули
cross_sum = 0  # количество клеток, на которых стоят крестики
print("Введите конечное поле (0 - нолик, X - крестик, - - пустое поле)")
for i in range(3):
    info[i] = input().split()
for i in range(3):
    for j in range(3):
        zeros[i][j] = (info[i][j] == "0")
        crosses[i][j] = (info[i][j] == "X")
        zero_sum += zeros[i][j]
        cross_sum += crosses[i][j]

for i in range(3):
    if (sum(crosses[i]) == 3) or (crosses[0][i] + crosses[1][i] + crosses[2][i] == 3):
        cross_wins = 1
    if (sum(zeros[i]) == 3) or (zeros[0][i] + zeros[1][i] + zeros[2][i] == 3):
        zero_wins = 1

if (sum([crosses[i][i] for i in range(3)]) == 3) or (sum([crosses[i][2 - i] for i in range(3)]) == 3):
    cross_wins = 1

if (sum([zeros[i][i] for i in range(3)]) == 3) or (sum([zeros[i][2 - i] for i in range(3)]) == 3):
    zero_wins = 1

if (zero_sum > cross_sum) or (cross_sum > zero_sum + 1):
    print("Невозможная ситуация")

elif cross_wins == 0 and zero_wins == 0:
    if zero_sum + cross_sum < 9:
        print("Игра ещё не завершена")
    else:
        print("Ничья")

elif cross_wins == 1 and zero_wins == 1:
    print("Невозможная ситуация")

elif cross_wins == 1:
    print("Крестики победили")

else:
    print("Нолики победили")
