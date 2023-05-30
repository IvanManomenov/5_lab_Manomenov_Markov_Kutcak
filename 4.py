n = int(input("Введите количество ступенек "))
var = [0 for i in range(n)]
var[0] = 1
for i in range(1, n):
    var[i] += var[i - 1]
    if i > 1:
        var[i] += var[i - 2]
    if i > 2:
        var[i] += var[i - 3]

print("Количество вариантов:", var[-1])
