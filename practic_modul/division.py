def main(var_1, var_2):
    if var_2 != 0:
        answer = var_1 / var_2
        print("Деление чисел ", var_1, '/', var_2, ' = ', answer)
    else:
        print('На 0 делить нельзя')

def get_number():
    while True:
        var = input("Введите число: ")
        try:
            var_1 = float(var)
        except ValueError:
            print('"' + var + '" - не являеться числом!')
        else:
            return var_1

if __name__ == '__main__':
    var_1 = get_number()
    var_2 = get_number()
    main(var_1, var_2)