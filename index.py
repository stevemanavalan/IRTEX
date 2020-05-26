# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:36:34 2020

@author: steve

Execute -> python index.py --dataset dataset --index index.csv
"""


# import the necessary packages
from segment.Segmentation import Segmentation
import glob
import cv2
import argparse
import os
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
     help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
     help = "Path to the directory that contains the images to be indexed")
args = vars(ap.parse_args())
# initialize the Segmentation class
cd = Segmentation()
# open the output index file for writing
output = open(args["index"], "w")
i =0
#os.mkdir('segmentresult') #uncomment if the segmented results needs to be stored in a folder in current working directory
print("##################################### Begin Indexing #####################################")
for imagePath in glob.glob(args["dataset"] + "/*.png"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    i+= 1
    imageID = imagePath[imagePath.rfind("/") + 1:]
    print("Indexing file : {}. {}".format(i,imageID))
    imageID_1 = imagePath[imagePath.rfind("/")+ 9:]
    image = cv2.imread(imagePath)
    # describe the image
    imgfg,imgbg,outline, features = cd.segment(image)  
    # save the foreground background and the outline of the image
# =================================uncomment if segmented results needs to be stored============================================
    #cv2.imwrite(os.getcwd() + "/segmentresult/{}fg".format(imageID_1.split(".")[0]) +".png",imgfg)
    #cv2.imwrite(os.getcwd() + "/segmentresult/{}bg".format(imageID_1.split(".")[0]) +".png",imgbg)
    #cv2.imwrite(os.getcwd() + "/segmentresult/{}outline".format(imageID_1.split(".")[0]) +".png",outline)
# =================================uncomment if segmented results needs to be stored============================================
    # write the features to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))
    # close the index file
print("##################################### End Indexing #####################################")
output.close()

