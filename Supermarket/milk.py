import setting
products = [
    {'id':1, 'name':'молоко 3.5%', 'price':43},
    {'id':2, 'name':'сыр 72%', 'price':400},
    {'id':3, 'name':'творог 10%', 'price':70},
    {'id':4, 'name':'йогурт 5.5 %', 'price':35},
    {'id':5, 'name':'кефир 7.5 %', 'price':45}, # Создание списка имеющихся товаров
]
products_indexes = tuple((x['id']for x in products)) # Моздает тюпл в котором храняться все id продуктов
def main(user_money = 0):
    """Запускает работу отдела молочных продуктов"""
    restart = user_money
    print('Добро пожаловать в молочеый отдел!')
    option = None
    shopping_cart = []
    while option != 7:
        option = setting.chec_inter_option(setting.table_option_show()) # Получам информацию что хочет пользователь выбрать
        if option == 1:
            print(setting.show_products(products)) # Печатает таблицу с продуктоми 
        elif option == 2:
            find_full = list()
            name_product = input('Введите товар для поиска: ')
            for find in products:
                if name_product.lower() in find['name']: # Находит совпадение и сохраняет их в листе
                    find_full.append(find)
            if find_full == []:
                print('Совподений не найдено')
            else:
                print('Найденные товары')
                print(setting.show_find(find_full)) # Печетает в таблице найденные продукты
        elif option == 3:
            product_index = setting.chek_product(products_indexes) # Получаем от пользователя какой продукт хочет купить
            product = tuple(filter(lambda x : x['id'] == product_index,products))[0]
            if user_money > product['price']: # Проверка хватает ли денег на покупку
                user_money -= product['price'] # Вычетание денег 
                shopping_cart_product = None
                shopping_cart_product_index = None
                for index, cart_product in enumerate(shopping_cart):
                    if cart_product['product']['id'] == product_index:
                        shopping_cart_product = cart_product
                        shopping_cart_product_index = index
                if not shopping_cart_product:
                    shopping_cart.append({'count':1,'product': product}) # Если продукта нет добовляет счетчик на количество
                else:
                    shopping_cart_product['count'] = shopping_cart_product['count'] + 1 # Если продукт есть добовляет к счетчику 1
                    shopping_cart[shopping_cart_product_index] = shopping_cart_product # Итоговая корзина
            else:
                print('Не достаточно денег для покупки!')
        elif option == 4:
            user_money = restart # Возврашает деньги при обнулении корзины
            shopping_cart = []
            print('Корзина очищена!')
        elif option == 5:
            if len(shopping_cart) > 0:
                print(setting.show_bags(shopping_cart)) # Отоброжает продукты в корзине
            else:
                print('Корзина пуста!')
        elif option == 6:
            index = 0
            del_prod = setting.chek_product(products_indexes) # Получаем номер продукта для удаления
            for have_product in shopping_cart:
                if del_prod == have_product['product']['id']:
                    del shopping_cart[index] # Удаляем продукт который хотим удолить
                index += 1               
    if len(shopping_cart) > 0:
        return shopping_cart
    else:
        return None


if __name__ == '__main__':
    main(1000)