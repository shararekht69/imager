############# imports: #################

import cv2
import numpy as np
import glob
import moviepy.editor as mpe

print("starting sth great..")
#salaaaaaaaaaaaaaaam!###
####################### Functionss: ############################


def func_imagesToVideo(int_videoNumberin30secPieces, str_imagesFolderAdress, str_destAdress):

    for n in range(int_videoNumberin30secPieces):
        img_array = []
        print("getting frame adresses")
        fileNameArray = glob.glob(str_imagesFolderAdress + '*.jpg')
        print(str_imagesFolderAdress + '*.jpg')
        # sortedFiles = sorted(fileNameArray)
        # khdoet patho besaz image+i+.jpg
        numberOfFrames = len(fileNameArray)
        print(numberOfFrames)

        for i in range(numberOfFrames):
            img = cv2.imread(str_imagesFolderAdress + str(i) + '.jpg')

            height, width, layers = img.shape
            img_array.append(img)
            size = (450, 359)
        print("creating film "+str(n)+" file...")
        out = cv2.VideoWriter(str_destAdress + '.mp4',
                              cv2.VideoWriter_fourcc(*'mp4v'), 20, size)

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

        print("film "+str(n)+" file saved.")

    print("merging videos..")

    return out

# ------------------- CODE: -----------------------


mergedImagesFolderAddress = "C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/final-Images/image"
destAddress = "C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/final video 4"
int_videoNumberin30secPieces = 1
finalclip = func_imagesToVideo(
    int_videoNumberin30secPieces, mergedImagesFolderAddress, destAddress)
