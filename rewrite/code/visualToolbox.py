import cv2
import numpy as np
import glob


class visualToolbox:

    inputFolder = ""
    outputFolder = ""
    sizeX = 0
    sizeY = 0

    def __init__(self, size=(600, 480), inputFolder="../media/", outputFolder="../media/"):

        self.inputFolder = inputFolder
        self.outputFolder = outputFolder
        self.sizeX = size[0]
        self.sizeY = size[1]
        #monalisa_newsize = (600, 480)

    def removeColor(self, img, tellorance, color = (0,0,0)):

        #Height, Width, Layers = img.shape
        b, g, r = color[0], color[1], color[2]
        img[np.where(
            (b-tellorance < img[:, :, 0] < b + tellorance) &
            (g - tellorance < img[:, :, 1] < g + tellorance) &
            (r - tellorance < img[:, :, 2] < r + tellorance))] = [0, 0, 0]

        return img

    def removeAllButColor(self, img, tellorance, color = (0,0,0)):

        #Height, Width, Layers = img.shape
        b, g, r = color[0], color[1], color[2]
        img[np.where(
            ((b-tellorance > img[:, :, 0]) | (img[:, :, 0] > b + tellorance)) &
            ((g-tellorance > img[:, :, 0]) | (img[:, :, 0] > g + tellorance)) &
            ((r-tellorance > img[:, :, 0]) | (img[:, :, 0] > r + tellorance)))] = [0, 0, 0]

        return img

    def mixImage1ThatHasSpecifiedColorWithImage2(image1, image2, type='replace', color=(0, 0, 0)):
        #type can be 'add', 'multiply' or 'replace'
        if type == "add":
            mergedImg = cv2.add(image1, image2)

            return mergedImg

        elif type == "multiply":
            image1Hight, image1Width, image1Layar = image1.shape
            colorfulEdgesImg = np.ones([image1Hight, image1Width, 3])

            colorfulEdgesImg[np.where(image2 == 255)] = [200, 200, 200]
            colorfulEdgesImg
            mergedImg = np.multiply(colorfulEdgesImg, image1)
            mergedImg[mergedImg > 255] = 255

            return mergedImg

        else:
            pass
