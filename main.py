import PIL
from PIL import Image
import os
import xml.etree.ElementTree as ET
from numpy import asarray, asmatrix, reshape

def format_image():
    for i in range(785):
        image = Image.open(f'../src/datasets/no_pedestrian/{i}.png')
        resized_image = image.resize((36, 82))
        resized_image.save(f'../src/datasets/no_pedestrian_formatted/{i}.png')

'''
count = 0
a = -1
b = -1
c = -1
d = -1

for file in os.listdir('C:\\Users\HP\Downloads\\archive (1)\\PNGImages'):
    if file.endswith('xml'):
        tree = ET.parse('C:\\Users\HP\Downloads\\archive (1)\\PNGImages\\' + file)
        root = tree.getroot()
        for child in root.iter():
            if child.tag == 'xmin':
                a = int(child.text.strip())
            if child.tag == 'ymin':
                b = int(child.text.strip())
            if child.tag == 'xmax':
                c = int(child.text.strip())
            if child.tag == 'ymax':
                d = int(child.text.strip())
            if(a > 0 and b > 0 and c > 0 and d > 0):
                image = Image.open('C:\\Users\HP\Downloads\\archive (1)\\PNGImages\\' + file[:-4] + '.png')
                new_image = image.crop((a - 5, b, c, d))
                new_image.save(f'../src/datasets/no_pedestrian/{count}.png')
                a = b = c = d = -1
                count +=1
'''

X_train = X_test = Y_train = Y_test = []

datasets_path = '../src/datasets/'
prefix = ['pedestrian_formatted/', 'no_pedestrian_formatted/']
folder = ['train/', 'test/']

for i in range(len(prefix)):
    for j in range(len(folder)):
        images_path = datasets_path + prefix[i] + folder[j]
        for image_path in os.listdir(images_path):
            image = Image.open(images_path + image_path)
            if j == 0:
                image = asarray(image)
                X_train.append(reshape(image, (image.shape[0] * image.shape[1] * image.shape[2], 1)))
                Y_train.append(i)
            else:
                image = asarray(image)
                X_test.append(asarray(reshape(image, (image.shape[0] * image.shape[1] * image.shape[2], 1))))
                Y_test.append(i)




