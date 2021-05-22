import cv2
import numpy as np
import glob


class visualToolbox:

    inputFolder = "../media/"
    outputFolder = "../media/"

    def __init__(self):

        self.inputFolder = ""
        self.outputFolder = ""

        monalisa_newsize = (600, 480)

    def removeColor(img, colorB, colorG, colorR, tellorance):

        Height, Width, Layers = img.shape

        img[colorB-tellorance < np.where((img[:, :, 0] < colorB + tellorance) &
                                         (img[:, :, 1] < tellorance) & (img[:, :, 2] < tellorance))] = [0, 0, 0]
        img[colorB-tellorance < np.where((img[:, :, 0] < tellorance) &
                                         (img[:, :, 1] < colorG + tellorance) & (img[:, :, 2] < tellorance))] = [0, 0, 0]
        img[colorB-tellorance < np.where((img[:, :, 0] < tellorance) &
                                         (img[:, :, 1] < colorR + tellorance) & (img[:, :, 2] < tellorance))] = [0, 0, 0]

        return img

    def keepColor(img, colorB, colorG, colorR, tellorance):

        img[np.where((img[:, :, 0] < tellorance) & (img[:, :, 1] < tellorance) & (
            img[:, :, 2] < tellorance))] = [colorB, colorG, colorR]

        return img
