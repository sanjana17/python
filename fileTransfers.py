import os
import glob
import shutil

def movefiles(type,dir,folderName):
	if(not os.path.exists(dir+'/'+folderName)):
		os.makedirs(dir+'/'+folderName)
	files = glob.glob(dir+'/*.'+type)
	for file in files:
		shutil.move(file,dir+'/'+folderName)
movefiles('doc','Downloads','hellll')
