def chek_int_input(say, range_list):
    while True:
        try:
            int_input = int(input(say))
            if int_input not in range_list:
                raise Exception('Нужно выбрать подходяшее число: ')
        except ValueError:
            print('Вы ввели не число!')
        except Exception as s:
            print(s)
        else:
            return int_input


def chek_int_input_not_range(say):
    while True:
        try:
            int_input = int(input(say))
        except ValueError:
            print('Вы ввели не число!')
        except Exception as s:
            print(s)
        else:
            return int_input


def chek_name_file():
    while True:
        try:
            filename = input('Введите назывние фаила.: ')
            filename += '.txt'
            file = open(filename)
            file.close()
        except FileNotFoundError:
            print('Фаил не найден')
        else:
            return filename


def chek_name_file_csv():
    while True:
        try:
            filename = input('Введите назывние фаила: ')
            filename += '.csv'
            file = open(filename)
            file.close()
        except FileNotFoundError:
            while True:
                try:
                    action = input('Фаил не найден. Вы хотите содать фаил с таким именем Да/Нет: ')
                    if action.title() not in ['Да', "Нет"]:
                        raise Exception('Не верный ввод!')
                except Exception as s:
                    print(s)
                else:
                    if action == 'Да':
                        file = open(filename, 'w')
                        file.close()
                        return filename
                    elif action == 'Нет':
                        print('Фаил не существует и не создан!')
                        exit()
        else:
            return filename




