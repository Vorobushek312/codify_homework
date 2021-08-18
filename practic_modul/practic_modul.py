# Калькулятор для 4ых операций(+,-,*,/), каждая операция - в отдельном модуле,
# основной модуль программы - main.py
# Сделать возможность запускать модули самостоятельно и выполнять приведённый в них функционал, с помощью конструкции: 
# if __name__ == '__main__':
#       pass # ваш код
from division import get_number 
from summa import main as summ
from subtraction import main as subtr
from multiplication import main as multi
from division import main as divisions
from exponentiation import main as expo
def main():
    print("Добро пожаловать в мой калькулятор.")
    print("Если вы хотите им воспользоваться то отправьте любое сообшение.")
    print("Для выхода напишите stop")
    i = input()
    while i != 'stop':
        var_1 = get_number()
        print("""Введите + для сложения
Введите - для вычетания
Введите * для умножения
Введите / для деления
Введите ** для возведения в степень""")
        while True:
            operation = input('Введите операцию: ')
            if operation in ['+', '/', '-', '*', '**']:
                break
            else:
                print('"' + operation + '" - не являеться операцией!')
        var_2 = get_number()
        if operation == '+':
            answer = summ(var_1, var_2)
            print('Сумма чисел равна', answer)
        elif operation == '-':
            answer = subtr(var_1, var_2)
            print('Разность чисел равна', answer)
        elif operation == '*':
            answer = multi(var_1, var_2)
            print('Произведение чисел равна', answer)
        elif operation == '/':
            answer = divisions(var_1, var_2)
            print('Деление чисел равна', answer)
        elif operation == '**':
            answer = expo(var_1, var_2)
            print('возведение в степень чисел равна', answer)
        print("Если вы хотите продолжить напишите любое слово.")
        print("Для выхода напишите stop")
        i = input()
    print('Bye')

if __name__ == '__main__':
      main()