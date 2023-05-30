m, n = map(int, input("Введите размеры матрицы ").split())
mx = [[] for j in range(m)]
for j in range(m):
    mx[j] = list(map(float, input("Введите строку матрицы ").split()))

a = float(input("Введите число, которое нужно найти в матрице "))

l = 0
r = m
mid = (l + r) // 2
while r > l + 1:
    if mx[mid][0] > a:
        r = mid
    else:
        l = mid
    mid = (l + r) // 2
    # print(l, r, mid)

high_row = mid  # наибольший столбец, в котором может быть искомое число

l = 0
r = m
mid = (l + r) // 2
while r > l + 1:
    if mx[mid][n - 1] >= a:
        r = mid
    else:
        l = mid
    mid = (l + r) // 2

low_row = mid  # наименьший столбец, в котором может быть искомое число

l = 0
r = n
mid = (l + r) // 2

delta = 10 ** 9 + 7
ans = [0, 0]
for row in range(low_row, high_row + 1):
    l = 0
    r = n
    mid = (l + r) // 2
    while r > l + 1:
        if mx[row][mid] > a:
            r = mid
        else:
            l = mid
        mid = (l + r) // 2

    col = mid
    if mx[row][col] == a:
        ans = [row, col]
        break
    if abs(mx[row][col] - a) < delta:
        ans = [row, col]
        delta = abs(mx[row][col] - a)

print("Число", mx[ans[0]][ans[1]], "в ячейке" * ans)
