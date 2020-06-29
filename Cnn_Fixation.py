#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

from layers import Fixations
import glob


# In[2]:


from utils import *

BACKEND = 'tf'
if BACKEND=='tf':
    from tf_helpers import Net, Data


# In[3]:


if BACKEND == 'tf':
    model_path = 'C:/Users/rania/Desktop/NLPproject_env/vgg16.ckpt.data-00000-of-00001'
    index_path = 'C:/Users/rania/Desktop/NLPproject_env/vgg16.ckpt.index'
    graph_path = 'C:/Users/rania/Desktop/NLPproject_env/vgg16.ckpt.meta'
    checkpoint_path = 'C:/Users/rania/Desktop/NLPproject_env/checkpoint'


# In[4]:


net = Net('C:/Users/rania/Desktop/NLPproject_env/vgg16.ckpt.meta', 'C:/Users/rania/Desktop/NLPproject_env/vgg16.ckpt')


# In[5]:


layers = Fixations(net)


# In[6]:


def vgg(points, inc, resFac):
    if BACKEND == 'tf':
        points = layers.fc(points=points, layer='fc3', prevLayer='fc2')
        points = layers.fc(points=points, layer='fc2', prevLayer='fc1')
        points = layers.fc(points=points, layer='fc1', prevLayer='pool4_1')
    else:
        points = layers.fc(points=points, layer='fc8', prevLayer='fc7')
        points = layers.fc(points=points, layer='fc7', prevLayer='fc6')
        points = layers.fc(points=points, layer='fc6', prevLayer='pool5')
        
    points = layers.pool(points=points, prevLayer='conv5_3', K=2, S=2)
    points = layers.conv(points=points,  layer='conv5_3', prevLayer='conv5_2', K=3, S=1, P=1)
    points = layers.conv(points=points,  layer='conv5_2', prevLayer='conv5_1', K=3, S=1, P=1)
    points = layers.conv(points=points,  layer='conv5_1', prevLayer='pool4', K=3, S=1, P=1)
    points = layers.pool(points=points, prevLayer='conv4_3', K=2, S=2)
    points = layers.conv(points=points,  layer='conv4_3', prevLayer='conv4_2', K=3, S=1, P=1)
    points = layers.conv(points=points,  layer='conv4_2', prevLayer='conv4_1', K=3, S=1, P=1)
    points = layers.conv(points=points,  layer='conv4_1', prevLayer='pool3', K=3, S=1, P=1)
    points = layers.pool(points=points, prevLayer='conv3_3', K=2, S=2)
    points = layers.conv(points=points,  layer='conv3_3', prevLayer='conv3_2', K=3, S=1, P=1)
    points = layers.conv(points=points,  layer='conv3_2', prevLayer='conv3_1', K=3, S=1, P=1)
    points = layers.conv(points=points,  layer='conv3_1', prevLayer='pool2', K=3, S=1, P=1)
    points = layers.pool(points=points, prevLayer='conv2_2', K=2, S=2)
    points = layers.conv(points=points,  layer='conv2_2', prevLayer='conv2_1', K=3, S=1, P=1)
    points = layers.conv(points=points,  layer='conv2_1', prevLayer='pool1', K=3, S=1, P=1)
    points = layers.pool(points=points, prevLayer='conv1_2', K=2, S=2)
    points = layers.data(points=points, inc=inc, resFac=resFac)
    return points


# In[7]:


img_path = 'C:/Users/rania/Downloads/IRTEX/VOC2012/Query/2007_000250.jpg'
img, offset, resFac, newSize = imgPreprocess(img_path=img_path)
net.image_dims = newSize
points, image_label = pred(net, img)
points = vgg(points, offset, resFac)
#visualize(img_path, points, diag_percent=0.1, image_label=image_label)


# In[8]:


img = cv2.imread(img_path)
#b, g, r = cv2.split(img)
#img = cv2.merge((r, g, b))
diag = math.sqrt(img.shape[0]**2 + img.shape[1]**2)*0.1
values = np.asarray(points)
selPoints = outlier_removal(values, diag)
# Make heatmap and show images
hm = heatmap(np.copy(img), selPoints)

_, ax = plt.subplots(1,3, figsize=(15, 5))

ax[0].imshow(img), ax[0].axis('off'),
#print(img)
#cv2.imwrite('C:/Users/rania/Downloads/IRTEX/2007_000250.jpg',img)   # save the figure to file
#fig = plt.figure()

ax[1].imshow(img), ax[1].axis('off'),
ax[1].scatter(selPoints[:, 1], selPoints[:, 0]),
ax[1].set_title('CNN Fixations')
ax[2].imshow(img), ax[2].imshow(hm, 'jet', alpha=0.6),
ax[2].axis('off'), ax[2].set_title('Heatmap')
#fig.add_axes(ax[1],ax[2])
_.canvas.draw()
X = np.array(_.canvas.renderer._renderer)
#X = 0.2989*X[:,:,1] + 0.5870*X[:,:,2] + 0.1140*X[:,:,3]
#X = 0.5*X[:,:,1] + 0.5*X[:,:,2] + 1*X[:,:,3]
X = X[:,400:1080]
#fig.savefig('graph.png')
cv2.imwrite('C:/Users/rania/Desktop/NLPproject_env/2007_000250.jpg',X)



#plt.show()


# In[ ]:


for imagePath in glob.glob('C:/Users/rania/Downloads/IRTEX/pascal2009_new/pascal2009' + "/*.jpg"):
    imageID = imagePath.split('/')[-1].split('\\')[-1]
    
    img = cv2.imread(imagePath)
    diag = math.sqrt(img.shape[0]**2 + img.shape[1]**2)*0.1
    values = np.asarray(points)
    selPoints = outlier_removal(values, diag)
    # Make heatmap and show images
    hm = heatmap(np.copy(img), selPoints)

    _, ax = plt.subplots(1,3, figsize=(15, 10))

    ax[0].imshow(img), ax[0].axis('off'),
    ax[1].imshow(img), ax[1].axis('off'),
    ax[1].scatter(selPoints[:, 1], selPoints[:, 0]),
    ax[2].imshow(img), ax[2].imshow(hm, 'jet', alpha=0.6),
    ax[2].axis('off'),
    _.canvas.draw()
    X = np.array(_.canvas.renderer._renderer)
    X = X[:,380:1080]
    cv2.imwrite(os.getcwd() + "/CnnFixation/{}".format(imageID) +".jpg",X)
    


# In[ ]:




