#!/usr/bin/env python
# coding: utf-8

# In[1]:


import argparse
import glob
import matplotlib.pyplot as plt
import numpy as np
from ModelFeatureVector_new import ExtractFeatures
from keras.preprocessing import image
from keras.models import Model
from keras.applications import ResNet50 
from keras.applications.resnet50 import preprocess_input
import os
from gluoncv import model_zoo, data, utils
from matplotlib import pyplot as plt
from collections import Counter


# In[2]:


net = model_zoo.get_model('yolo3_darknet53_voc', pretrained=True)


# In[3]:


cd = ExtractFeatures()
#base_model1 = VGG16(include_top=False, weights="imagenet")
base_model1 = ResNet50(include_top=False, weights="imagenet")
base_model1 = Model(input=base_model1.input, output=base_model1.layers[-5].output)
output_vgg16 = open("demo.csv", "w")
#Output_resnet = open("index_resnet.csv", "w")
#i=0
for imagePath in glob.glob('C:/Users/rania/Downloads/IRTEX/pascal2009demo' + "/*.jpg"):
    #C:/Users/rania/Downloads/IRTEX/pascal2009
    features_vgg16 = cd.ModelSummary_VGG16(imagePath,base_model1)
    #imageID = imagePath[imagePath.rfind("/") - 1:]
    imageID = imagePath.split('/')[-1].split('\\')[-1]

    x, img = data.transforms.presets.yolo.load_test(imagePath, short=512)
    class_IDs, scores, bounding_boxs = net(x)
    n_box = class_IDs.shape[1]
    objects_detected = []
    objects_detected_key =[]
    count =[]
    objects_dict = {}
    items = []
    keys = []
    items_count =[]
    for n in range(n_box):
        if class_IDs[0][n].asscalar() != -1:
            objects_detected.append(net.classes[int(class_IDs[0][n].asscalar())])
    objects_dict = dict(Counter(objects_detected))
    for key, value in objects_dict.items():
        keys.append(key)
        count.append(value)
    def converttostr(input_seq, seperator):
       # Join all the strings in list
        final_str = seperator.join(input_seq)
        
        return final_str
    seperator = ':'
    objects = converttostr(keys, seperator)
    items.append(objects)
    features_vgg16 = [str(f) for f in features_vgg16] 
#    objects_detected_key = [str(f) for f in items]
    count = [str(c) for c in count]
    count_of_objects = converttostr(count, seperator)
    items_count.append(count_of_objects)
#    output_vgg16.write("%s,%s,%s\n" % (imageID, ",".join(features_vgg16),','.join("%s:%s" % (k,v) for k,v in objects_dict.items())))
 
    output_vgg16.write("%s,%s,%s,%s\n" % (imageID, ",".join(features_vgg16),','.join(items),','.join(items_count)))
  #  features_resnet50 = [str(f) for f in features_resnet50]
  #  Output_resnet.write("%s,%s\n" % (imageID, ",".join(features_resnet50)))
    # close the index file
output_vgg16.close()
    
    

    
   
  #  features_vgg16 = cd.ModelSummary_VGG16(imagePath,base_model1)
 #   features_resnet50 = cd.ModelSummary_Resnet50(imagePath)



    
    


# In[ ]:




