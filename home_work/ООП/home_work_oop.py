# Voronov Andrei
# ООП:
from prettytable import PrettyTable
# Нужно создать класс User(пользователь), у которого есть такие свойства: username, email, password
class User:
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = password
user_1 = User('Andrei', '212@gmail.com', '1234')
user_2 = User('Anton', 'Ant@gmail.com', '223344')
user_3 = User('Dasha', 'qwer321@list.ru', '332211')
# Создать еще один класс Group, у которого есть свойство users - это будет список, по умолчанию пустой
class Group:
    users = []
group = Group()
group.users.append([user_1.username, user_1.email, user_1.password])
group.users.append([user_2.username, user_2.email, user_2.password])
group.users.append([user_3.username, user_3.email, user_3.password])
# Затем создать класс TablePrinter, у которого будет метод(функция) print(), в который можно будет передать объект класса Group, а TablePrinter 
# распечатает на экран список всех пользователей в этой группе. Таблица должна быть такой:
 
 
# TEXT
# username | email | password

# master_alish | masteraalish@gmail.com | ******
# monreal | monrealdesign@vk.ru | ********
# santa_barbara | disco@mail.com | ******

class TablePrinter:
    def print_user(self, users):
        print_users = PrettyTable()
        print_users.field_names = ['username', 'email', 'password']
        for user in users:
            print_users.add_row([user[0], user[1], '*****'])
        print(print_users)
    def print_only_gmail(self, users):
        print_users = PrettyTable()
        print_users.field_names = ['username', 'email', 'password']
        for user in users:
            if '@gmail.com' in user[1]:
                print_users.add_row([user[0], user[1], '*****'])
        print(print_users)
print_1 = TablePrinter()
print_1.print_user(group.users)
print_1.print_only_gmail(group.users)



# Сверху обязательно идет заголовок таблицы. Пароли заменяем на звездочки, так как пароли не принято показывать нигде для безопасности.
# Также у класса TablePrinter должен быть второй метод print_only_gmail() который также принимает объект класса Group, и также выводит список пользователей.
#  Но только тех пользователей у которых почта @gmail.com.
