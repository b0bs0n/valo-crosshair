from PIL import Image
filename = 'icon.png'
with Image.open(filename) as img:
    img.save('icon.ico')
