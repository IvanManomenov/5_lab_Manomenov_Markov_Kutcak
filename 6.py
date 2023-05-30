# y<k> = a * x<k> + (1-a) * y<k-1>
# a - alpha - коэффициент фильтрации (от 0 до 1, так же он может задаваться в процентах)
# x<t> - series[] - исходный ряд
# y<t> - result[] - фильтрованный(сглаженный) ряд
#

def exponential_filter(series, alpha):
    result = [series[0]]

    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n-1])

    return result