# Классная работа:
# 1. Создать класс человек, с именем, фамилией и приватным полем secret
# для вывода имени и фамилии создайте отдельные методы и 
# приватный метод для вывода поля secret.

# class Human:
#     def __init__(self, name, surname, __secret) -> None:
#         self.name = name
#         self.surname = surname
#         self.__secret = __secret
    
#     def get_name(self):
#         print(self.name)
    
#     def get_surname(self):
#         print(self.surname)
    
#     def get_secret(self):
#         print(self.__secret)

# person_1 = Human('Andrei', 'Voronov', 'My secret')
# person_1.get_name()
# person_1.get_surname()
# person_1.get_secret()
# 4. Напишите класс Rectangle с атрибутами конструктора длины и ширины.
# Создайте метод Perimeter() для вычисления периметра прямоугольника и метод Area() для вычисления площади прямоугольника.
# Создайте метод display(), который отображает длину, ширину, периметр и площадь объекта.
# Создайте дочерний класс Parallelepipede, наследующий от класса Rectangle, с атрибутом height и еще одним методом Volume() для вычисления объема параллелепипеда.
# Приведите примеры использования.
# class Rectangle:
#     def __init__(self, lends, weidth) -> None:
#         self.lends = lends
#         self.weidth = weidth
#     def perimeters(self):
#         perimeter = (self.lends * 2) + (2 * self.weidth)
#         return perimeter
    
#     def areas(self):
#         area = self.lends * self.weidth
#         return area

#     def display(self):
#         print(self.lends, self.weidth, self.perimeters(), self.areas())

# class Parallelepipede(Rectangle):
#     def __init__(self, lends, weidth, heigh) -> None:
#         super().__init__(lends, weidth)
#         self.heigh = heigh
    
#     def volumes(self):
#         volume = self.lends * self.heigh * self.weidth
#         return volume

# test_1 = Rectangle(10, 20)
# test_1.display()

# test_2 = Parallelepipede(10, 20, 30)
# print(test_2.volumes())
# Напишите класс MyStr, наследующего от класса str, добавьте методы append() и pop(), работающие также как и в  классе list.
class MyStr(str):
    def __init__(self, string, addstr) -> None:
        self.string = string
        self.addstr = addstr
    def append(self):
        return self.string + self.addstr

test_1 = MyStr('Andrei', 'Anton')
print(test_1.append())

