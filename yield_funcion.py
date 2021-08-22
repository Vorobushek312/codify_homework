#Voronov Andrei
import utilic
import sys


def my_range(start , stop):
    while start != stop:
        yield start
        start += 1


def my_enumerate(values, start = 0):
    for value in values:
        yield start, value
        start += 1


def str_lower(a):
    return a.lower()


def my_map(fun, values):
    for value in values:
        yield fun(value)
# 1. Реализовать функцию range с помощью генератора.
say = """Домашнее задание.
Выберите номер задания для проверки.
1. Реализовать функцию range с помощью генератора.
2. Реализовать функцию enumerate с помощью генератора.
3. Реализовать функцию map с помощью генератора.
4. Для выхода: """
while True:
    option = utilic.chek_int_input(say, [1,2,3,4])
    if option == 1:
        print('Реализаци моего варианта range')
        start = utilic.chek_int_input_not_range('Ввндите начально число: ')
        stop = utilic.chek_int_input_not_range("Введите конечное число: ")
        print(list(my_range(start, stop)))
    elif option == 2:
        print('Реализаци моего варианта enumerate')
        value = input("Введите что нибудь!")
        start = utilic.chek_int_input_not_range('Введите число для начала счета')
        print(list(my_enumerate(value, start)))
    elif option == 3:
        print('Реализаци моего варианта map')
        value = input('Введите слово с збуквами верхнего региста и я выведу все в нижнем регисте')
        print(list(my_map(str_lower, value)))
    elif option == 4:
        print('Спасибо за проверку')
        exit()
# 2. Реализовать функцию enumerate с помощью генератора.
# 3. Реализовать функцию map с помощью генератора.









value = 'abc'
my_list = ['A', 'B', 'C', 'd']

# print(list(my_range(1, 10)))
# print(list(range(1, 10)))
# print(list(my_enumerate(value)))
# print(list(enumerate(value)))
# print(list(map(multi, my_list)))
# print(list(my_map(multi, my_list)))
# print(sys.getsizeof(list(my_range(1, 10))))
# print(sys.getsizeof(list(range(1, 10))))
# print(sys.getsizeof(list(my_enumerate(value))))
# print(sys.getsizeof(list(enumerate(value))))
# print(sys.getsizeof(list(map(multi, my_list))))
# print(sys.getsizeof(list(my_map(multi, my_list))))
