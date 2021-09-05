def get_number(opis, value):
    while True:
        try:
            value_user = int(input(opis))
            if not 0 < value_user <= value:
                raise Exception('Вам нужно угодать число от 1 до ' + str(value))
        except ValueError:
            print('Вам нужно ввести число!')
        except Exception as s:
            print(s)
        else:
            return value_user
import random
index = 1
opis = ('Попытка № ' + str(index) + ' : ')
print('Первый уровень! Угадайте число от 1 до 10. У вас есть 1 попытка!')
value_random = random.randint(1,10)
print(value_random)
value_user = get_number(opis, 10)
if value_random == value_user:
    print('''Поздравляем вы угадали число!
Второй уровень! Угадайте число от 1 до 50. У вас есть 3 попытки!''')
    value_random = random.randint(1,50)
    print(value_random)
    while index != 4:
        opis = ('Попытка № ' + str(index) + ' : ')
        value_user = get_number(opis, 50)
        if value_user == value_random:
            print('''Поздравляем вы угадали число!
Третий уровень! Угадайте число от 1 до 100. У вас есть 5 попытки!''')
            index_2 = 1
            value_random = random.randint(1,100)
            print(value_random)
            while index_2 != 6:
                opis = ('Попытка № ' + str(index_2) + ' : ')
                value_user = get_number(opis, 100)
                if value_user == value_random:
                    print('Поздравляем вы угадали число!')
                    break
                else:
                    print('Увы вы не прошли уровень... Попробуйте заного')
                index_2 += 1
        else:
            print('Увы вы не прошли уровень... Попробуйте заного')
        index += 1
else:
    print('Увы вы не прошли уровень... Попробуйте заного')
print('Пока-пока')

