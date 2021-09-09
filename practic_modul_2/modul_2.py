# 1. Определите класс Book со следующими атрибутами: Название, Автор (полное имя), Цена.
# Определите конструктор, используемый для инициализации атрибутов метода значениями, введенными пользователем.
# Задайте метод View() для отображения информации для текущей книги.
# Протестируйте.
# class Book:
#     def __init__(self, name, apthor, price) -> None:
#         self.name = name
#         self.apthor = apthor
#         self.price = price
#     def view(self):
#         print(f'''1. Название : {self.name} 
# 2. Автор: {self.apthor}
# 3. Цена: {self.price}''')
# for i in range(3):
#     name = input('Введите название книги: ')
#     apthor = input('Введите автора книги: ')
#     price = input('Введите цену книги: ')
#     info_book = Book(name, apthor, price)
#     info_book.view()
# 2. Определите класс Playlist, его метод __init__() должен иметь два аргумента: self,
# song_list - список из классов Song.
# Класс Song с полями:
# - name - название песни,
# - lyric - слова песни.
# Создайте список из классов песней и передайте в класс Songs.
# Внутри класса Playlist создайте метод sing_me_a_song(song_name), который находит песню по её названию и выводит
# каждый элемент текста песни в отдельной строке. Обработайте возможные ошибки.
# class Playlist:
#     def __init__(self, song_list) -> None:
#         self.song_list = song_list
#     def sing_me_a_song(self):
#         name = input('Введите название исполнителя: ')
#         for text in self.song_list:
#             if name in text[0]:
#                 print(text[1])
# class Song:
#     def __init__(self, name, lyric) -> None:
#         self.name = name
#         self.lyric = lyric
    
# class Songs:
#     list_songs = []

# song_1 = Song('Guf', '''Ice... Ice, ice baby,
# Я буду тебя любить, даже когда я буду на небе...
# Ну а пока что я здесь. И я в рэпе,
# И я тебя люблю, слышишь, ice baby...''')
# song_2 = Song('Guf', """Ведь сегодня-завтра будет вчера, а еще вчера-сегодня было завтра
# Тут имеет смысл подождать до утра и уж потом строить планы, что-то загадывать
# Сегодня-завтра будет вчера, еще вчера-сегодня было завтра
# Имеет смысл подождать до утра, и уж потом строить планы, что-то загадывать""")
# songs = Songs()
# songs.list_songs.append([song_1.name, song_1.lyric])
# songs.list_songs.append([song_2.name, song_2.lyric])
# play = Playlist(songs.list_songs)
# play.sing_me_a_song()

# 3. Игра в кости для 2ух игроков, игроки по очереди бросают кости, начинает первый игрок, 
# пока он вводит в консоль слово: mix - кости перемешиваются(максимум 5 раз, иначе автопоражения, предупреждать об оставшемся количестве перемешиваний), 
# если вводит любое другое слово кости бросаются и показывается результат(он записывается), потом очередь 2ого игрока.
# После этого тоже самое делает 2ой игрок и так 3 раза, у кого по итогу этих 3-ёх раз будет большее число - тот победил.

# import random
# def bit_user(text):
#     index = 0
#     while True:
#         print(text)
#         option = input('mix - перемешает кости, другое слово бросит кубики: ')
#         if option == 'mix':
#             print("Кости перемешаны.")
#             index += 1
#             if index == 5:
#                 print('Автопорожение.')
#                 exit()
#             continue
#         else:
#             value_1 = random.randrange(1,6)
#             print("Результат первого кубика:", value_1)
#             value_2 = random.randrange(1,6)
#             print("Результат второго кубику:", value_2)
#             result = value_1 + value_2
#         return result
# summ_u1 = 0
# summ_u2 = 0
# for i in range(3):
#     user_1 = bit_user('Первый игрок бросает кости.')
#     user_2 = bit_user('Второй игрок бросает кости.')
#     summ_u1 += user_1
#     summ_u2 += user_2
#     print('Сумма брокска(ов) первого игрока:', summ_u1)
#     print('Сумма брокска(ов) второго игрока:', summ_u2)
# if summ_u1 == summ_u2:
#     print('Ничья')
# elif summ_u2 > summ_u1:
#     print('Выйграл второй игрок.')
# else:
#     print('Выйграл первый игрок.')

# 4. Функции для расчета стоимости вашей поездки:
# Определите функцию hotel_cost с одним аргументом nights в качестве входных данных. Стоимость проживания в отеле составляет 140 долларов за ночь. 
# Таким образом, функция hotel_cost должна возвращать 140 * nights.
# Определите функцию plane_ride_cost, которая принимает на вход строку city. Функция должна возвращать разные цены в зависимости от местоположения, 
# как в примере кода выше. Ниже приведены допустимые пункты назначения и соответствующие им цены туда и обратно.
# "Шарлотт": 183
# "Тампа": 220
# "Питтсбург": 222
# "Лос-Анджелес": 475
# -Под существующим кодом определите функцию rental_car_cost с аргументом days. Рассчитайте стоимость аренды автомобиля: Каждый день аренды автомобиля 
# стоит $40.(cost=40*days) Если вы арендуете автомобиль на 7 или более дней, вы получаете скидку $50(cost-=50). В качестве альтернативы (elif), если 
# вы арендуете автомобиль на 3 или более дней, вы получите скидку $20. Вы не можете получить обе вышеуказанные скидки. Верните эту стоимость. -Затем 
# определите функцию trip_cost, которая принимает два аргумента, город и дни. Как и в примере выше, пусть ваша функция возвращает сумму вызовов функций 
# rental_car_cost(days), hotel_cost(days) и plane_ride_cost(city).
# Измените определение функции trip_cost. Добавьте третий аргумент, spending_money. Измените то, что делает функция trip_cost. Добавьте переменную 
# `spending_money к возвращаемой ею сумме.

def hotel_cost(nights):
    return nights * 140
def plane_ride_cost(city, plane_ride):

        for city_place in plane_ride:
            if city_place['city'] == city:
                return city_place['price']
plane_ride = [
    {'city' : "Шарлотт", 'price' : 183},
    {'city' : "Тампа", 'price' : 220},
    {'city' : "Питтсбург", 'price' : 222},
    {'city' : "Лос-Анджелес", 'price' : 475}
]
def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost
def trip_cost(city, days, spending_money):
    return int(rental_car_cost(days)) + int(hotel_cost(days) + plane_ride_cost(city, plane_ride)) + spending_money
for i in plane_ride:
    print(i['city'] + ':', i['price'])
city = input('Введите название города куда хотите отправиться: ')
days = int(input('Введите количество дней для путевки: '))
spending_money = int(input('Введите деньги на непредвиденные расходы: '))
summ_money = trip_cost(city, days, spending_money)
print(f'Сумма денег к оплате для поездки в город {city} на {days} дней с другими расходами в {spending_money} составляет :{summ_money}')
