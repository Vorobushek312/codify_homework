# Voronov Andrei
# Условие программы:
# В магазине есть список разных продуктов, у каждого продукта есть название, цена, уникальный номер. 
# Сперва пользователю нужно отобразить весь список продуктов с их информацией, после нужно сказать чтобы он ввел название товара, 
# если такой товар есть предложить пользователю купить этот товар, и ввести сумму если введенная сумма меньше цены которая указана 
# на товар то нужно уведомить его что у вас не хватает денег чтобы купить, иначе сказать ему что вы получили товар.
from prettytable import PrettyTable
x = PrettyTable()
shop = [
    {'product' : 'marijuana', 'price': 250, 'number': 228},
    {'product' : 'hash', 'price': 100, 'number': 229},
    {'product' : 'cocain', 'price': 400, 'number': 230},
    {'product' : 'spices', 'price': 50, 'number': 231},
    {'product' : 'tobacco', 'price': 120, 'number': 232},
]
x.field_names = ["№", "Название", "Цена"]
for products in shop:
    x.add_row([products['number'], products['product'], products['price']])
print('Имеюшийся товар в магазите')
print(x)
name = input('Введите название товара который хотите приобрести >>> ')
if name not in [x['product'] for x in shop]:
    print('error')
else:
    for i in shop:
        if name == i['product']:
            cash = int(input('Вы можете купить этот товар. Введите ссумму для покупки >>> '))
            if i['price'] <= cash:
                print('Получите свой товар, сдача равна', cash - i['price'])
            else:
                print('У вас недостаточно средств для покупки товара.')
                