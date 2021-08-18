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
import setting
from meat import main as meat_main # Импортируем отдел мяса
from soap_detergent import main as soap_detergent_main # Импортируем отдел мыломойки
from milk import main as milk_main # Импортируем отдел молока  
def main():
    money = setting.enter_shop()
    while True:
        print(setting.title_show())
        options = setting.chec_option()
        if options == 1:
            print(setting.department_show())
        elif options == 2:
            department = setting.chec_inter_departmen()
            if department == 1:
                products = meat_main(money)
            elif department == 2:
                products = soap_detergent_main(money)
            elif department == 3:
                products = milk_main(money)
            money = setting.calc_user_products(products, money)
        elif options == 3:
            exit()
if __name__ == '__main__':
    main()
