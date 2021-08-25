# 1. Напишите программу которая спрашивает ФИО, телефон пользователя и
# записывает их в файл, в виде словаря, обработайте возможные ошибки.
# 2. Расширьте возможность программы (1) добавив поиск по ФИО, телефону.
# 3. Расширьте возможность программы (1) и (2) добавив удаление данных по ФИО, телефону.
import csv
import os
import sys
import utilic
say = """
1. Добавить информацию о человеке.
2. Найти информацию о человеке по ФИО или телефону
3. Удаление информации о человеке
4. Посмотреть всю информацию в базе.
5. Для выхода: """
print('Программа работы с информацией в фаилах.')
info_database = []
fail_name = utilic.chek_name_file_csv()
while True:
    operation = utilic.chek_int_input(say, [1, 2, 3, 4, 5])
    if operation == 1:
        name = input('Введите имя пользователя: ')
        surname = input('Введите фамилию пользователя: ')
        age = utilic.chek_int_input_not_range("Введите возраст: ")
        info_dict = {'name': name.title(), 'surname': surname.title(), 'age': age}
        info_database.append(info_dict)
        with open(fail_name, 'a') as file:
            writer = csv.DictWriter(file, info_database[0].keys())
            writer.writerows(info_database)
    elif operation == 2:
        find_user = input('Введите инофрмацию для поиска: ')
        with open(fail_name, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                for info in line:
                    if find_user.title() in info or find_user in info:
                        print(line)
    elif operation == 3:
        lines = list()
        delete_list = list()
        delete_name = input('Введите имя: ')
        delete_list.append(delete_name.title())
        delete_surname = input('Введите фамилию: ')
        delete_list.append(delete_surname.title())
        delete_age = input('Введите возраст: ')
        delete_list.append(delete_age)
        with open(fail_name, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                if row == delete_list:
                    lines.remove(row)
        with open(fail_name, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    elif operation == 4:
        with open(fail_name, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                print(line)
    elif operation == 5:
        print('Программа завершена:')
        exit()
