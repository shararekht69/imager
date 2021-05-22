import cv2
import numpy as np
import glob


class visualToolbox:

    inputFolder = ""
    outputFolder = ""
    sizeX = 0
    sizeY = 0

    def __init__(self, size=(600,480) , inputFolder = "../media/", outputFolder = "../media/"):

        self.inputFolder = inputFolder
        self.outputFolder = outputFolder
        self.sizeX = size[0]
        self.sizeY = size[1] 
        #monalisa_newsize = (600, 480)

    def removeColor(img, tellorance, color = (0,0,0)):

        #Height, Width, Layers = img.shape
        b , g, r = color[0], color[1], color[2]
        img[b-tellorance < np.where((img[:, :, 0] < b + tellorance) & (g - tellorance <img[:, :, 1] < g + tellorance) & (r - tellorance < img[:, :, 2] < r + tellorance))] = [0, 0, 0]
        
        return img

    def keepColor(img, colorB, colorG, colorR, tellorance):

        img[np.where((img[:, :, 0] < tellorance) & (img[:, :, 1] < tellorance) & (
            img[:, :, 2] < tellorance))] = [colorB, colorG, colorR]

        return img
