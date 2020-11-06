from PIL import Image 
from os import listdir

with open('opencv-files/neg.txt', 'w') as file:

    for imagePath in listdir("opencv-files/positive"):
        print(imagePath)
        im = Image.open('opencv-files/positive/{}'.format(imagePath))
        result = im.point(lambda p: 255 -p)
        result.save('opencv-files/negative/{}'.format(imagePath))
        file.write('opencv-files/negative/{}\n'.format(imagePath))