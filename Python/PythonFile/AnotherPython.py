from sys import argv
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
from sklearn.decomposition import PCA
import numpy as np
import subprocess
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import sys

token = argv[1]
data = argv[2]

if token == '-f':
    # creating feature vector for dataset and storing in csv
    subprocess.call(['java', '-jar', 'mpegfeatures.jar', '-f', data])
    sys.exit(0)
elif token == '-i':
    # creating feature vector for query image and storing in csv
    subprocess.call(['java', '-jar', 'mpegfeatures.jar', '-i', data])
    
# Read dataset feature vectors
data_features = pd.read_csv('outputFeature.csv', header=None)
# Dropping 1st column from the dataframe
data_feature_vector = data_features.drop(columns=[0])

# Read query image feature vector
query_feature = pd.read_csv('queryFeature.csv', header=None)
# Dropping 1st column from the dataframe
query_feature_vector = query_feature.drop(columns=[0])


# Finding out the number of dimensions that keeps 95% of the variance of the original images
pca_dims = PCA()
pca_dims.fit(data_feature_vector)
cumsum = np.cumsum(pca_dims.explained_variance_ratio_)
d = np.argmax(cumsum >= 0.95) + 1

# Applying PCA on data feature vector
pca = PCA(n_components=d)
data_feature_vector = pca.fit_transform(data_feature_vector)

# Applying same PCA rule to query feature vector
query_feature_vector = pca.transform(query_feature_vector)

# cosine similarity between query image and complete dataset
cos_sim = cosine_similarity(query_feature_vector, data_feature_vector).flatten()

# Create cosine similarity values dataframe
cos_sim_df = pd.DataFrame(cos_sim, columns=['cos_sim'])
# Add cosine similarity as lasy column in data feature dataframe as ground truth
dataset = pd.concat([data_features, cos_sim_df], axis=1)

# sorting result in descending order
sort_result = dataset.sort_values(by='cos_sim', ascending=False)[[0, 'cos_sim']].head(10)

# Query Image
print('QUERY IMAGE..')
query_img = Image.open(query_feature[0][0])
plt.figure(figsize=(5,5))
plt.imshow(query_img, cmap=plt.cm.binary)
plt.show()

# Display result images
img_array = []
for i in sort_result.index:
    img = Image.open(sort_result[0][i])
    img_array.append(img)
    
# Top 10 Search Results
print('TOP 10 SEARCH RESULT')
plt.figure(figsize=(15,15))
for i in range(len(img_array)):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img_array[i], cmap=plt.cm.binary)
#     plt.xlabel(img_array[i][1])
plt.show()

# converting result to json format
json_array = []
for i in sort_result.index:
    x = {
        "ObjectId" : "",
        "name": os.path.basename(sort_result[0][i]),
        "score": os.path.basename(str(sort_result['cos_sim'][i])),
        "color": "",
        "fg" : ""
    }
    json_array.append(x)
# convert into JSON:
json_data = json.dumps(json_array)
print(json_data)
