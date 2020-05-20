from PIL import Image
import glob
import numpy as np
import os
import csv

# %%

data_dir = "/home/dr1/sds_hd/sd18a006/DataBaseCRCProjekt/Daniel/GroundTruth/exported_tiles"
Dataset = "TO58492_97"
pngPath = os.path.join(data_dir,Dataset,"*.png")
FileList = []

# open existing Filelist and read the content in a list
with open(os.path.join(data_dir,"Filelist.txt"), 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        # add item to the list
        FileList.append(currentPlace)

# append new Files to FileList
for image_path in glob.glob(pngPath):
     FileList.append(os.path.basename(image_path)[:-11])

#save new Filelist
with open(os.path.join(data_dir,"Filelist.txt"), 'w') as filehandle:
    for listitem in FileList:
        filehandle.write('%s\n' % listitem)