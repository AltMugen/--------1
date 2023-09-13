def z2():
    s = input("Введите строку\n")
    i = 0
    k = 0
    g = 0
    while i<len(s)-1:
        if s[i].isupper()==s[i].isupper():
            k+=1
        if s[i].lower() in "aeuoi":
            g+=1
        i+=1
    print(f"Кол во пар {k}\nКол во глассных {g}")