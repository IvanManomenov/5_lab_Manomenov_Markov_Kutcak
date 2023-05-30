a = list(map(int, input("Введите массив ").split()))
mn = a[0]
mx = a[0]
for i in a:
    if i < mn:
        mn = i
    if i > mx:
        mx = i

nums = [0 for i in range(mx - mn + 1)]

for i in a:
    nums[i - mn] = 1

zer = 0

for i in range(len(nums)):
    if nums[i] == 0:
        zer = i + mn
        break

print("Наименьшее пропущенное число", zer)
