#!/usr/bin/env python
# coding: utf-8

# In[1]:


import argparse
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
from ModelFeatureVector_new import ExtractFeatures
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input


# In[2]:


cd = ExtractFeatures()
#approximately takes 2 minutes
output_vgg16 = open("index_vgg16.csv", "w")
i=0
for imagePath in glob.glob('C:/Users/rania/Desktop/NLPproject_env/High_Level_Feature/dataset' + "/*.png"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    i+=1
    imageID = imagePath[imagePath.rfind("/") + 1:]
    features_vgg16 = cd.ModelSummary_VGG16(imagePath)
    features_vgg16 = [str(f) for f in features_vgg16]
    output_vgg16.write("%s,%s\n" % (imageID, ",".join(features_vgg16)))
    # close the index file
output_vgg16.close()
    
    


# In[ ]:





# In[ ]:




