from PIL import Image 
from os import listdir

with open('opencv-files/neg.txt', 'w') as file:

    for imagePath in listdir("opencv-files/negative"):
        print(imagePath)
        file.write('opencv-files/negative/{}\n'.format(imagePath))