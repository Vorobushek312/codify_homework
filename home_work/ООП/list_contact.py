# Voronov Andrei
# Создайте класс Contact, и объявите в конструкторе(__init__) ему поля
# name, last_name и number. Далее, создайте класс ContactList, в нем
# объявите переменную contacts_list = [], после, реализуйте три метода,
# add_contact(), который берет в аргументы объект класса Contact и
# добавляет в лист contacts_list, seacrh_contact(), который должен вернуть
# нам контакт если такой имеется в списке, remove_contact() который
# должен удалить найденный контакт, эти методы также принимают в
# качества аргумента объект класса Contact. Создайте несколько объектов
# класса Contact, и объект класса ContactList, воспользуйтесь всеми его
# методами.
def chek_int_input(say, range_list):
    while True:
        try:
            int_input = int(input(say))
            if int_input not in range_list:
                raise Exception('Нужно выбрать подходяшее число: ')
        except ValueError:
            print('Вы ввели не число!')
        except Exception as s:
            print(s)
        else:
            return int_input

class Contact:
    def __init__(self, name, last_name, number):
        self.name = name
        self.last_name = last_name
        self.number = number

class ContactList:
    contact_list = []
    
    def add_contact(self, cls):
        self.contact_list.append(cls) 
        return self

    def search_contact(self, name):
        index = 0
        for info_contact in self.contact_list:
            if name in info_contact[0]:
                index += 1
                print(f'Найден контакт {index}: Имя: {info_contact[0]} - Фамилия: {info_contact[1]} - Телефон: {info_contact[2]}.')
            if index == 0:
                print('Контактов не найдено.')
    
    def remove_contact(self, delete_contact):
        save_info = self.contact_list
        index = 0
        for info_contact in self.contact_list:
            if info_contact == delete_contact:
                print(f'Имя: {info_contact[0]} - Фамилия: {info_contact[1]} - Телефон: {info_contact[2]}. \
                \nКонтакт удален')
                del self.contact_list[index]
            else:
                index += 1
        if save_info == self.contact_list:
            print("Такой контакт не найден!")

say = 'Выберите операцию. \
        \n1. Добавить контакт. \
        \n2. Найти контакт. \
        \n3. Удалить контакт.\
        \n4. Для выхода.\n'
while True:
    contacts = ContactList()
    option = chek_int_input(say, [1,2,3,4])
    if option == 1:
        name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        number = input('Введите номер телефона: ')
        if contacts.contact_list != []:
                for info_phone in contacts.contact_list:
                    if number == info_phone[2]:
                        print('Контакт с таким телефоном уже сушествует.')
                        break
                else:
                    contact = Contact(name, last_name, number)
                    contacts.add_contact([contact.name, contact.last_name, contact.number])
                    print(f'Имя: {contact.name}\nФамилия: {contact.last_name}\nТелефон: {contact.number}\nУспешно добавлены.')
        else:            
            contact = Contact(name, last_name, number)
            contacts.add_contact([contact.name, contact.last_name, contact.number])
            print(f'Имя: {contact.name}\nФамилия: {contact.last_name}\nТелефон: {contact.number}\nУспешно добавлены.')
    elif option == 2:
        name = input('Введите имя которое ищите: ')
        contacts.search_contact(name)          
    elif option == 3:
        delete_contact = []
        name = input('Введите имя: ')
        delete_contact.append(name)
        last_name = input('Введите фамилию: ')
        delete_contact.append(last_name)
        number = input('Введите номер телефона: ')
        delete_contact.append(number)
        contacts.remove_contact(delete_contact)
    elif option == 4:
        print('Пока-пока')
        exit()



