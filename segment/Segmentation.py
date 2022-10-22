# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:02:45 2020

@author: steve
"""

from segment import SaliencyRC
import cv2
import imutils
import numpy as np
from segment.LocalBinaryPatterns import LocalBinaryPatterns
import mahotas 
from skimage.filters import threshold_minimum
class Segmentation:
        
    def segment(self,img3i):
        img3f = img3i.astype(np.float32)
        img3f *= 1. / 255 #divide the RGB image by 255 -> to get float equivalent
        sal = SaliencyRC.GetRC(img3f,0.4,10,5,0.5) # Generate saliency map for the image
        idxfg = np.where(sal < (sal.max()+sal.min()) / 3)
        idxbg = np.where(sal > (sal.max()+sal.min()) / 3)
        imgfg = img3i.copy()
        imgbg = img3i.copy()
        imgfg[idxfg] = 0 #create foreground mask
        imgbg[idxbg] = 0 #create background mask
        sal = sal * 255
        sal = sal.astype(np.int16)       
              
        ##################################### Begin color Histogram Descriptor ########################################
        hsvImagefg = cv2.cvtColor(imgfg, cv2.COLOR_BGR2HSV)
        hsvImagebg = cv2.cvtColor(imgbg, cv2.COLOR_BGR2HSV)
        vfg =  hsvImagefg[:, :, 2]               
        colorfg = cv2.calcHist([hsvImagefg], [0, 1], None, [8,10], [0, 256, 0, 256]) #cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
        colorfg = cv2.normalize(colorfg, colorfg).flatten() 
        colorbg = cv2.calcHist([hsvImagebg], [0, 1], None, [8,10], [0, 256, 0, 256])
        colorbg = cv2.normalize(colorbg, colorbg).flatten()      
        #####################################End color Histogram Descriptor ###########################################
               
        ##################################### Begin Zernike Shape Descriptor ##########################################
        thresh = threshold_minimum(vfg)
        binary = vfg > thresh  
        binary = binary.astype(np.uint8)      
        outline = np.zeros(vfg.shape, dtype = "uint8")
        cnts = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        cv2.drawContours(outline, [cnts], -1, 255, -1)      
        shapefg = mahotas.features.zernike_moments(outline, 10)
         #shapefg = cv2.HuMoments(cv2.moments(vfg)).flatten() #hu moments not used due to poor performance
        ##################################### End Zernike Shape Descriptor #############################################
        
        ##################################### Begin lbp texture Descriptor #############################################
        desclbp = LocalBinaryPatterns(24, 3) # (The number of points p in a circularly symmetric neighborhood to consider, radius of the circle)
        lbpfg = desclbp.describe(vfg)
        #lbpbg = desclbp.describe(vbg)
        ##################################### End lbp texture Descriptor ###############################################
        
        ##################################### Begin Histogram of Gradient Descriptor ###################################
        #(H, hogImage) = feature.hog(imgfg, orientations=9, pixels_per_cell=(2, 2),
		   #cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1", visualize=True)
        #where_are_NaNs = np.isnan(H)
        #H[where_are_NaNs] = 0
        ##################################### End Histogram of Gradient Descriptor #####################################    
        
        return imgfg,imgbg,sal,shapefg #return image foreground, background and saliency map and the feature vector
    
    