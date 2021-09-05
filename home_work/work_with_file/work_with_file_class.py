# Voronov Andrei
import os
import utilic


def create_26_files():
    for i in range(65, 91):
        my_file = open(chr(i) + '.txt', 'w')
        my_file.write(chr(i))
        my_file.close()


def delete_26_files():
    for i in range(65, 91):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), chr(i) + '.txt')
        os.remove(path)


say = """Домашнее задание.
Выберите номер задания для проверки.
1. Создание 26 текстовых файлов.
2. Удаление этих 26 файлов.
3. Для выхода: """
while True:
    operation = utilic.chek_int_input(say, [1, 2, 3])
    if operation == 1:
        create_26_files()
    elif operation == 2:
        delete_26_files()
    elif operation == 3:
        exit()
