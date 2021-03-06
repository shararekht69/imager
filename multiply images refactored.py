import cv2
import numpy as np
import glob
from datetime import datetime

# ---------------- FUNCTION: -----------------------


def func_sizeChanging(image, x, dest_x, y, dest_y, mode):

    if mode == 0:  # Crop imagea=ghghhghg
        changedImage = image[x:dest_x, y:dest_y]
        # changedImage.astype(np.float16)

    elif mode == 1:  # resize image for given mode
        dsize = (dest_x, dest_y)
        changedImage = cv2.resize(image, dsize)

    return changedImage


def func_transformingImage(image, x, y, dest_y, dest_x):

    # Creating a translation matrix
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])

    # Image translation
    TranslatedImage = cv2.warpAffine(
        image, translation_matrix, (dest_y, dest_x))

    return TranslatedImage


def func_isBlack(pixel, tellorance):
    # @Shery: it should be <= tellorance because in grayscale 0 means black, 255 means white
    # if ((pixel[0] + pixel[1] + pixel[2])/3) <= tellorance:
    if pixel[0] <= tellorance and pixel[1] <= tellorance and pixel[2] <= tellorance:
        return True

    else:
        return False


def func_preprocessingImage(image):
    height, width, layer = image.shape

    # for i in range(height):
    #    for j in range(width):
    #        if func_isBlack(image[i, j], 30):
    #            image[i, j][0] = 0
    #            image[i, j][1] = 0
    #            image[i, j][2] = 0
    image[np.where((image[:, :, 0] < 30) & (image[:, :, 1] < 30)
                   & (image[:, :, 2] < 30))] = [0, 0, 0]

    # removing watermarks and white written info at the bottom of image
    # for i in range(270, 360):
    #    for j in range(300, 450):
    #        image[i, j][0] = 0
    #        image[i, j][1] = 0
    #        image[i, j][2] = 0
    #image[270:360, 300:450] = np.zeros([360-270, 450-300, 3])
    image[600:680, 800:1280] = np.zeros([680-600, 1280-800, 3])

    return image


def func_mergingImages(image1, image2):
    image1Hight, image1Width, image1Layar = image1.shape
    colorfulEdgesImg = np.ones([image1Hight, image1Width, 3])
    # for i in range(image1Hight):
    #    for j in range(image1Width):
    #        if image2[i, j] == 255:
    #            colorfulEdgesImg[i, j] = [200, 200, 200]

    colorfulEdgesImg[np.where(image2 == 255)] = [200, 200, 200]

    colorfulEdgesImg
    finalImg = np.multiply(colorfulEdgesImg, image1)
    finalImg[finalImg > 255] = 255
    return finalImg


# --------------------- CODE: ------------------------------

moonFolderImagesAddress = "../image/moon-images/image"
monalisaFolderImagesAddress = "../image/monalisa-images/image"
illusionFolderImagesAddress = "../image/illusion-Images2/image"
handFolderImagesAddress = "../image/hand image/image"
finalImage = "../image/final-images/image"
finalImage1 = "../image/final-images2/image"

#moonFileNameArray = glob.glob(moonFolderImagesAddress + '*.jpg')
#monalisaFileNameArray = glob.glob(monalisaFolderImagesAddress + '*.jpg')
#illusionFileNameArray = glob.glob(illusionFolderImagesAddress + '*.jpg')

count = 1
print("start time: ", datetime.time(datetime.now()))
for i in range(10):
    # reading images:
    moonImg = cv2.imread(moonFolderImagesAddress +
                         str(i+1) + '.jpg')  # U: 200
    monalisaImg = cv2.imread(
        monalisaFolderImagesAddress + str(i+434) + '.jpg')  # U:50
    illusionImg = cv2.imread(
        illusionFolderImagesAddress + str(i+1) + '.jpg')  # U:1

