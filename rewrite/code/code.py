import visualToolbox
import cv2
import numpy as np

tool = visualToolbox.tools()

#circular_effect
img_gray = cv2.imread(tool.inputFolder + "vids/dance/image" + str(1) + ".jpg",cv2.IMREAD_GRAYSCALE)
x,y = img_gray.shape
print(x,y)
img_average = np.zeros((720,1280), dtype=int)
c = 0
for i in range(1,30):
    img_gray =  cv2.imread(tool.inputFolder + "vids/dance/image" + str(i) + ".jpg",cv2.IMREAD_GRAYSCALE)
    #print(img_average,img_gray)
    img_average =img_average+img_gray
    c = c + 1
img_average = img_average//c
print("averaged",img_average)

for i in range(1,30):
    dance = cv2.imread(tool.inputFolder + "vids/dance/image" + str(i) + ".jpg")
    #dance = tool.circular_effect(dance,400)
    dance = tool.rectangular_effect(dance,img_average,400)
    
    cv2.imwrite(tool.outputFolder + "imgs/image" + str(i) + ".jpg", dance)
    print("created frame:", i)
#dance = cv2.imread(tool.inputFolder + "l1_0.png")#"vids/dance/image" + str(1) + ".jpg")
#dance = tool.circular_effect(dance,500)
#cv2.imwrite("circular_effect.jpg", dance)

"""
    #delaunay_effect
    for i in range(1,238):
    dance = cv2.imread(tool.inputFolder + "vids/dance/image" + str(i) + ".jpg")
    dance = tool.delaunay_effect(dance, 18000)
    cv2.imwrite(tool.outputFolder + "imgs/image" + str(i) + ".jpg", dance)
    print("created frame:", i)



    waterfall = cv2.imread(tool.inputFolder + "vids/waterfall/image" + str(i) + ".jpg")
    robot = cv2.imread(tool.inputFolder + "vids/robot/image" + str(i) + ".jpg")
    fractal = cv2.imread(tool.inputFolder + "vids/fractal/image" + str(i) + ".jpg")
    deepdream = cv2.imread(tool.inputFolder + "vids/deepdream/image" + str(i) + ".jpg")
    
    story = cv2.blur(story,(3,3))
    story = tool.changeColorToTempColor(story,20,(40,50,60), "rgb")
    story = tool.mergeImg2onImg1WhereImg1hasTempColor(story, deepdream)

    story = tool.changeColorToTempColor(story,30,(120,125,125), "rgb")
    story = tool.mergeImg2onImg1WhereImg1hasTempColor(story, waterfall)
    story = tool.changeColorToTempColor(story,30,(80,90,100), "rgb")
    story = tool.mergeImg2onImg1WhereImg1hasTempColor(story, waterfall)

    story = tool.changeColorToTempColor(story,20,(230,230,230), "rgb")
    story = tool.mergeImg2onImg1WhereImg1hasTempColor(story, waterfall)

    story = tool.changeColorToTempColor(story,20,(10,10,10), "rgb")
    story = tool.mergeImg2onImg1WhereImg1hasTempColor(story, fractal)
    story = tool.changeColorToTempColor(story,20,(30,30,30), "rgb")
    story = tool.mergeImg2onImg1WhereImg1hasTempColor(story, fractal)


    cv2.imwrite(tool.outputFolder + "imgs/image" + str(i) + ".jpg", story)
    print("created frame:", i) 
"""