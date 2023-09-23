bakery = {
    'торт': [['мука', 'сахар', 'яйца'], 100, 500],
    'пирожное': [['мука', 'сахар', 'яйца', 'шоколад'], 50, 200],
    'маффин': [['мука', 'сахар', 'яйца', 'ваниль'], 30, 100]
}
cart = {}

def view_description():
    for product, details in bakery.items():
        print(f'{product} - {details[0]}')

def view_price():
    for product, details in bakery.items():
        print(f'{product} - {details[1]}')

def view_quantity():
    for product, details in bakery.items():
        print(f'{product} - {details[2]}')

def view_all_info():
    for product, details in bakery.items():
        print(f'{product} - {details}')

def add_to_cart():
    product = input('Введите название продукции: ')
    product = product.lower()
    quantity = int(input('Введите количество: '))
    if product in bakery and quantity <= bakery[product][2]:
        if product in cart:
            cart[product] += quantity
        else:
            cart[product] = quantity
        bakery[product][2] -= quantity
        print(f'Товар добавлен в корзину.')
    else:
        print('Такого продукта нет в наличии или недостаточное количество.')

def remove_from_cart():
    product = input('Введите название продукции: ')
    if product in cart:
        quantity = cart[product]
        del cart[product]
        bakery[product][2] += quantity
        print(f'Товар удален из корзины.')
    else:
        print('Такого продукта нет в корзине.')

def checkout():
    total_price = 0
    print('Чек:')
    for product, quantity in cart.items():
        price = bakery[product][1] * (quantity / 100)
        total_price += price
        print(f'{product}: {quantity}гр. - {price}')
    print(f'Общая сумма: {total_price}')
    cart.clear()

def z5():
    while True:
        print('1. Просмотр описания\n2. Просмотр цены\n3. Просмотр количества\n4. Вся информация\n5. Добавить в корзину\n6. Удалить из корзины\n7. Оформить заказ\n8. Выход')
        choice = int(input('Выберите действие: '))
        if choice == 1:
            view_description()
        elif choice == 2:
            view_price()
        elif choice == 3:
            view_quantity()
        elif choice == 4:
            view_all_info()
        elif choice == 5:
            e = 1
            while e:
                add_to_cart()
                e = int(input("Хотите продолжить покупки? 1 для продолжения, 0 для отказа\n"))
        elif choice == 6:
            remove_from_cart()
        elif choice == 7:
            checkout()
        elif choice == 8:
            print('До свидания!')
            break