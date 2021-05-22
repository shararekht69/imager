from typing import final
import visualToolbox
import cv2
import numpy as np

tool = visualToolbox.tools()

layer0_img = cv2.imread(tool.inputFolder + "l0_" + str(0) + ".png") 
layer1_img = cv2.imread(tool.inputFolder + "l1_" + str(0) + ".png") 
layer2_img = cv2.imread(tool.inputFolder + "l2_" + str(0) + ".png") 
layer3_img = cv2.imread(tool.inputFolder + "l3_" + str(0) + ".png") 
layer4_img = cv2.imread(tool.inputFolder + "l4_" + str(0) + ".png") 
print(tool.inputFolder + "l0_" + str(0) + ".png")
#(self, img, tellorance, color = (0,0,0), tempColor = (0,0,0)):
image = tool.changeColorToTempColor(layer1_img,50,(50,90,150), "rgb")
image = tool.mergeImg2onImg1WhereImg1hasTempColor(image, layer2_img)

image = tool.changeColorToTempColor(image,50,(0,0,100), "rgb")
image = tool.mergeImg2onImg1WhereImg1hasTempColor(image, layer3_img)

image = tool.changeColorToTempColor(image,50,(230,230,230), "rgb")
image = tool.mergeImg2onImg1WhereImg1hasTempColor(image, layer0_img)

image = tool.changeColorToTempColor(image,50,(140,150,170), "rgb")
image = tool.mergeImg2onImg1WhereImg1hasTempColor(image, layer4_img)



cv2.imwrite(tool.outputFolder + "l_final_" + str(0) + ".jpg", image) 