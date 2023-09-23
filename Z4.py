def z4():
    print('Введите элементы списка\nДля окончания ввода, совершить пустой ввод\n')
    a = int(input())
    li = []
    while True:
        try:
            li.append(a)
            a = int(input())
        except:
            break
    e = 0
    p = 0
    po = 0
    for i in li:
        if e:
            po+=i
        if i == 0:
            e = 1
        if i >0:
            p+=i
    i = 0
    while i < len(li):
        if li[i] < 0:
            li.pop(i)
        else:
            i+=1
    print("Сумма положительных"+str(p)+"\n")
    if not e:
        print("Сумму посчитать нельзя\n")
    else:
        print("Сумма после нуля"+str(po)+"\n")
    print(li + '\n')
