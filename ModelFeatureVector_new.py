#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import InputLayer
from keras.applications import VGG16
from keras.applications import ResNet50
from keras.models import Model
from keras.preprocessing import image
import numpy as np
from keras.applications.vgg16 import preprocess_input
from keras.applications.resnet50 import preprocess_input as pi
class ExtractFeatures:
    
    
    def ModelSummary_VGG16(self,imagePath):
        #used VGG16 to extract the feature from last layer (output is of 512 dimensions)
        img = image.load_img(imagePath, target_size=(32, 32))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)
        
        base_model1 = VGG16(include_top=False, weights="imagenet", input_shape=(32, 32, 3))
        base_model1 = Model(input=base_model1.input, output=base_model1.layers[-1].output)
        features = base_model1.predict(img)
        return features[0][0][0]
    
    
    def ModelSummary_Resnet50(self,imagePath):
        #using resnet to extract features for the conv layer(output is of 512 dimensions)
        img = image.load_img(imagePath, target_size=(32, 32))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = pi(img)
        
        model = ResNet50(include_top=False, weights="imagenet", input_shape=(32, 32, 3))
        #obtaining 512 feature vector length from batch normalisation layer
        base_model = Model(input=model.input, output=model.get_layer('res5c_branch2b').output)
        features = base_model.predict(img)
        return features[0][0][0]
    
    
    


# In[ ]:




