# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:36:34 2020

@author: steve

Execute -> python index.py --dataset pascal2009  --index index.csv
"""


# import the necessary packages
from segment.Segmentation import Segmentation
from segment.colorpicker import colorpicker
import glob
import cv2
import argparse
import os
import shutil
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import extcolors
import webcolors

import pickle


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
     help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
     help = "Path to the directory that contains the images to be indexed")
args = vars(ap.parse_args())
# initialize the Segmentation class
cd = Segmentation()
cp = colorpicker()
# open the output index file for writing
output = open(args["index"], "w")
i =0
if not os.path.exists('segmentresult'):
    os.mkdir('segmentresult') #uncomment if the segmented results needs to be stored in a folder in current working directory
else:
    shutil.rmtree('segmentresult')           # Removes all the subdirectories!
    os.makedirs('segmentresult')
print("##################################### Begin Indexing #####################################")
data = []
# load the model from disk
loaded_model = pickle.load(open("rf_pascal_pattern.sav", 'rb'))
for imagePath in glob.glob(args["dataset"] + "/*"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    i+= 1
    path = os.path.basename(imagePath)
    imageID = imagePath[imagePath.rfind("/") + 1:]
    print("Indexing file : {}. {}".format(i,path))
    imageID_1 = imagePath[imagePath.rfind("/")+ 12:]
    print(imageID_1)
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (64, 64)) 
    # describe the image
    imgfg,imgbg,outline,texture, features = cd.segment(image,imageID_1,loaded_model)  
          
    # =============================================================================
    colorsfg, pixel_countfg = extcolors.extract(os.getcwd() + "/segmentresult/{}fg".format(imageID_1.split(".")[0]) +".jpg")
    try:
        closest_name_fg = webcolors.rgb_to_name(colorsfg[1][0])  
    except ValueError:
        closest_name_fg = closest_colour(colorsfg[1][0])
        colorsbg, pixel_countbg = extcolors.extract(os.getcwd() + "/segmentresult/{}bg".format(imageID_1.split(".")[0]) +".jpg")
    try:
        closest_name_bg = webcolors.rgb_to_name(colorsbg[0][0])  
    except ValueError:
        closest_name_bg = closest_colour(colorsbg[0][0])
    # =============================================================================
    closest_hue_fg = cp.name2hue(webcolors.name_to_hex(closest_name_fg).upper())
    closest_hue_bg = cp.name2hue(webcolors.name_to_hex(closest_name_bg).upper())
    ################################################################### Texture Classifier ##################################
    # write the features to file
    features = [str(f) for f in features]
    features.append(closest_name_fg)
    features.append(closest_name_bg)
    features.append(closest_hue_fg)
    features.append(closest_hue_bg)
    features.append(texture)
    data.append("%s,%s\n" % (path, ",".join(features)))
    output.write("%s,%s\n" % (path, ",".join(features)))
    # close the index file
print("##################################### End Indexing #####################################")
#result = pd.DataFrame(data)
#result.to_csv(args["index"], index=False, header=False, delimiter=',', encoding= "utf-8")
#output.close()

