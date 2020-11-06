from PIL import Image 
from os import listdir

with open('neg.txt', 'w') as file:

    for imagePath in listdir("opencv-files/dataset-masks"):
        # print(imagePath)
        # im = Image.open('opencv-files/dataset-masks/{}'.format(imagePath))
        # result = im.point(lambda p: 255 -p)
        # result.save('opencv-files/dataset-negative-masks/{}'.format(imagePath))
        file.write('opencv-files/dataset-negative-masks/{}'.format(imagePath))
