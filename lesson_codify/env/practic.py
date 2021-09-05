from PIL import Image, ImageDraw, ImageFont
FILE_NAME = 'test.jpg'
# box = (20, 0, 100, 400)

# img = Image.open(FILE_PASS)
# img.thumbnail((100,100))
# img.save('test_2.jpg', 'JPEG')
# img.close()

# try:
#     with Image.open(FILE_PASS) as im:
#         region = im.crop(box)
#         region.save('test_3.jpg', "JPEG")
# except OSError:
#     print("cannot create thumbnail for ", FILE_PASS)

img = Image.open(FILE_NAME)
draw = ImageDraw.Draw(img)
draw.text((5,10),'MY PYTHON')
img.save('test_4.jpg', 'JPEG')
img.close()