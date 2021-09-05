# Voronov Andrei
# Задачи на обработку ошибок:
# 1. Написать функцию которая принимает 1 аргумент, если это не число выбрасываем своё исключение(через raise Exception("")), 
# если число,то, если оно четное - выбрасываем исключение ValueError, если оно меньше 0 - TypeError, если оно больше 10 - IndexError. 
# Обрабатываем ошибку, говорим пользователю, в чем его ошибка
def value_error(value):
    try:
        value = float(value)
    except Exception:
        print('То что вы ввели не являеться числом, введите пожалуйста число!')
    else:
        try:
            if value < 0:
                raise TypeError()
            elif value % 2 == 0:
                raise ValueError()
            elif value > 10:
                raise IndexError()
        except TypeError:
            print(value, 'Это число меньше 0! Введите число больше 0')
        except ValueError:
            print(value, 'Это число четное! Введите число не четное')
        except IndexError:
            print(value, 'Это число больше 10! Введите число меньшн 10')
        else:
            print(value, 'Число подходит по всем условиям')
    
value = input('Введите число>>> ')
value_error(value)
    
# 2. Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть. Если все хорошо - пишите объект в консоль. 
# Если нет - обработайте возмозможные ошибки и скажите ему, что не так
my_list = [1, 2, 3, 4, 5, 'Andrei', 'Sasha', 'Dasha']

value = input('Введите индекс списка для просмотра значения>>> ')
try:
    value = int(value)
    my_list[value]
except IndexError:
    print('Такого значения нет в списке!')
except ValueError:
    print('Индекс может быть только целое число. Введите целое число.')
else:
    print(my_list[value])
