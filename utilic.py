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