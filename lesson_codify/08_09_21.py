# class Person:
#     def __init__(self, first_name, last_name, middle_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.middle_name = middle_name
#         self.age = age
#     def __eq__(self, value):
#         return (len(self.first_name) + len(self.last_name) + len(self.middle_name)) == \
#             (len(value.first_name) + len(value.last_name) + len(value.middle_name))
#     def __add__(self, value):
#         return self.age + value.age
#     def __mul__(self, value):
#         return self.age * value.age

# person_1 = Person('Ant', 'Kri', 'XZZ', 23)
# person_2 = Person('And', 'Vor', 'And', 26)
# print(person_1 == person_2)
# print(person_1 + person_2)
# print(person_1 * person_2)



# class BankAccount:
#     def __init__(self, valet):
#         self.valet = valet
#     def __add__(self, value):
#         return self.valet + value
#     def __eq__(self, value):
#         return self.valet == value
#     def __mul__(self, value):
#         return self.valet * value
#     def __ge__(self, value):
#         return self.valet >= value
#     def __gt__(self, value):
#         return self.valet > value
#     def __lt__(self, value):
#         return self.valet < value
#     def __iadd__(self, value):
#         self.valet += value
#         return self

# bank_acc = BankAccount(50)
# print(bank_acc == 50) #True
# print(bank_acc + 30) 
# print(bank_acc * 5)
# print(bank_acc >= 30)
# print(bank_acc > 40)
# print(bank_acc < 60)
# bank_acc += 40
# print(bank_acc == 90)
# print(bank_acc.valet)

# class Animal:
#     def __init__(self, name) -> None:
#         self.name = name
#     def __str__(self) -> str:
#         return self.name
#     def __len__(self):
#         return len(self.name)

# animal_1 = Animal('Dog')
# print(str(animal_1))
# print(len(animal_1))

def print_start_end(func):
    def new_func():
        print('Start')
        func()
        print('End')
    return new_func

@print_start_end
def milti():
    print('Zzz')

milti()