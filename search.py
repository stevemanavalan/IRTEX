# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:49:48 2020

@author: steve

execute ->  python search.py  --index index.csv --query query/2009_000012.jpg --result pascal2009
"""

# import the necessary packages
from segment.Segmentation import Segmentation
from segment.Searcherdf import Searcherdf
import argparse
import cv2
import os
import shutil
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
if not os.path.exists('queryresult'):
    os.mkdir('queryresult') #uncomment if the segmented results needs to be stored in a folder in current working directory
else:
    shutil.rmtree('queryresult')           # Removes all the subdirectories!
    os.makedirs('queryresult')
query = cv2.imread(args["query"])
#################################################################### F2 SIM SCORE ###########################################
searcherdf = Searcherdf(args["index"])
##############################################################################################################################
results = searcherdf.search(args["query"])
i =0
# loop over the results
for (resultID,score) in results.items():
    i+=1
    # load the result image and display it
    print(score, resultID)
    result = cv2.imread("pascal2009\{}".format(resultID))
    cv2.imwrite(os.getcwd() + "/queryresult/{}_{}".format(i,(resultID.split(".")[0]) +".png"),result)