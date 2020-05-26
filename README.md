# IRTEX
Image Retrieval with Textual Explanation


1)dataset : which is basically a mixture of ciphar-10 images

2)query : which has a query image from ciphar-10

I have implemented on VGG16, and RESNET 50.

First VGG16:

in the command prompt type : python index_vgg16.py (this will write the feature vector to the csv file index_vgg16.csv)


Next type: python search_vgg16.py --index index_vgg16.csv --result dataset(This ranks the results according to cosine and Eucledean 
and places the images in ResultVGG_Cosine and ResultVGG_Eucledean (Make sure to create these before hand).

Second Resnet:

Similarly for Resnet50 : python index_resnet50.py (this will write the feature vector to the csv file index_resnet.csv)

Next type: python search_resnet50.py --index index_resnet.csv --result dataset(This ranks the results according to cosine and Eucledean 
and places the images in ResultResnet_Cosine and ResultResnet_Eucledean (Make sure to create these before hand).

For sample I have already uploaded index_resnet.csv and index_vgg16.csv
Please note that Resnetcsv takes quite some time to write vectors to csv.

Also if any exceptions occur with a warning please ignore!

