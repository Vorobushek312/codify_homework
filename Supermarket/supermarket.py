# Командная работа, супермаркет. Поставить обработчики на возможные исключения.
# # Пользователь заходит в приложение, вводит количество его денег и выбирает одну из опций:
# # - перейти в раздел
# #     - мясо и молочная продукция
# #     - хлеб и выпечка
# #     - мыломоющие
# #     ... остальные по желанию
# # - выйти из приложения
# # В каждом из разделов, в которых минимум 5 позиций продуктов, пользователь может:
# # 1. Посмотреть весь список товаров.
# # 2. Найти товар по имени (опционально).
# # 3. Добавить товар в корзину (предусмотреть проверку на достаточное количество денег, добавление одного товара несколько раз должно суммировать количество). 
# # 4. Очистить корзину.
# # 5. Посмотреть список продуктов в корзине.
# # 6. Удалить определенный элемент из корзины (опционально).
# # 7. Завершить покупки и пройти на кассу, где клиенту будет производится расчёт и выдаваться сдача(если она есть).
# # Приложение будет состоять из нескольких модулей:
# # - main.py # касса, получение денег от пользователя
# # - milk_meat.py # мясо и молочная продукция
# # - baking.py # хлеб и выпечка
# # - cleaning_materials.py # мыломоющие
from meat import main as meat_main
from soap_detergent import main as soap_detergent_main
from milk import main as milk_main
def enter_shop():
    print('Добро пожаловать в супермаркет Бишкек')
    while True:
        try:
            cash = float(input('Введите количество денег которое у вас есть.'))
            if cash <= 0:
                raise Exception('Сумма денег должна быть положительная!')
        except ValueError:
            print('Вы ввели не число. Введите число!')
        except Exception as s:
            print(s)
        else:
            return cash   
def main():
    money = enter_shop()
    value = None
    while value != 3:
        print("""Опции пользования магазином.
1. Посмотреть список отделов
2. Перейти в отдел.
3. Выйти из преложения""")
        try:
            options = int(input())
            if options not in [1, 2, 3]:
                raise Exception('Токой опции не существует!')
        except ValueError:
            print('Вы должны выбрать номер раздела!')
        except Exception as s:
            print(s)
        else:
            if options == 1:
                print("""
Нумерация отделов
1. Мясо
2. Мыломоющее
3. Молоко
                """)
            elif options == 2:
                while True:
                    try:
                        department = int(input('Укажите номер отдела.'))
                        if department not in [1, 2, 3]:
                            raise Exception('Токой опции не существует!')
                    except ValueError:
                        print('Вы должны выбрать номер раздела!')
                    except Exception as s:
                        print(s)
                    else:
                        break
                if department == 1:
                    products = meat_main(money)
                elif department == 2:
                    products = soap_detergent_main(money)
                elif department == 3:
                    products = milk_main(money)
                money = calc_user_products(products, money)
            if options == 3:
                exit()

    
def calc_user_products(products, money):
    full_price = 0
    if products != None:
        for item in products:
            full_price += item['count'] * item['product']['price']
    money -= full_price
    print(f'Общая стоимость: {full_price} Ваша сдача {money}.')
    return money

main()
