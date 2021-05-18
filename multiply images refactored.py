import cv2
import numpy as np
import glob


# ---------------- FUNCTION: -----------------------

def func_sizeChanging(image, x, dest_x, y, dest_y, mode):

    if mode == 0:  # Crop image
        changedImage = image[x:dest_x, y:dest_y]
        changedImage.astype(np.float16)

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


def func_preprocessingImage(image):
    height, width, layer = image.shape

    for i in range(height):
        for j in range(width):
            if (((image[i, j][0] + image[i, j][1] + image[i, j][2])/3) < 5):
                image[i, j][0] = 0
                image[i, j][1] = 0
                image[i, j][2] = 0
    '''
    for i in range(270, 360):
        for j in range(300, 450):
            image[i, j][0] = 0
            image[i, j][1] = 0
            image[i, j][2] = 0
    '''
    return image


def func_isBlack(pixel, tellorance):
    if ((pixel[0] + pixel[1] + pixel[2])/3) >= tellorance:
        return True

    else:
        return False


def func_mergingImages(image1, image2):
    image1Hight, image1Width, image1Layar = image1.shape
    colorfulEdgesImg = np.ones([image1Hight, image1Width, 3])
    for i in range(30, image1Hight-30):
        for j in range(35, image1Width-35):
            if image2[i-29, j-34] == 255:
                colorfulEdgesImg[i, j] = [1, 10, 10]

    finalImg = np.multiply(colorfulEdgesImg, image1)

    return finalImg

# --------------------- CODE: ------------------------------


moonFolderImagesAddress = "C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/moon-images/image"
monalisaFolderImagesAddress = "C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/monalisa-images/image"
resizedMoonFolderAddress = "C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/resized-moon-images2/image"
mergedImagesFolderAddress = "C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/merged-images3/image"
resizedMonalisaFolderAddress = "C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/resized-monalisa/image"
illusionFolderImagesAddress = "C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/illusion-Images/image"
resizedIllusionAddress = "C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/resized-illusion-images/image"
finalImage = "C:/Users/sharareh/Desktop/code python 3.7.9/project/multiply image/final-images2/image"

moonFileNameArray = glob.glob(moonFolderImagesAddress + '*.jpg')
monalisaFileNameArray = glob.glob(monalisaFolderImagesAddress + '*.jpg')
illusionFileNameArray = glob.glob(illusionFolderImagesAddress + '*.jpg')

count = 1
for i in range(3):
    # reading images:
    moonImg = cv2.imread(moonFolderImagesAddress + str(i+200) + '.jpg')
    monalisaImg = cv2.imread(monalisaFolderImagesAddress + str(i+50) + '.jpg')
    illusionImg = cv2.imread(illusionFolderImagesAddress + str(i+1) + '.jpg')

    # -----getting images' shapes:
    moonHeight, moonWidth, moonLayers = moonImg.shape
    # print(moonImg.shape)
    monalisaHeight, monalisaWidth, monalisaLayer = monalisaImg.shape
    # print(monalisaImg.shape)
    illusionImageHeight, illusionImageWidth, illusionImageLayes = illusionImg.shape
    # print(illusionImg.shape)

    # -----process on moon images:
    nesbat = float(monalisaWidth/monalisaHeight)
    print(nesbat)
    croppedMoonImage = func_sizeChanging(moonImg, 1, 720, 190, 1090, 0)
    resizedMoonImage = func_sizeChanging(
        croppedMoonImage, 1, 360, 1, 450, 1)
    print(resizedMoonImage.shape)

    preprocessedMoonImg = func_preprocessingImage(resizedMoonImage)

    # -----process on monalisa images:
    #monalisaTranslated = func_transformingImage(monalisaImg, 20, 1, moonWidth, moonHeight)
    newsize = (375, 300)
    resizedMonalisaImage = cv2.resize(monalisaImg, newsize)
    edgeMonalisa = cv2.Canny(resizedMonalisaImage, 70, 120)

    monalisaTranslated = func_transformingImage(
        edgeMonalisa, 20, 1, moonWidth, moonHeight)

    mergedImg = func_mergingImages(preprocessedMoonImg, monalisaTranslated)
    #cv2.imwrite(mergedImagesFolderAddress, mergedImg)

    # -----process on illusion images:
    croppedIllusionImage = func_sizeChanging(illusionImg, 1, 360, 95, 545, 0)
    illusionImageHeight, illusionImageWidth, illusionImageLayes = croppedIllusionImage.shape
    # print(resizedIllusionImage.shape)

    for x in range(illusionImageHeight-1):
        for y in range(illusionImageWidth-1):
            # if mergedImage[x, y][0] != 0 and mergedImage[x, y][1] != 0 and mergedImage[x, y][2] != 0:
            if func_isBlack(mergedImg[x, y], 5):
                croppedIllusionImage[x, y][0] = mergedImg[x, y][0]
                croppedIllusionImage[x, y][1] = mergedImg[x, y][1]
                croppedIllusionImage[x, y][2] = mergedImg[x, y][2]

    cv2.imwrite(finalImage +
                str(i) + ".jpg", croppedIllusionImage)

    if i % 10 == 0:
        print("image " + str(i) + " saved!")
