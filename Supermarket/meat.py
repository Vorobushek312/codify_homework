import setting
products = (
    {'id': 1, 'name':'баранина 1кг', 'price':320},
    {'id': 2, 'name':'говядина 1кг', 'price':420},
    {'id': 3, 'name':'конина 1кг', 'price':520},
    {'id': 4, 'name':'фарш 1кг', 'price':220},
    {'id': 5, 'name':'свинина 1кг', 'price':520},
)
products_indexes = tuple((x['id']for x in products))
def main(user_money = 0):
    restart = user_money
    print('Добро пожаловать в молочеый отдел!')
    option = None
    shopping_cart = []
    while option != 7:
        option = setting.chec_inter_option(setting.table_option_show())
        if option == 1:
            print(setting.show_products(products))
        elif option == 2:
            find_full = list()
            name_user = input('Введите товар для поиска: ')
            for find in products:
                if name_user.lower() in find['name']:
                    find_full.append(find)
            if find_full == []:
                print('Совподений не найдено')
            else:
                print('Найденные товары')
                print(setting.show_find(find_full))
        elif option == 3:
            product_index = setting.chek_product(products_indexes)
            product = tuple(filter(lambda x : x['id'] == product_index,products))[0]
            if user_money > product['price']:
                user_money -= product['price']
                shopping_cart_product = None
                shopping_cart_product_index = None
                for index, cart_product in enumerate(shopping_cart):
                    if cart_product['product']['id'] == product_index:
                        shopping_cart_product = cart_product
                        shopping_cart_product_index = index
                if not shopping_cart_product:
                    shopping_cart.append({'count':1,'product': product})
                else:
                    shopping_cart_product['count'] = shopping_cart_product['count'] + 1 
                    shopping_cart[shopping_cart_product_index] = shopping_cart_product
            else:
                print('Не достаточно денег для покупки!')
        elif option == 4:
            user_money = restart
            shopping_cart = []
            print('Корзина очищена!')
        elif option == 5:
            if len(shopping_cart) > 0:
                print(setting.show_bags(shopping_cart))
            else:
                print('Корзина пуста!')
        elif option == 6:
            index = 0
            del_prod = setting.chek_product(products_indexes)
            for have_product in shopping_cart:
                if del_prod == have_product['product']['id']:
                    del shopping_cart[index]
                index += 1               
    if len(shopping_cart) > 0:
        return shopping_cart
    else:
        return None


if __name__ == '__main__':
    main(1000)