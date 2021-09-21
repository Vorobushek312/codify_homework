# class Email:
#   def send(self,text):
#     raise NotImplemented()


# class GmailMail(Email):
#   def send(self,text):
#     print('send email to gmail')

# class RuMail(Email):
#   def send(self,text):
#     print('send email to rumail')

# class YandexMail(Email):
#   def send(self,text):
#     print('send email to yandex')

# class YahooMail(Email):
#   def send(self,text):
#     print('send email to yandex')

# class ListMail(Email):
#   def send(self,text):
#     print('send email to yandex')

# def send_mail(email_handler: Email, text:str):
#   email_handler.send(text)

# user_input = input("Введите почту: ")
# if user_input == 'gmail':
#   send_mail(GmailMail(),'Hello')
# elif user_input == 'yandex':
#   send_mail(YandexMail(),'Hello')
# elif user_input == 'rumail':
#   send_mail(RuMail(),'Hello')
# elif user_input == 'yahoo':
#   send_mail(YahooMail(),'Hello')
# elif user_input == 'list':
#   send_mail(ListMail(),'Hello')

class User:
    def create(self):
        bad_word = 'bad'
        phone_validator = '+996'
        
        age = int(input("Введите возраст: "))
        if age < 18:
            raise "Вам нет 18, доступ запрещён!"

        email = input("Введите почту: ")
        if bad_word in email:
            raise 'Нельзя использовать такие слова при вводе!'

        users_file = open('/users.txt', "a")
        users_file.write(f"Почта: {email} Возраст: {age}")
        users_file.close()
class AgeValidator:
    def validate(self, age):
        raise NotImplemented()

class EmailValidator:
    def validate_email(self, email: str) -> bool:
        raise NotImplemented()


class InputHandler:
    def handle_input(self, placeholder: str) -> str:
        raise NotImplemented()


class Database:
    def save(self, info: dict) -> bool:
        raise NotImplemented()

class ConsoleInput(InputHandler):
    def handle_input(self, placeholder: str):
        result = input(placeholder)
        return result

class GmailEmail(EmailValidator):
    def validate_email(self, email: str):
        if 'gmail' == email.split('@')[1]:
            return True
        else:
            return False
            
class SaveToDatabase(Database):
  def save(self, info: dict):
    import os
    import sys
    try:
      with open(os.path.join(sys.path[0], 'user_data.txt'),'w') as file:
        import csv
        writer = csv.DictWriter(file, info.keys())
        writer.writeheader()
        writer.writerow(info)
        return True
    except Exception as e:
      print(e)
      return False


class User:
    def __init__(self, input_handler: InputHandler, \
    email_validator: EmailValidator, db: Database):

        self.input_handler = input_handler
        self.email_validator = email_validator
        self.db = db

    def create(self):
        email = self.input_handler.handle_input("Введите email: ")
        is_email_valid = self.email_validator.validate_email(email)
        if is_email_valid:
            self.db.save({'email:': email})