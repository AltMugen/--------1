def z2():
    s = input("Введите строку\n")
    i = 0
    k = 0
    K = 0
    g = 0
    while i < len(s)-1:
        if s[i].lower() in "aeuoi":
            g += 1
        if s[i].isupper() == s[i+1].isupper():
            if s[i] == s[i].lower():
                k += 1
            else:
                K += 1
            i += 1
        if i < len(s):
            if s[i].lower() in "aeuoi":
                g += 1
        i += 1
    print(f"Кол во пар  ниж {k}\nКол во пар  вер {K}\nКол во глассных {g}")