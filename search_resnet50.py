#!/usr/bin/env python
# coding: utf-8

# In[8]:


from ModelFeatureVector_new import ExtractFeatures
from Searcher import Searcher
import argparse
from keras.preprocessing import image
import cv2


# In[9]:


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
    help = "Path to where the computed index will be stored")
ap.add_argument("-r", "--result", required = True,
    help = "Path to the result path")
args = vars(ap.parse_args())


# In[10]:


cd = ExtractFeatures()
# load the query image and describe it
filename = 'C:/Users/rania/Desktop/NLPproject_env/High_Level_Feature/queries/9896_bird.png'
features_resnet50 = cd.ModelSummary_Resnet50(filename)
# perform the search
searcher = Searcher(args["index"])
results_sim_resnet50 = searcher.search_cosine(features_resnet50)
results_dist_resnet50 = searcher.search_Eucledean(features_resnet50)
print("Results according to Cosine SImiliarity FOR RESNET50")
i=0
for (score, resultID) in results_sim_resnet50:
    i+=1
    result = cv2.imread(resultID)
    cv2.imwrite("C:/Users/rania/Desktop/NLPproject_env/High_Level_Feature/ResultResnet_Cosine/{}".format((resultID.split('\\')[1]).split(".")[0]) +str(score)+".png",result)

    # load the result image and display it
    print(score, resultID)
print("Results according to Eucledean_Norm FOR RESNET50")
for (score, resultID) in results_dist_resnet50:
    # load the result image and display it
    print(score, resultID)
    result = cv2.imread(resultID)
    cv2.imwrite("C:/Users/rania/Desktop/NLPproject_env/High_Level_Feature/ResultResnet_Eucledean/{}".format((resultID.split('\\')[1]).split(".")[0]) +str(score)+".png",result)


# In[ ]:




