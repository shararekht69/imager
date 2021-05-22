############ imports: #################

import cv2

############### Functions: ######################


def func_videoToImage(vidcap, str_destAdress, sec, count):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    builtFrames, image = vidcap.read()

    if builtFrames:
        cv2.imwrite(str_destAdress +
                    str(count) + ".jpg", image)  # save frame as JPG file

    return builtFrames


################# Code: ########################

str_videoAdress = 'C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/image/illusion.mp4'
vidcap = cv2.VideoCapture(str_videoAdress)

str_destAdress = "../image/illusion-images2/image"
sec = 1
# 610
frameRate = 0.05  # //it will capture image in each 0.5 second
count = 1

builtFrames = func_videoToImage(vidcap, str_destAdress, sec, count)
while True:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    builtFrames = func_videoToImage(vidcap, str_destAdress, sec, count)
