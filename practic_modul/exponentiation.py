from division import get_number 
def main(var_1, var_2):
    answer = var_1 ** var_2
    print("Число ", var_1, 'в степени', var_2, ' = ', answer)



if __name__ == '__main__':
    var_1 = get_number()
    var_2 = get_number()
    main(var_1, var_2)