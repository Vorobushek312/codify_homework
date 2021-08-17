import random
value_random = random.randint(1,10)
print(value_random)
while True:
    try:
        value_user = int(input('Первый уровень! Угадайте число от 1 до 10. У вас есть 1 попытка!>>> '))
        if not 0 < value_user < 11:
            raise Exception('Вам нужно угодать число от 1 до 10')
    except ValueError:
        print('Вам нужно ввести число!')
    except Exception as s:
        print(s)
    else:
        break
if value_random == value_user:
    index = 3
    index_e = 1
    print('Поздравляем вы угадали число!')
    while True:
        try:
            value_user = int(input('Второй уровень! Угадайте число от 1 до 50. У вас есть 3 попытки! >>> '))
            if not 0 < value_user < 51:
                raise Exception('Вам нужно угодать число от 1 до 50')
        except ValueError:
            print('Вам нужно ввести число!')
        except Exception as s:
            print(s)
        else:
            break
    value_random = random.randint(1,50)
    print(value_random)
    while index != index_e:
        index_e += 1
        if value_user != value_random:
            while True:
                try:
                    value_user = int(input('Попробуйте еще раз. >>> '))
                    if not 0 < value_user < 51:
                        raise Exception('Вам нужно угодать число от 1 до 50')
                except ValueError:
                    print('Вам нужно ввести число!')
                except Exception as s:
                    print(s)
                else:
                    break
        elif value_user == value_random:
            print('Поздравляем вы угадали число!')
            index_2 = 3
            while True:
                try:
                    value_user = int(input('Третий уровень! Угадайте число от 1 до 100. У вас есть 4 попытки! >>> '))
                    if not 0 < value_user < 101:
                        raise Exception('Вам нужно угодать число от 1 до 100')
                except ValueError:
                    print('Вам нужно ввести число!')
                except Exception as s:
                    print(s)
                else:
                    break
            value_random = random.randint(1,100)
            print(value_random)
            while index_2 !=0:
                index_2 -= 1
                if value_user != value_random:
                    while True:
                        try:
                            value_user = int(input('Попробуйте еще раз. >>> '))
                            if not 0 < value_user < 101:
                                raise Exception('Вам нужно угодать число от 1 до 100')
                        except ValueError:
                            print('Вам нужно ввести число!')
                        except Exception as s:
                            print(s)
                        else:
                            break
                elif value_user == value_random:
                    print('Поздравляем вы угадали число!')
                    break
                elif index_2 == 0:
                    print('Увы вы проиграли!')
        elif index == 1:
            print('Увы вы проиграли!')
            break
else:
    print('Увы вы не прошли первый уровень... Попробуйте заного')
print('Пока-пока')

