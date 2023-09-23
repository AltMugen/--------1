def z3():
    lst = list(map(int, input("Введите элементы списка, разделенные пробелами: ").split()))
    sp = sum(i for i in lst if i > 0)
    print(f'Сумма положительных элементов: {sp}')
    if 0 in lst:
        iz = lst.index(0)
        sz = sum(lst[iz:])
        print(f'Сумма элементов после первого нуля: {sz}')
    else:
        print('Сумму посчитать нельзя')
    lst = [i for i in lst if i >= 0]
    print(f'Список без отрицательных элементов: {lst}')