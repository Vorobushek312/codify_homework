def main(var_1, var_2):
    answer = var_1 - var_2
    print ("Сумма чисел ", var_1, '-', var_2, ' = ', answer)



if __name__ == '__main__':
    while True:
        var = input("Введите первое число: ")
        try:
            var_1 = float(var)
        except ValueError:
            print('"' + var + '" - не являеться числом!')
        else:
            break
    while True:
        var = input("Введите второе число: ")
        try:
            var_2 = float(var)
        except ValueError:
            print('"' + var + '" - не являеться числом!')
        else:
            break
    main(var_1, var_2)