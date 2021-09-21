# Напишите класс Song с полями name(str), tags(tuple), authors(list) и методами класса которые позволяют
# создать песню с тэгами:
#         1. electronic, experimental, rock
#         2. ambient, metal, punk
#         3. lo-fi, dark ambient, industrial
#         4. для песен Майкла Джексона, определите тэги сами
#         5. Любой автор по выбору для которого вы должны определить тэги

class Song:
    def __init__(self, tags,  authoes = None, name = None) -> None:
        self.name = name
        self.tags = tags
        self.authors = authoes
    def __repr__(self) -> str:
        return f'Название: {self.name}, таги: {self.tags} , автор: {self.authors}'
    
    @classmethod
    def electronic(cls):
        return  cls(['electronic' , 'experimental' , 'rock'],)
    @classmethod
    def ambient(cls):
        return cls(['ambient', 'metal', 'punk'],)
    @classmethod
    def industrial(cls):
        return cls(['lo-fi', 'dark ambient', 'industrial'])
    @classmethod
    def jackson(cls):
        return cls(['R&B', 'Rock', 'Pop'], 'Michael Jackson')
    @classmethod
    def guf(cls):
        return cls(['Rap', 'Hip-Hop', 'Gunster Rap'], 'guf')
    
djq = Song.electronic()
noname_dj = Song.ambient()
noyze = Song.industrial()
jackson = Song.jackson()
gufi = Song.guf()
print(djq)
print(noname_dj)
print(noyze)
print(jackson)
print(gufi)
    