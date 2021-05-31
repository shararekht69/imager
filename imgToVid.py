############# imports: #################

import cv2
import numpy as np
import glob
import moviepy.editor as mpe


print("starting sth great..")

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

        for i in range(1, numberOfFrames+1):
            print(i, str_imagesFolderAdress + str(i) + '.jpg')
            img = cv2.imread(str_imagesFolderAdress + str(i) + '.jpg')

            height, width, layers = img.shape
            img_array.append(img)
            size = (1280, 720)
        print("creating film "+str(n)+" file...")
        out = cv2.VideoWriter(str_destAdress + '.mp4',
                              cv2.VideoWriter_fourcc(*'mp4v'), 5, size)

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

        print("film "+str(n)+" file saved.")

    print("merging videos..")

    return out

# ------------------- CODE: -----------------------


# C: \Users\sharareh\Desktop\code python 3.7.9\project\multiply image\multiply image sample\final-images
mergedImagesFolderAddress = "rewrite/media/imgs/image"
destAddress = "rewrite/media/vids/output_dance_18000_10fs"
int_videoNumberin30secPieces = 1
finalclip = func_imagesToVideo(
    int_videoNumberin30secPieces, mergedImagesFolderAddress, destAddress)
