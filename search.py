# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:49:48 2020

@author: steve

execute ->  python search.py  --index index.csv --query query/9896_bird.png --result dataset
"""

# import the necessary packages
from segment.Segmentation import Segmentation
from segment.searcher import Searcher
import argparse
import cv2
import os
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
os.mkdir('queryresult') #uncomment if the segmented results needs to be stored in a folder in current working directory
# initialize the image descriptor class
cd = Segmentation()
# load the query image and describe it
query = cv2.imread(args["query"])
imgfg, imgbg, saliencymap, features = cd.segment(query)
# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
# display the query
cv2.namedWindow('Query', cv2.WINDOW_NORMAL)
cv2.imshow("Query", query)
cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
i =0
# loop over the results
for (score, resultID) in results:
    i+=1
    # load the result image and display it
    print(score, resultID)
    result = cv2.imread(resultID)
    #comment if the query results needs not be stored in a folder in current working directory
    cv2.imwrite(os.getcwd() + "/queryresult/{}_{}".format(i,(resultID.split('\\')[1]).split(".")[0]) +".png",result)
    cv2.imshow("Result", result)
    cv2.waitKey(0)

