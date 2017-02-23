##  Made by Gerardo Uranga ##
##  guranga@miners.utep.edu ##
##  Last Modified: 2/22/2017 ##
##                           ##
##  Small script to place images in folders of the user's choice. ##
##  Runs from command line. To change, simply uncomment direc and output to ##
##  suit your needs. ##

import os, sys
import shutil
import cv2
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Import Variable Meanings:
# direc = input directory
# output = output directory
# trash = trash folder directory
# image_folder = input directory: name used so for loops are easier to understand
# folder_names[] = list of folder names that contain the names corresponding to command line inputs
# image_direcs[] = list of file names inside the folders of the image folders
# image_files[] = list of images file names
# j = used to iterate through image_direcs and in the while loop
# new_direc = updated directory of the image after being moved. 
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#direc = 'your\\directory\\here'
direc = sys.argv[1]
#output = 'your\\directory\\here'
output = sys.argv[2]
trash = output+'\\'+"trash"
if not (os.path.exists(trash)):
    os.makedirs(trash)
image_folder = os.listdir(direc)
folder_names = []
image_direcs = []
image_files = []
j = 0

for i in range(0,len(sys.argv)-3):
    folder_names.append(sys.argv[i+3])
    if not (os.path.exists(output + '\\' + folder_names[-1])):
        os.makedirs(output+'\\'+folder_names[-1])

for folders in image_folder:
    file_direc = (direc + '\\' + folders)
    for fil in os.listdir(file_direc):
        image_direcs.append(file_direc +'\\' + fil)
        image_files.append(fil)
    while (j < len(image_direcs)):
        image = cv2.imread(image_direcs[j])
        cv2.imshow("",image)
        key = cv2.waitKey()
        while (key == 117 and j > 0): #undo key
            j = j-1
            image = cv2.imread(image_direcs[j])
            cv2.imshow("",image)
            key = cv2.waitKey()
        if (key == 100): # delete key
            new_direc = trash + '\\' + image_files[j] 
            try:
                shutil.move(image_direcs[j], trash)
            except:
                pass
        else :
            new_direc = output + '\\' + folder_names[int(chr(key))-1] + '\\' + image_files[j]
            try:
                shutil.move(image_direcs[j], output +'\\' + folder_names[int(chr(key))-1])
            except: #done to ignore repetition
                pass
        image_direcs[j] = new_direc
        j += 1
os.rmdir(trash)
