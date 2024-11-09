def persona(N):
    res = 0
    fail = 0
    for i in N:
        try:
            res += i
        except TypeError:
            fail += 1
            print(f'Incorrect type - {i}')
    return res, fail

def calc(N):
    try:
        aver = persona(N)
        return aver[0]/(len(N)-aver[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'In -N- Incorrect type')

print(f'Результат 1: {calc("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calc([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calc(567)}') # Передана не коллекция
print(f'Результат 4: {calc([42, 15, 36, 13])}') # Всё должно работать
