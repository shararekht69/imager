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
        for i in range(Height):
            for j in range(Width):

                img[600:680, 800:1280] = np.zeros([680-600, 1280-800, 3])

                if img[i, j][0] <= tellorance and img[i, j][1] <= tellorance and img[i, j][2] <= tellorance:
                    return True

                else:
                    return False

    def keepColor(img, colorB, colorG, colorR, tellorance):

        img[np.where((img[:, :, 0] < tellorance) & (img[:, :, 1] < tellorance) & (
            img[:, :, 2] < tellorance))] = [colorB, colorG, colorR]

        return img
