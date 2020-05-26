# IRTEX : Image REtrieval with TExtual Explanation

This branch contains files for extracting low level features based on MPEG-7 color, shape and texture descriptors.
Repository has 2 parts :
  1. Java application : MPEGFeatureExtraction
  2. Python Notebook for Image Search


# 1. Java application : MPEGFeatureExtraction
The MPEG-7 Descriptors used for feature extraction are :
  1. Color Descriptor:
      1. Scalable Color Descriptor: It is a color histogram in the HSV color space. It has a scalable binary representation                                       over a large granularity range. The scalability is achieved in terms for bit                                                   representation and bin numbers.
      2. Color Layout Descriptor: It represents a very compact spatial layout of color image. An 8x8 thumbnail of the image is                                   generated which is encoded and quantized.
      3. Edge Histogram Descriptor: It represents spatial distribution of total five edges – four directional and one non-                                         directional edges. Each edge is consisting of local histograms which can be aggregated as                                     global histogram.
  2. Shape Descriptor:
      1. Region-Based Shape Descriptor: The descriptor expresses the region-based shape of an object. Multiple objects with                                           discontinuous regions can be described by this descriptor. It gives a compact and                                             efficient way of describing properties of multiple disjoint regions simultaneously.
      
 
## To run this java application below are the steps to follow :

  Feature Extraction runnable JAR name : mpegfeatures.jar
  ### To Extract complete dataset features :
    Command : java -jar mpegfeatures.jar -f cifar10/cifar10/train
       • -f : token to indicate dataset feature generation
       • cifar10/cifar10/train : name of the directory
    Output file name : outputFeature.csv
    Output file location : same as runnable jar location
    
    
  ### To Extract query image feature :
    Command : java -jar mpegfeatures.jar -i cifar10/cifar10/train/airplane/0001.png
       • -i : token to indicate query image feature extraction
       • cifar10/cifar10/train/airplane/0001.png : query image
    Output file name : queryFeature.csv
    Output file location : same as runnable jar location



