import setting # Импортируем модуль с функциями
from meat import main as meat_main # Импортируем отдел мяса
from soap_detergent import main as soap_detergent_main # Импортируем отдел мыломойки
from milk import main as milk_main # Импортируем отдел молока  
def main(): 
    money = setting.enter_shop() # Получение информации о средствах покупателя
    while True:  
        print(setting.title_show()) # Информируем пользователя об опциях
        options = setting.chec_option() # Получение информации куда хочет перейти пользователь
        if options == 1:
            print(setting.department_show()) # Информируем пользователя об опциях в отделах
        elif options == 2:
            department = setting.chec_inter_departmen() # Получение информации куда хочет перейти пользователь
            if department == 1:
                products = meat_main(money) # Начинает работать с отделом мяса
            elif department == 2:
                products = soap_detergent_main(money) # Начинает работать с отделом мыломоющих товаров
            elif department == 3:
                products = milk_main(money) # Начинает работать с отделом молочных продуктов
            money = setting.calc_user_products(products, money) # Расчет остатка денежных средств пользователя
        elif options == 3:
            print(f'Пока. Заберите остаток {money}!')
            exit()
if __name__ == '__main__':
    main()
