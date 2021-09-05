# 1. Создайте классы вашей семьи и выделите какую характерную особенность, 
# записав её в качестве функции
# пример 
# class Mom:
    #   def cook_food():
    #       print('cook')

# class Family:
#     name = 'Andrei'
#     lastname = 'Voronov'
#     def drink(self, drink):
#         print(f'{self.lastname} {self.name} like drink {drink}')
#     def see_film(self):
#         print(f'{self.lastname} {self.name} see film')
#     def get_full_name(self):
#         print(f'Фамилия: {self.lastname} Имя: {self.name}')

# father = Family()
# father.drink('Tea')
# father.get_full_name()
# mather = Family()
# mather.name = 'Olga'
# mather.lastname = "Voronova"
# father.drink('juse')
# father.get_full_name()

# Создайте класс Animal с методами voice(),run(), fight() и классы наследники cat, dog, bird, fish, переопределите все методы
# в соответсвии с классом наследником, подготовьте примеры использования с использованием всех методов у классов наследников.
class Animal:
    sound = 'Da'
    speed = 40
    hit = 'Hit'
    action = 'run'
    def voice(self):
        print(self.sound)
    def run(self):
        print(f'Speed = {self.speed} km/h')
    def fight(self):
        print(self.hit)
    def option(self):
        print(self.action)
class Cat(Animal):
    def __init__(self,sound, speed, hit, action):
        self.sound = sound
        self.speed = speed
        self.hit = hit
        self.action = action
class Dog(Animal):
    def __init__(self,sound, speed, hit, action):
        self.sound = sound
        self.speed = speed
        self.hit = hit
        self.action = action
class Bird(Animal):
    def __init__(self,sound, speed, hit, action):
        self.sound = sound
        self.speed = speed
        self.hit = hit
        self.action = action
class Fish(Animal):
    def __init__(self,sound, speed, hit, action):
        self.sound = sound
        self.speed = speed
        self.hit = hit
        self.action = action

animal = Animal()
animal.voice()
animal.run()
animal.fight()
dog = Dog('wow', 30, 'Bites', "Man's best friend")
dog.voice()
dog.run()
dog.fight()
dog.option()
cat = Cat('myu', 25, 'Scratches', 'Calms the nerves')
cat.voice()
cat.run()
cat.fight()
cat.option()
bird = Bird('Cry', 65, 'Bite', "sleeps in a pallet")
bird.voice()
bird.run()
bird.fight()
bird.option()
fish = Fish('bul-bul', 15, 'eaiting', "Breathes underwater")
fish.voice()
fish.run()
fish.fight()
fish.option()