answers = []

def check_real(table, check):
    f = True
    for i in table:
        if i[0] == check[0]:  # or (i[1] == check[1]):
            f = False
            break
        if (i[0] + i[1] == check[0] + check[1]) or (i[0] - i[1] == check[0] - check[1]):
            f = False
            break
    return f


def return_variants(table,  row):
    if row == 8:
        answers.append(table)
        return
    for i in range(8):
        tab = table.copy()
        if check_real(tab, [i, row]):
            tab.append([i, row])
            return_variants(tab, row + 1)


return_variants([], 0)
print("Всего вариантов:",  len(answers))
for i in answers:
    print(*i)
