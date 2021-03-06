# resizeAndAddLogo.py - Resizes all images in current working directory to fit 
# in a 300x300 square, and adds catlogo.png to the lower-right corner.
import os
from PIL import Image
os.chdir('automate_online-materials')
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME).resize((50,50))
logoWidth, logoHeight = logoIm.size
os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.gif') or filename.endswith('.bmp')) \
    or filename == LOGO_FILENAME:
        continue
    
    im = Image.open(filename)
    width, height = im.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    print('Adding logo to %s...' % (filename))
    logoCopy = logoIm.copy()
    logoCopy.resize(width/8, ((width/8)*logoHeight)/logoWidth)
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join('withLogo', filename))
