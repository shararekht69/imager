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

    def changeColorToTempColor(self, img, tellorance, color = (0,0,0), tempColor = (0,0,0)):

        #Height, Width, Layers = img.shape
        b, g, r = color[0], color[1], color[2]
        img[np.where(
            (b-tellorance < img[:, :, 0] < b + tellorance) &
            (g - tellorance < img[:, :, 1] < g + tellorance) &
            (r - tellorance < img[:, :, 2] < r + tellorance))] = tempColor

        return img

    #def removeAllButColor(self, img, tellorance, color = (0,0,0)):
    #    #Height, Width, Layers = img.shape
    #    b, g, r = color[0], color[1], color[2]
    #    img[np.where(
    #        ((b-tellorance > img[:, :, 0]) | (img[:, :, 0] > b + tellorance)) &
    #        ((g-tellorance > img[:, :, 0]) | (img[:, :, 0] > g + tellorance)) &
    #        ((r-tellorance > img[:, :, 0]) | (img[:, :, 0] > r + tellorance)))] = [0, 0, 0]
    #    return img

    def addOrMultipyImgs(image1, image2,w1=1, w2=1, type='replace'):
        #type can be 'add', 'multiply' 
        if type == "add":
            addedImg = cv2.add(image1*w1, image2*w2)//(w1+w2)
            addedImg[addedImg > 255] = 255
            return addedImg

        elif type == "multiply":
            #image1Hight, image1Width, image1Layar = image1.shape
            #colorfulEdgesImg = np.ones([image1Hight, image1Width, 3])

            #colorfulEdgesImg[np.where(image1 == 255)] = [200, 200, 200]
            #colorfulEdgesImg
            
            #mergedImg = np.multiply(colorfulEdgesImg, image1)
            MultipliedImg = np.multiply(image1*w1, image2*w2)//(w1+w2)
            MultipliedImg[MultipliedImg > 255] = 255

            return MultipliedImg



    def mergeImg2onImg1WhereImg1hasTempColor(image1, image2, tempColor = (0,0,0)):
        b, g, r = tempColor[0], tempColor[1], tempColor[2]
        image1[np.where(
            (image1[:, :, 0] == b) &
            (image1[:, :, 1] == g) &
            (image1[:, :, 2] == r))] = image2[np.where(
            (image1[:, :, 0] == b) &
            (image1[:, :, 1] == g) &
            (image1[:, :, 2] == r))] 
        return image1
