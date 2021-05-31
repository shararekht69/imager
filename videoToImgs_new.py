############ imports: #################

import cv2

############### Functions: ######################


def func_videoToImage(vidcap, str_destAdress, sec, count):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    builtFrames, image = vidcap.read()

    if builtFrames:
        image = cv2.resize(image, (1280,720))
        cv2.imwrite(str_destAdress +
                    str(count) + ".jpg", image)  # save frame as JPG file

    return builtFrames


################# Code: ########################

str_videoAdress = 'rewrite/media/vids/dance.mp4'
vidcap = cv2.VideoCapture(str_videoAdress)

str_destAdress = "rewrite/media/vids/dance/image"
sec = 1
# 610
frameRate = 0.8  # //it will capture image in each 0.5 second
count = 1

builtFrames = func_videoToImage(vidcap, str_destAdress, sec, count)
while True:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    builtFrames = func_videoToImage(vidcap, str_destAdress, sec, count)
