import cv2
import numpy as np


class visualToolbox:

    inputFolder = ""
    outputFolder = ""
    size = (0,0)

    def __init__(self, size=(600, 480), inputFolder="../media/", outputFolder="../media/"):

        self.inputFolder = inputFolder
        self.outputFolder = outputFolder
        self.size = size

    def changeColorToTempColor(self, img, tellorance, color = (0,0,0), tempColor = (0,0,0)):
        b, g, r = color[0], color[1], color[2]
        img[np.where(
            (b-tellorance < img[:, :, 0] < b + tellorance) &
            (g - tellorance < img[:, :, 1] < g + tellorance) &
            (r - tellorance < img[:, :, 2] < r + tellorance))] = tempColor
        return img

    def addImgs(self, img1, img2,w1=1, w2=1):
            addedImg = cv2.add(img1*w1, img2*w2)//(w1+w2)
            addedImg[addedImg > 255] = 255
            return addedImg

    def multipyImgs(self, img1, img2,w1=1, w2=1):
        MultipliedImg = np.multiply(img1*w1, img2*w2)//(w1+w2)
        MultipliedImg[MultipliedImg > 255] = 255
        return MultipliedImg

    def mergeImg2onImg1WhereImg1hasTempColor(img1, img2, tempColor = (0,0,0)):
        b, g, r = tempColor[0], tempColor[1], tempColor[2]
        img1[np.where(
            (img1[:, :, 0] == b) &
            (img1[:, :, 1] == g) &
            (img1[:, :, 2] == r))] = img2[np.where(
            (img1[:, :, 0] == b) &
            (img1[:, :, 1] == g) &
            (img1[:, :, 2] == r))] 
        return img1
    
    def grayToBGR(self,img):
        cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        return img
