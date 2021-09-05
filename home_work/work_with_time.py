# Voronov Andrei
# 1. Написать программу с помощью которой пользователь, по выбору, может посмотреть
# - текущее число
# - месяц
# - год
# - время
# - полную дату и время в формате '%m/%d/%Y %H:%M:%S'
import utilic
import datetime
say = """Домашнее задание.
Выберите номер задания для проверки.
1. Посмотреть текущее число.
2. Посмотреть месяц.
3. Посмотреть год.
4. Посмотреть время
5. Посмотреть олную дату и время в формате '%m/%d/%Y %H:%M:%S
6. Для выхода: """
while True:
    optiont = utilic.chek_int_input(say, [1,2,3,4,5,6])
    current_datetime = datetime.datetime.now()
    if optiont == 1:
        print('Текуший день: ', current_datetime.day)
    elif optiont == 2:
        print("Текуший месяц: ", current_datetime.month)
    elif optiont == 3:
        print("Текуший год: ", current_datetime.year)
    elif optiont == 4:
        print("Текущее время: ", current_datetime.time())
    elif optiont == 5:
        print("Текушая дата: ", current_datetime.strftime('%m/%d/%Y %H:%M:%S'))
    elif optiont == 6:
        print("До скорых встречь!")
        exit()