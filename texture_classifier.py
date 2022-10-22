# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:26:31 2020

@author: steve
"""

import cv2
import numpy as np
import os
import glob
import mahotas as mt
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from segment.LocalBinaryPatterns import LocalBinaryPatterns
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import pickle

# function to extract haralick textures from an image
def extract_features(image):
    # calculate haralick texture features for 4 types of adjacency
    textures = mt.features.haralick(image)

    # take the mean of it and return it
    ht_mean  = textures.mean(axis=0)
    return ht_mean

# load the training dataset
train_path  = "textureDataset/train"
train_names = os.listdir(train_path)

# empty list to hold feature vectors and train labels
train_features = []
train_labels   = []

# loop over the training dataset
print ("[STATUS] Started extracting haralick textures..")
for train_name in train_names:
    cur_path = train_path + "/" + train_name
    cur_label = train_name
    i = 1

    for file in glob.glob(cur_path + "/*.jpg"):
        print ("Processing Image - {} in {}".format(i, cur_label))
        # read the training image
        image = cv2.imread(file)
        imagehsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        colorbg = cv2.calcHist([imagehsv], [0, 1], None, [8,10], [0, 256, 0, 256])
        colorbg = cv2.normalize(colorbg, colorbg).flatten()      
        # extract haralick texture from the image
        desclbp = LocalBinaryPatterns(100, 3) # (The number of points p in a circularly symmetric neighborhood to consider, radius of the circle)
        lbpfg = desclbp.describe(imagehsv[:, :, 2])
        
        features = extract_features(gray)
        fv = np.concatenate((colorbg,lbpfg),axis=None)
        #print((fv))

        # append the feature vector and label
        train_features.append(fv)
        train_labels.append(cur_label)

        # show loop update
        i += 1

# have a look at the size of our feature vector and labels
print ("Training features: {}".format(np.array(train_features).shape))
print ("Training labels: {}".format(np.array(train_labels).shape))

# create the classifier
print ("[STATUS] Creating the classifier..")
#clf_svm = SVC(kernel='linear',probability=True,random_state=9)
#clf_svm = RandomForestClassifier()
clf_svm = RandomForestClassifier()

# fit the training data and labels
print ("[STATUS] Fitting data/label to model..")
clf_svm.fit(train_features, train_labels)
# save the model to disk
filename = 'rf_pascal_pattern.sav'
pickle.dump(clf_svm, open(filename, 'wb'))

# loop over the test images
test_path = "textureDataset/test"
for file in glob.glob(test_path + "/*.jpg"):
    # read the input image
    image = cv2.imread(file)
    imagehsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    colorbg = cv2.calcHist([imagehsv], [0, 1], None, [8,10], [0, 256, 0, 256])
    colorbg = cv2.normalize(colorbg, colorbg).flatten()      
    # convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # extract haralick texture from the image
    features = extract_features(gray)
    lbpfg = desclbp.describe(imagehsv[:, :, 2])
    fv = np.concatenate((colorbg,lbpfg),axis=None)
    # evaluate the model and predict label
    prediction = clf_svm.predict(fv.reshape(1, -1))[0]
    
    #class_probabilities = clf_svm.predict_proba(lbpfg.reshape(1, -1))[0]
    #print(class_probabilities)  

    # show the label
    cv2.putText(image, prediction, (20,30), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0,255,255), 1)
    print ("Prediction - {}".format(prediction))
    cv2.imwrite(os.getcwd() + "/segmentresult/fg.jpg",image)
    # display the output image
    cv2.imshow("Test_Image", image)
    cv2.waitKey(0)