# -----getting images' shapes:
    moonHeight, moonWidth, moonLayers = moonImg.shape
    # print(moonImg.shape)
    monalisaHeight, monalisaWidth, monalisaLayer = monalisaImg.shape
    # print(monalisaImg.shape)
    illusionImageHeight, illusionImageWidth, illusionImageLayes = illusionImg.shape
    # print(illusionImg.shape)

# -----process on moon images:

    preprocessedMoonImg = func_preprocessingImage(moonImg)
    croppedMoonImage = None

# -----process on monalisa images:
    newsize = (600, 480)
    resizedMonalisaImage = cv2.resize(monalisaImg, newsize)
    edgeMonalisa = cv2.Canny(resizedMonalisaImage, 20, 200)
    resizedMonalisaImage = None

    monalisaTranslated = func_transformingImage(
        edgeMonalisa, 350, 130, moonWidth, moonHeight)  # 30-35
    edgeMonalisa = None
    mergedImg = func_mergingImages(preprocessedMoonImg, monalisaTranslated)
    preprocessedMoonImg = None
    monalisaTranslated = None
    #cv2.imwrite("./merged.jpg", mergedImg)
    # mergedImgHeight, mergedImgWidth, mergedImgLayers = mergedImg.shape

# -----process on illusion images:

    # for x in range(illusionImageHeight - 1):
    #    for y in range(illusionImageWidth - 1):
    #        # if mergedImage[x, y][0] != 0 and mergedImage[x, y][1] != 0 and mergedImage[x, y][2] != 0:
    #        if not (func_isBlack(mergedImg[x, y], 0)):
    #            croppedIllusionImage[x, y][0] = mergedImg[x, y][0]
    #            croppedIllusionImage[x, y][1] = mergedImg[x, y][1]
    #            croppedIllusionImage[x, y][2] = mergedImg[x, y][2]

    #np.where(not((mergedImg[:,:,0]<30) & (mergedImg[:,:,1]<30) & (mergedImg[:,:,2]<30)))
    illusionImg[np.where((mergedImg[:, :, 0] > 30) & (mergedImg[:, :, 1] > 30) & (mergedImg[:, :, 2] > 30))] = mergedImg[np.where(
        (mergedImg[:, :, 0] > 30) & (mergedImg[:, :, 1] > 30) & (mergedImg[:, :, 2] > 30))]

    mergedImg = None


# -----writing final image:
    cv2.imwrite(finalImage1 +
                str(count) + ".jpg", illusionImg)  # croppedIllusionImage)
    # if i % 10 == 0:
    #print("image " + str(count) + " saved!")

    count = count + 1

print(str(count)+" - finished: ", datetime.time(datetime.now()))


'''
# ------process on hand images:
    mergedIllusionMoon = cv2.imread(
        finalImage + str(i+2) + '.jpg')

    handImg = cv2.imread(
        handFolderImagesAddress + str(i+60) + '.jpg')

    croppedHandImage = func_sizeChanging(handImg, 0, 360, 95, 545, 0)
    handImg = None
    handImageHeight, handImageWidth, handImageLayes = croppedHandImage.shape
    # cv2.imwrite("C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/multiply image sample/illusion" + str(i) + '.jpg', croppedIllusionImage)
    # print(croppedIllusionImage.shape)

    for x in range(handImageHeight - 1):
        for y in range(handImageWidth - 1):
            # if mergedImage[x, y][0] != 0 and mergedImage[x, y][1] != 0 and mergedImage[x, y][2] != 0:
            if not (func_isBlack(croppedHandImage[x, y], 20)):
                mergedIllusionMoon[x, y][0] = (
                    1.3*mergedIllusionMoon[x, y][0] + croppedHandImage[x, y][0]) // 3
                mergedIllusionMoon[x, y][1] = (
                    1.3*mergedIllusionMoon[x, y][1] + croppedHandImage[x, y][1]) // 3
                mergedIllusionMoon[x, y][2] = (
                    1.3*mergedIllusionMoon[x, y][2] + croppedHandImage[x, y][2]) // 3

    croppedHandImage = None
'''
