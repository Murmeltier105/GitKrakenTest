from sklearn.model_selection import train_test_split
import os
import numpy as np
import glob

data_dir = "/home/dr1/sds_hd/sd18a006/DataBaseCRCProjekt/Daniel/GroundTruth/exported_tiles"
Dataset = "TO58492_97"
pngPath = os.path.join(data_dir,Dataset,"*.png")
FileList = []

# open existing Filelist and read the content in a list
if os.path.exists(os.path.join(data_dir, 'Filelist.txt')):
    with open(os.path.join(data_dir,"Filelist.txt"), 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            FileList.append(currentPlace)

# append new Files to FileList
for image_path in glob.glob(pngPath):
     FileList.append(os.path.basename(image_path)[:-11])

FileList = np.unique(FileList)

#save new Filelist
with open(os.path.join(data_dir,"Filelist.txt"), 'w') as filehandle:
    for listitem in FileList:
        filehandle.write('%s\n' % listitem)

#split Filelist in train and test
train_id, test_id = train_test_split(FileList, test_size=0.2, random_state=1)

#split train set in train and val
train_id, val_id  = train_test_split(train_id, test_size=0.25, random_state=1) # 0.25 x 0.8 = 0.2

#save lists
with open(os.path.join(data_dir,"train.txt"), 'w') as filehandle:
    for listitem in train_id:
        filehandle.write('%s\n' % listitem)

with open(os.path.join(data_dir,"val.txt"), 'w') as filehandle:
    for listitem in val_id:
        filehandle.write('%s\n' % listitem)

with open(os.path.join(data_dir,"test.txt"), 'w') as filehandle:
    for listitem in test_id:
        filehandle.write('%s\n' % listitem)