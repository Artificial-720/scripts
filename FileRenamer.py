# Python script to rename multiple  
# files in a directory
# To use:
# - change source var to intended directory
# - update renamer function rename file to intended layout
#
# Example:
# file structure
# exampledir\
#   75849203.png
#   83754902.png
#
# file structure after running example code
# exampledir\
#   image 1.png
#   image 2.png

import os

#source = "C:\\exampledir\\"
source = "C:\\exampledir\\"

#builds new name for a file
#   count - int current count from list of files in directory
#   filename - string filename before it is changed
# returns - string containing new filename
def renamer(count, filename):
    #Change this function
    #make sure to have correct file extention ie ".exe, .png"
    tmp = "image " + str(count + 1) + ".png"
    return tmp



#loop over all files in directory calling renamer on each
for count, filename in enumerate(os.listdir(source)):
    dst = renamer(count, filename)
    #adds file path and renames
    src = source + filename
    dst = source + dst
    os.rename(src, dst)
