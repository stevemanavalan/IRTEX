#!/usr/bin/env python
# coding: utf-8

# In[6]:


import argparse
import glob
import matplotlib.pyplot as plt
import numpy as np
from ModelFeatureVector_new import ExtractFeatures
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input


# In[1]:


cd = ExtractFeatures()
#Writing the extracted features of a sample datset to a csv file time taken approx 7 minutes
output_resnet = open("index_resnet.csv", "w")
i=0
for imagePath in glob.glob('C:/Users/rania/Desktop/NLPproject_env/High_Level_Feature/dataset' + "/*.png"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    i+=1
    imageID = imagePath[imagePath.rfind("/") + 1:]
    
    features_resnet50 = cd.ModelSummary_Resnet50(imagePath)
    features_resnet50 = [str(f) for f in features_resnet50]
    output_resnet.write("%s,%s\n" % (imageID, ",".join(features_resnet50)))
    # close the index file
output_resnet.close()
    


# In[ ]:





# In[ ]:




