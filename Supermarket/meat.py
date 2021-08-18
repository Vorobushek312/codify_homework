products = (
    {'id': 1, 'name':'баранина 1кг', 'price':320},
    {'id': 2, 'name':'говядина 1кг', 'price':420},
    {'id': 3, 'name':'конина 1кг', 'price':520},
    {'id': 4, 'name':'фарш 1кг', 'price':220},
    {'id': 5, 'name':'свинина 1кг', 'price':520},
)
products_indexes = tuple((x['id']for x in products))
def main(user_money = 0):
    print('Добро пожаловать в мясной отдел!')
    option = None
    shopping_cart = []
    while option != 5:
        try:
            option = int(input('''
            1. Посмотреть весть список товаров
            2. Добавить товар в корзину 
            3. Очистить корзину 
            4. Посмотреть список продуктов в корзине
            5. Завершить покупку и перейти на кассу 
            Виберите опцию:'''))
            if option not in (1,2,3,4,5):
                raise Exception('Нет токой опции!')
        except ValueError:
            print('Некоретный ввод опции!')
        except Exception as e:
            print(e)
        else:
            if option == 1:
                for product in products:
                    print('*'*30)
                    for parameter in product:
                        print(parameter,':',product[parameter])
            elif option == 2:
                try:
                    product_index = int(input('Введите id продукта:'))
                    if product_index not in products_indexes:
                        raise Exception('Такого продукта нет!')
                except ValueError:
                    print('Некорретный ввод!')
                except Exception as e:
                    print(e)
                else:
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
            elif option == 3:
                shopping_cart = []
                print('Корзина очищена!')
            elif option == 4:
                if len(shopping_cart) > 0:
                    for item_to_buy in shopping_cart:
                        print('*'*30)
                        for product in item_to_buy:
                            print(item_to_buy[product])
                else:
                    print('Корзина пуста!')               
    if len(shopping_cart) > 0:
        return shopping_cart
    else:
        return None


if __name__ == '__main__':
    main(1000)