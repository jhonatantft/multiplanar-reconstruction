import os, re
import numpy as np
import matplotlib.pyplot as plt

def rename_files(path):
    for count, filename in enumerate(os.listdir(path)):
        name, number = filename.split('.')

        if (bool(re.search('^[-+]?[0-9]+$', number))):
            number = str('%03d' % int(number),)
            new_filename = name + '.' + number
            os.rename(path + filename, path + new_filename)

def buildsSectionByAxis(images, section, axis = None):
    newImage = []
    if not axis:
        return images[section]
    if axis == 'y':
        for image in images:
            newImage.append(image[section])
    if axis == 'z':
        for image in images:
            newLine = []
            for line in image:
                newLine.append(line[section])
            newImage.append(newLine)
    return newImage

def retrieveEachImage(root, files, images):
    resolution = [512, 512]
    for file in files:
        image = np.fromfile(os.path.join(root, file), dtype='int16', sep='')
        images.append(image.reshape(resolution))

def getImages(path, images):
    for (root, directories, files) in os.walk(path):
        files.sort()
        retrieveEachImage(root, files, images)
    return images

def show_images(images):
    for i in range(len(images)):
        plt.imshow(images[i], cmap='gray')
        plt.show()

def main():
    # rename_files('/home/jhonatan/Desktop/multiplanar-reconstruction/Arterielle/')
    frame = 350
    images = getImages('./Arterielle', [])
    sectionX = buildsSectionByAxis(images, frame)
    sectionY = buildsSectionByAxis(images, frame, 'y')
    sectionZ = buildsSectionByAxis(images, frame, 'z')
    show_images([sectionX, sectionY, sectionZ])

if __name__ == '__main__':
    main()
