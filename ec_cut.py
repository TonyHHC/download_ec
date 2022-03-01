import os
import glob
import time
import cv2
import numpy as np

def cutImage(imgName):

	imgSrcFilebasename = os.path.basename(imgName)
	imgSrcFilebasenameWithoutExt = imgSrcFilebasename.split('.')[0]
	newImageNameWithoutExt = imgSrcFilebasenameWithoutExt.zfill(4)
	
	newImgName = os.path.join('E:/Temp/EC', newImageNameWithoutExt+'.png')

	img = cv2.imread(imgName)
	
	x = 90
	y = 390
	w = 985-90+1
	h = 1545-390+1
	
	cut_img = img[y:y+h, x:x+w]
	cv2.imwrite(newImgName, cut_img)

	img = None
	cut_img = None
	
	del img
	del cut_img
	
if __name__ == "__main__":	

	#cutImage('D:/Temp/2.png')

	images = glob.glob('D:/Temp/EC/*.png')
	for eachImg in images:
		print('Cut {} ...'.format(eachImg))
		cutImage(eachImg)
