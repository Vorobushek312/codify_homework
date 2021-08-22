from prettytable import PrettyTable # Импортируем модуль для создания таблиц

def title_show():
    """Создает таблицу с опциями и выводит ее в консоль"""
    title = PrettyTable()
    title.field_names = ['№', 'Название опции']
    title.add_rows(
        [
            ['1', "Посмотреть список отделов."],
            ['2', "Перейти в отдел."],
            ['3', "Выйти из преложения"],
        ]
    )
    return title


def department_show():
    """Отоброжает имеющиеся отделы продуктов"""
    department = PrettyTable()
    department.field_names = ['№', 'Название отдела']
    department.add_rows(
        [
            ['1', "Мясной отдел."],
            ['2', "Отдел мыломоющего."],
            ['3', "Молочный отдел"],
        ]
    )
    return department


def enter_shop():
    """Функция требует ввести обязательно положительное число.
    После возврашает его"""
    print('Добро пожаловать в супермаркет Бишкек')
    while True:
        try:
            cash = float(input('Введите количество денег которое у вас есть: '))
            if cash <= 0:
                raise Exception('Сумма денег должна быть положительная!')
        except ValueError:
            print('Вы ввели не число. Введите число!')
        except Exception as s:
            print(s)
        else:
            return cash


def chec_option():
    """Возврашает номер опции, выбранную пользователем"""
    while True:
        try:
            options = int(input("Введите номер опции: "))
            if options not in [1, 2, 3]:
                raise Exception('Токой опции не существует!')
        except ValueError:
            print('Вы должны выбрать номер раздела!')
        except Exception as s:
            print(s)
        else:
            return options


def chec_inter_departmen():
    """Возврашает номер выброного отдела"""
    while True:
        try:
            department = int(input('Укажите номер отдела: '))
            if department not in [1, 2, 3]:
                raise Exception('Токой опции не существует!')
        except ValueError:
            print('Вы должны выбрать номер раздела!')
        except Exception as s:
            print(s)
        else:
            return department


def calc_user_products(products, money):
    """Производит расчет остатка денежных средств пользователя"""
    full_price = 0
    if products != None:
        for item in products:
            full_price += item['count'] * item['product']['price']
    money -= full_price
    print(f'Общая стоимость: {full_price} Ваша сдача {money}.')
    return money


def table_option_show():
    """Выводит в таблице опции отдела"""
    table_option = PrettyTable() # создаем переменную table с доступом к библиотеки 
    table_option.field_names = ['№', 'Название опции'] # Создание названий столбцов
    table_option.add_rows(
        [
            ['1', "Посмотреть весть список товаров"],
            ['2', 'Найти товар по имени.'],
            ['3', "Добавить товар в корзину"],
            ['4', "Очистить корзину"],
            ['5', 'Посмотреть список продуктов в корзине'],
            ['6', 'Удалить товар из корзины.'],
            ['7', 'Завершить покупку и перейти на кассу']
        ]
    )
    return table_option


def chec_inter_option(table_option_show):
    """Возврашает номер выбранной опции"""
    while True:
        try:
            print(table_option_show)
            option = int(input('Выберите опцию: '))
            if option not in (1,2,3,4,5,6,7):
                raise Exception('Нет токой опции!')
        except ValueError:
            print('Некоретный ввод опции!')
        except Exception as e:
            print(e)
        else:
            return option


def show_products(products):
    """Создает тоблицу с продуктами которые можно купить"""
    x = PrettyTable()
    x.field_names = ["ID", "Название", "Цена"]
    for product in products:
        x.add_row([product['id'], product['name'], product['price']])
    return x


def chek_product(products_indexes):
    """Возврашает номер выбранного продукта"""
    while True:
        try:
            product_index = int(input('Введите id продукта: '))
            if product_index not in products_indexes:
                raise Exception('Такого продукта нет!')
        except ValueError:
            print('Некорретный ввод!')
        except Exception as e:
            print(e)
        else:
            return product_index


def show_bags(products):
    """Создает таблицу с продуктами в корзине"""
    x = PrettyTable()
    x.field_names = ["ID", "Название", "Цена", 'Количество']
    for item_to_buy in products:
        x.add_row([item_to_buy['product']['id'], item_to_buy['product']['name'], item_to_buy['product']['price'], item_to_buy['count']])
    return x

def show_find(find):
    """Создает таблицу с найденными продуктами по поику"""
    x = PrettyTable()
    x.field_names = ["ID", "Название", "Цена"]
    for find_item in find:
        x.add_row([find_item ['id'], find_item ['name'], find_item ['price']])
    return x
