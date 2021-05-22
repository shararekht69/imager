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

    def removeColor(self, img, tellorance, color = (0,0,0)):

        #Height, Width, Layers = img.shape
        b , g, r = color[0], color[1], color[2]
        img[np.where(
            (b-tellorance < img[:, :, 0] < b + tellorance) &
            (g - tellorance <img[:, :, 1] < g + tellorance) &
            (r - tellorance < img[:, :, 2] < r + tellorance))] = [0, 0, 0]
        
        return img

    def removeAllButColor(self, img, tellorance, color = (0,0,0)):

        #Height, Width, Layers = img.shape
        b , g, r = color[0], color[1], color[2]
        img[np.where(
            ((b-tellorance > img[:, :, 0]) | ( img[:, :, 0] > b + tellorance)) &
            ((g-tellorance > img[:, :, 0]) | ( img[:, :, 0] > g + tellorance)) &
            ((r-tellorance > img[:, :, 0]) | ( img[:, :, 0] > r + tellorance)) )] = [0,0,0]
            
        return img
