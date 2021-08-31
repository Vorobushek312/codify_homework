# Voronov Andrei
# 1. Создайте класс Vehicle с атрибутами экземпляра max_speed и mileage


class Vehicle():
    max_speed = 90
    milwage = 216


# 2. Создайте класс Vehicle без переменных и методов


class Vehicle():
    pass


# 3. Создайте класс Person с атрибутами экземпляра first_name,last_name,middle_name,email,is_active и методами get_full_name - возвращает полное имя, 
# get_gmail - возвращает только почту с доменом @gmail.com. Создайте 5 экземпляров класса Person с разными параметрами и выведите в консоль все параметры 
# созданных вами классов.


class Person():
    first_name = 'Андрей'
    last_name = 'Воронов'
    middle_name = 'Андреевичь'
    email = 'Voronov_95@gmail.com'
    is_active = True


    def get_full_name(self):
        full_name = (f'''Фамилия: {self.last_name}\nИмя: {self.first_name} \nОтчество: {self.middle_name}''')
        return full_name


    def get_gmail(self):
        if '@gmail.com' in self.email:
            return self.email
        else:
            return 'gmail не верный.'


person_1 = Person()
person_1.first_name = 'Александр'
person_1.middle_name = 'Евгеньивичь'
person_1.last_name = 'Михеев'
person_1.email = 'Alex@gmail.com'
person_2 = Person()
person_2.first_name = 'Дарья'
person_2.middle_name = 'Валерьевна'
person_2.last_name = 'Костко'
person_2.email = 'Dasha_1994@gmail.com'
person_3 = Person()
person_3.first_name = 'Дарья'
person_3.middle_name = 'Николаевна'
person_3.last_name = 'Федорина'
person_3.email = 'Daria_93@gmail.com'
person_4 = Person()
person_4.first_name = 'Анна'
person_4.middle_name = 'Михайловна'
person_4.last_name = 'Игначкова'
person_4.email = 'Anna_ignach@gmail.com'
person_5 = Person()
person_5.first_name = 'Антон'
person_5.middle_name = 'Эдуардовичь'
person_5.last_name = 'Уваров'
person_5.email = 'Anton_55994@gmail.com'

print(person_1.get_full_name() + '\n' + person_1.get_gmail() + '\n')
print(person_2.get_full_name() + '\n' + person_2.get_gmail() + '\n')
print(person_3.get_full_name() + '\n' + person_3.get_gmail() + '\n')
print(person_4.get_full_name() + '\n' + person_4.get_gmail() + '\n')
print(person_5.get_full_name() + '\n' + person_5.get_gmail() + '\n')
