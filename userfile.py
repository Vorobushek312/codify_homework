# Voronov Andrei
# Напишите программу которая позволяет пользователю:
# 1. Записать какой-то текст в файл
# 2. Найти записанный текст в файле по дате, либо по содержимому в ней.
import utilic
say = """Домашнее задание.
Выберите номер задания для проверки.
1. Записать какой-то текст в файл.
2. Найти записанный текст в файле по дате, либо по содержимому в ней..
3. Добавить запись в фаил
4. Посмотреть содиржимое фаила
5. Для выхода: """
while True:
    option = utilic.chek_int_input(say, [1, 2, 3, 4, 5])
    if option == 1:
        filename = input('Введите назывние фаила. (Если такой фаил существует то он перезапишеться).: ')
        filename += '.txt'
        info_text = input('Введите что хотите записать в фаил: ')
        with open(filename, 'w') as file:
            file.write(info_text + '\n')
        print('Фаил сохоанен!')
    elif option == 2:
        find_list = []
        filename = utilic.chek_name_file()
        find_text = input('Введите что хотите найти в фаиле.')
        with open(filename, 'r') as file:
            for line in file:
                if find_text in line:
                    find_list.append(line)
        if find_list != []:
            for line in find_list:
                print(line, end='')
    elif option == 3:
        filename = utilic.chek_name_file()
        add_text = input("Введите текст: ")
        with open(filename, 'a')as file:
            file.write(add_text + '\n')
    elif option == 4:
        filename = utilic.chek_name_file()
        with open(filename, 'r') as file:
            for line in file:
                print(line, end="")
    elif option == 5:
        print('Bye')
        exit()

