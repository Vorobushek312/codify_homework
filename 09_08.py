# # my_list = ['1','2','3', [1,2,3,4,5]]
# # result = list(map(len, my_list))
# # print(result)

# # Классная работа
# # 1. Используя функцию map получить сформировать из списков:
# # - [(1,2,3),['15',99],[17]]
# # - ['123456789',[],(),'00000000000000001']
# # 1.1 списки с длинной элементов в этих списках.
# # 1.2 если элемент списка является списком(list), добавить в начало символ ':)'
# # в конец ':('
# # 1.3 Если элемент в списке является кортежом или списком, то возращать первый и последний элемент.

# my_list = [(1,2,3),['15',99],[17]]
# my_list_2 = ['123456789',[],(),'00000000000000001']
# result = list(map(lambda x : len(x), my_list))
# result_1 = list(map(lambda x : len(x), my_list_2))
# # print(result, result_1)



# # def find_list(my_list1):
# #     if type(my_list1) == list:
# #         my_list1.append(':(')
# #         my_list1.insert(0, ':)')
# #     return my_list1
# # result_2 = list(map(find_list, my_list))
# # result_3 = list(map(find_list, my_list_2))
# # # print(result_2, result_3)

# def my_func(my_listt):
#     if type(my_listt) == list or type(my_listt) == tuple:
#         first_value = my_listt[0]
#         last_value = my_listt[-1]
#         return first_value, last_value

# result_4 = list(map(my_func, my_list))
# print(result_4)
product = {'chees':120, 'milk': 40, 'meat':400, 'water':25}
itemslist = product.items()
print(type(itemslist))