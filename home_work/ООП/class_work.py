# 3.Создайте класс Plane, конструктор которого принимает brand,
# model. Пропишите в классе метод __str__. Пусть он возвращает
# brand и model самолета. Создайте подклассы Destroyer
# (Истребитель), Stelth (Стэлс), Kukuruznik (Кукурузник). В классе
# Destroyer перегрузите метод конструктор с помощью функции
# super(), добавьте поле can_fire = True. Также создайте в классе
# Destroyer метод fire (стрелять). В классе Stelth перегрузите метод
# конструктор с помощью функции super(), добавьте поле is_visible
# = False. Также добавьте метод hide (прятаться) в класс Stelth. А в
# классе Kukuruznik перегрузите метод конструктор с помощью
# функции super(), добавьте поле can_fertilize = True. Создайте в
# классе метод fertilize (распылять удобрения).Также создайте
# класс миксин SwimMixin, который будет иметь метод swim().
# Унаследуйтесь от этого класса миксина для классов Destroyer,
# Stelth, Kukuruznik. Используйте созданные классы и методы.
# 4.Напишите функцию go_for_a_walk(), которая зовет погулять. Она будет
# распечатывать на экран "Давай, пойдем погуляем на улице!" Напишите
# декоратор, который будет принимать параметр temperature (декоратор тройной
# вложенности). Температуру должен вводить пользователь. Добавьте проверку
# на тип получаемых данных от пользователя используя конструкцию try - except.
# Переведите данные в int и прокиньте в декоратор.
# Если температура больше 10 С, то декоратор должен вызвать функцию
# go_for_a_walk и затем распечатать "На улице тепло, давай погуляем, я не
# против!". Если от 0 до 10 С, то он вызовет функцию и распечатает "Прохладно.
# Надо одеться!", если от -10 до 0 (не включая 0), то - "Холодно. Потеплее
# оденься и пойдем!", если меньше -10, то "Мороз. Лучше давай дома посидим,
# фильм посмотрим!"
class SwimMixin:
    def swim(self):
        print('Swim')
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def __str__(self):
        print(self.brand, self.model)

class Destroyer(Plane, SwimMixin):
    def __init__(self, can_fire = True):
        super().__init__()
        self.can_fire = can_fire
    def fire():
        pass
    def swim(self):
        super().swim()
        print('Destroyer swim')
class Stelth(Plane, SwimMixin):
    def __init__(self, is_visible = False):
        super().__init__()
        self.is_visible = is_visible
    def hide():
        pass
class Kukuruznik(Plane, SwimMixin):
    def __init__(self, can_fertilize = True):
        super().__init__()
        self.can_fertilize = can_fertilize
    def fertilize():
        pass
class SwimMixin:
    def swim():
        pass

destr = Destroyer('Opel', '226')
destr.__str__