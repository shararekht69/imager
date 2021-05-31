import cv2
import numpy as np

from scipy.spatial import Delaunay
import random
from numpy.random import default_rng



class tools:

    inputFolder = ""
    outputFolder = ""
    size = (0,0)

    def __init__(self, size=(600, 480), inputFolder="rewrite/media/", outputFolder="rewrite/media/"):

        self.inputFolder = inputFolder
        self.outputFolder = outputFolder
        self.size = size

    def changeColorToTempColor(self, img, tellorance, color = (0,0,0), mode = "rgb", tempColor = (0,0,0)):
        b, g, r = color[0], color[1], color[2]
        if mode == "rgb":
            img[np.where(
                ((b - tellorance < img[:, :, 0]) & (img[:, :, 0]< b + tellorance)) &
                ((g - tellorance < img[:, :, 1]) & (img[:, :, 1]< g + tellorance)) &
                ((r - tellorance < img[:, :, 2]) & (img[:, :, 2]< r + tellorance)) )] = tempColor
        elif mode == "distance":
            img = np.reshape(img, [img.shape[0]*img.shape[1],3])
            print("reshaped",img)
            img[np.where(
                (((b - img[:, :, 0])**2) +
                ((g - img[:, :, 1])**2) +
                ((r - img[:, :, 2])**2)) < tellorance)] = tempColor

        
        return img

    def addImgs(self, img1, img2,w1=1, w2=1):
            addedImg = cv2.add(img1*w1, img2*w2)//(w1+w2)
            addedImg[addedImg > 255] = 255
            return addedImg

    def multipyImgs(self, img1, img2,w1=1, w2=1):
        MultipliedImg = np.multiply(img1*w1, img2*w2)//(w1+w2)
        MultipliedImg[MultipliedImg > 255] = 255
        return MultipliedImg

    def mergeImg2onImg1WhereImg1hasTempColor(self, img1, img2, tempColor = (0,0,0)):
        b, g, r = tempColor[0], tempColor[1], tempColor[2]
        img1[np.where(
            (img1[:, :, 0] == b) &
            (img1[:, :, 1] == g) &
            (img1[:, :, 2] == r))] = img2[np.where(
            (img1[:, :, 0] == b) &
            (img1[:, :, 1] == g) &
            (img1[:, :, 2] == r))] 
        return img1
    
    def grayToBGR(self,img):
        cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        return img

    

    def delaunay_effect(self, img, tri_num=25000):
        rows, cols, *v = img.shape
        #print(rows,cols)
        
        points_rows = np.random.randint(0, rows, tri_num)
        points_cols = np.random.randint(0, cols, tri_num)

        points = np.zeros((tri_num,2)) 
        points[:,0] = points_rows
        points[:,1] = points_cols
        #print(points)

        tri = Delaunay(points)
        #print(tri.simplices)
        ###draw
        canvas = np.ones((rows,cols,3)) #* 255
        #canvas = canvas.astype(np.float32)

        for i in range(len(tri.simplices)):
            #print(points[tri.simplices[i][0]][0])
            penSize = random.randint(1,1)
            pt0 = (int(points[tri.simplices[i][0]][1]),int(points[tri.simplices[i][0]][0]))
            pt1 = (int(points[tri.simplices[i][1]][1]),int(points[tri.simplices[i][1]][0]))
            pt2 = (int(points[tri.simplices[i][2]][1]),int(points[tri.simplices[i][2]][0]))
            if random.randint(1,2) == 1:
                canvas[pt0[1]:pt2[1],pt0[0]:pt2[0]] = img[pt1[1],pt1[0]]
            start_point = pt0#(int(points[tri.simplices[i][0]][1]),int(points[tri.simplices[i][0]][0]))
            end_point = pt1#(int(points[tri.simplices[i][1]][1]),int(points[tri.simplices[i][1]][0]))
            color = img[end_point[1],end_point[0]]
            color = (int(color[0]),int(color[1]),int(color[2]))
            canvas = cv2.line(canvas, start_point, end_point, color, penSize)
            #canvas = cv2.circle(canvas, end_point, 3, color, -1)
            start_point = pt1#(int(points[tri.simplices[i][1]][1]),int(points[tri.simplices[i][1]][0]))
            end_point = pt2#(int(points[tri.simplices[i][2]][1]),int(points[tri.simplices[i][2]][0]))
            color = img[end_point[1],end_point[0]]
            color = (int(color[0]),int(color[1]),int(color[2]))
            canvas = cv2.line(canvas, start_point, end_point,color, penSize)
            start_point = pt2#(int(points[tri.simplices[i][2]][1]),int(points[tri.simplices[i][2]][0]))
            end_point = pt0#(int(points[tri.simplices[i][0]][1]),int(points[tri.simplices[i][0]][0]))
            color = img[end_point[1],end_point[0]]
            color = (int(color[0]),int(color[1]),int(color[2]))
            canvas = cv2.line(canvas, start_point, end_point, color, penSize)
        #cv2.imwrite("out_.jpg", canvas)
        return canvas

    def rectangular_effect(self,img,img_averaged, box_num=200):
        rows, cols, *v = img.shape
        img_gray =  np.ones((rows,cols))
        
        img_gray[:,:] = (img[:,:,0]+img[:,:,1]+img[:,:,2])//3
        img_gray = img_gray.astype(np.int)
        img_gray = img_gray-img_averaged//2
        indexes = np.where(img_gray<0)
        img_gray[indexes] = 0
        canvas = np.ones((rows,cols,3)) * 255

        rng = default_rng()
        points_rows = rng.choice(rows, size=box_num, replace=False)
        points_cols = rng.choice(cols, size=box_num, replace=False)
        points = np.zeros((box_num,2))
        points = points.astype(np.int)
        points[:,0] = np.sort(points_rows)
        points[:,1] = np.sort(points_cols)
        max_gray_color = np.max(img_gray)
        for i in range(1,box_num):
            for j in range(1,box_num):
                box = img_gray[points[i-1][0]:points[i][0],points[j-1][1]:points[j][1]]

                color_avg = np.average(box)
                #print(color_avg)
                if color_avg<max_gray_color*1/3:
                    color = (color_avg*102//255, color_avg*209//255, color_avg*250//255)
                    brightness_ratio =  255//max(color)
                    color = (color[0]*brightness_ratio,color[1]*brightness_ratio,color[2]*brightness_ratio)
                    canvas[points[i-1][0]:points[i][0],points[j-1][1]:points[j][1]] = color
                #elif color_avg<max_gray_color*2/3:
                #    color = (color_avg*160//255, color_avg*214//255, color_avg*6//255)
                #    brightness_ratio =  255//max(color)
                #    color = (color[0]*brightness_ratio,color[1]*brightness_ratio,color[2]*brightness_ratio)
                #    canvas[points[i-1][0]:points[i][0],points[j-1][1]:points[j][1]] = color
                #elif color_avg<max_gray_color*3/3:
                #    color = (color_avg*180//255, color_avg*140//255, color_avg*19//255)
                #    brightness_ratio =  255//max(color)
                #    color = (color[0]*brightness_ratio,color[1]*brightness_ratio,color[2]*brightness_ratio)
                #    canvas[points[i-1][0]:points[i][0],points[j-1][1]:points[j][1]] = color
                elif color_avg<max_gray_color*2/3:
                    color = (color_avg*76//255, color_avg*60//255, color_avg*7//255)
                    brightness_ratio =  255//max(color)
                    color = (color[0]*brightness_ratio,color[1]*brightness_ratio,color[2]*brightness_ratio)
                    canvas[points[i-1][0]:points[i][0],points[j-1][1]:points[j][1]] = color
                elif color_avg<max_gray_color*3/3:
                    color = (color_avg*111//255, color_avg*71//250, color_avg*102//255)
                    brightness_ratio =  255//max(color)
                    color = (color[0]*brightness_ratio,color[1]*brightness_ratio,color[2]*brightness_ratio)
                    canvas[points[i-1][0]:points[i][0],points[j-1][1]:points[j][1]] = color
                  
        return canvas


    def circular_effect(self,img, box_num=200):
        rows, cols, *v = img.shape
        img_gray =  np.ones((rows,cols))
        
        img_gray[:,:] = (img[:,:,0]+img[:,:,1]+img[:,:,2])//3
        img_gray = img_gray.astype(np.int)
        #print(img_gray)
        canvas = np.ones((rows,cols,3)) * 255
        #points_rows = np.random.randint(0, rows, box_num) 
        #points_cols = np.random.randint(0, cols, box_num)
        rng = default_rng()
        points_rows = rng.choice(rows, size=box_num, replace=False)
        points_cols = rng.choice(cols, size=box_num, replace=False)
        points = np.zeros((box_num,2))
        points = points.astype(np.int)
        points[:,0] = np.sort(points_rows)
        points[:,1] = np.sort(points_cols)
        #print(img)
        #print(points)
        for i in range(1,box_num):
            for j in range(1,box_num):
                box = img_gray[points[i-1][0]:points[i][0],points[j-1][1]:points[j][1]]
                
                ##print(box.size)
                color_avg = np.average(box)
                #ratio = int(box.size * color_avg/255)
                #color_choices = [(color_avg,0,0),(0,color_avg,0),(0,0,color_avg)]
                canvas[points[i-1][0]:points[i][0],points[j-1][1]:points[j][1]] = (color_avg,color_avg,color_avg)
                ##dot:

                #cols, rows = box.shape
                #for m in range(points[i-1][0],rows):
                #    for n in range(points[j-1][1],cols):
                #        rand = random.randint(0,box.size) 
                #        #print(box.size,rand, ratio)
                #        #if  rand< ratio:
                #        canvas[points[i-1+m][0],points[j-1+n][1]] = 0
                    



                #circle:
                #(x,y) = ((points[i-1][0]+points[i][0]//2),(points[j-1][1]+points[j][1])//2)
                #(w,h) = (points[i][0]-points[i-1][0],points[j][1]-points[j-1][1])
                #canvas = cv2.circle(canvas,(x,y), min(w,h),color_avg, -1)       
        return canvas
