# Voronov Andrei
# 1. Напишите lambda функцию которая принимает число и возвращает его возведенным в степень двойки
answer_1 = lambda value: value**2
print(answer_1(3))
# 2. Напишите lambda функцию которая принимает строку и возвращает её в верхнем регистре.
answer_2 = lambda string: string.upper()
print(answer_2('Andrei'))
# 3. Напишите lambda функцию которая принимает строку и возвращает её в нижнем регистре.
answer_3 = lambda string: string.lower()
print(answer_3('Andrei'))
# 4. Напишите lambda функцию которая принимает список или tuple и возвращает последний элемент.
my_list = [1, 2, 3, 4, 5, 'd']
my_tuple = (1, 2, 3, 4, 5, 'e')
answer_4 = lambda last_index: last_index[-1]
print(answer_4(my_list), answer_4(my_tuple))
# 5. Дан список: [1,2,3,4,5,6,834,123, 99,32, 644 ] с помощью спискового включения - сформируйте новый список только из чётных элементов.
my_list = [1,2,3,4,5,6,834,123, 99,32, 644 ]
new_list = [x for x in my_list if x % 2 == 0]
print(new_list)
