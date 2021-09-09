# Voronov Andrei
# Исходные данные: Папка с изображениями, названными по имени автора 
# Цель: Написать Python-скрипт, который программным образом обработает каждое 
# изображение из исходных данных, добавив имя автора в качестве подписи, 
# взятое из названия изображения. (см. приложение)
# И далее сохранит изображения (оставив изначальное название) в папке, 
# указанной при запуске скрипта из терминала (по умолчанию сохраняет 
# в `./output-images/`)
# Требования: Выравнивание текста по правому нижнему углу. 
# Шрифт и размер шрифта по предпочтению. 
# Ориентировочное время выполнения: 2 часа (отсчет от начала выполнения задачи)

from PIL import Image, ImageDraw, ImageFont
import sys
import os

LOAD_PATH = sys.path[0] + '/source-images/'
BASE_SAVE_PATH = sys.path[0] + '/output-images/'
font = ImageFont.truetype(sys.path[0] + '/allison.ttf', 28, encoding="unic")

files_array = os.listdir(LOAD_PATH)
try:
    os.mkdir(sys.path[0] + '/output-images/')
except FileExistsError:
    try:
        os.rmdir(sys.path[0] + '/output-images/')
    except OSError:
        files_array_base = os.listdir(BASE_SAVE_PATH)
        for i in files_array_base:
            os.remove(BASE_SAVE_PATH + i)
for text in files_array:
    img = Image.open(LOAD_PATH + text)
    width, height = img.size
    draw = ImageDraw.Draw(img)
    width_text, height_text = draw.textsize(text[0:-4], font)
    draw.text(((width - width_text),(height - height_text)),text[0:-4], font=font)
    img.save(BASE_SAVE_PATH  + text, 'JPEG')
    img.close()



