# =。= coding: utf-8 =。=
#---------------------------------------
#author:YoungPen
#version:0.1
#description:把微软聚焦的壁纸复制出来到指定目录，地址目前是写死的，
#---------------------------------------
import os 
import os.path 
import shutil 
import time
from PIL import Image

def getCurTime(): 
	nowTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	return nowTime


def copyFiles(sourceDir,targetDir): 
	for file in os.listdir(sourceDir): 
		sourceFile = os.path.join(sourceDir,  file) 
		targetFile = os.path.join(targetDir,  file) 
		if os.path.isfile(sourceFile): 	
			if not os.path.exists(targetDir):  
				os.makedirs(targetDir)  
			if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
					open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
		if os.path.isdir(sourceFile): 
			First_Directory = False 
			copyFiles(sourceFile, targetFile)

			
def rename(sourceDir):
	for file in os.listdir(sourceDir):
		fileimg=os.path.join(sourceDir,file)
		if os.path.isfile(fileimg)==True:
			if file.find('.')<0:
				newname=file+'.jpg'
				filetemp=os.path.join(sourceDir,newname)
				if os.path.exists(filetemp)==True:
					print('文件已存在，删除！')
					os.remove(filetemp)
				os.rename(fileimg,filetemp)


def remove(sourceDir):
	for file in os.listdir(sourceDir):
		fileimg=os.path.join(sourceDir,file)
		if os.path.isfile(fileimg)==True:
			print(fileimg)
			if os.path.getsize(fileimg)<300000:
				print('文件小于300kb，目测非图片，已经删除')
				os.remove(fileimg)
#这里因为image对象有open方法，没有close方法，采用二进制读写模式打开获取然后close
			else:
				fp = open(fileimg,'rb')
				img=Image.open(fp)
				fp.close()
				imgSize = img.size
				print(imgSize)
				if imgSize != (1920,1080):
					print('图片尺寸非1920*1080，不是需要的壁纸，删除！')
					os.remove(fileimg)


def moveimg(nowTime,sourceDir):
	newDir=os.path.join(sourceDir,nowTime)
	filenum=-1
	print(newDir)
	if os.path.exists(newDir)==False:
		os.makedirs(newDir)
	for file in os.listdir(sourceDir):
		oldImg=os.path.join(sourceDir,file)
		filenum=filenum+1
		try:
			shutil.move(oldImg,newDir)
		except:
			print('文件可能已经存在');
			os.remove(oldImg)
			pass
	print('总共'+str(filenum)+'张图片')

if __name__ == '__main__':
	formatTime = getCurTime()
	source_File_Path = "C:\\Users\\Xey\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets" 
	wallpaper_File_Path = "D:\\temp\\wallpaper" 
	print (formatTime)
	print ('正在复制今日微软聚焦图片文件')
	copyFiles(source_File_Path, wallpaper_File_Path)
	print ('开始重命名图片文件')
	rename(wallpaper_File_Path)
	print('开始筛选文件')
	remove(wallpaper_File_Path)
	print('建立文件夹并转移')
	moveimg(formatTime,wallpaper_File_Path)
	print ('任务完成！')
	