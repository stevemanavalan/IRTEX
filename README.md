# IRTEX
# Foreground and Background (Segmentation)

Retrieval System utilizing foreground and background features of a query image powered by XAI

#### Table of Contents

* Code Organization
* Setup
* Tools and libraries Used
* Evaluation

#### Code Organization

```
|   index.py
|   README.md
|   search.py
+---dataset
+---Evaluation_CIFAR
|   +---Descriptor_Index_csv
|   \---Descriptor_Similariy_evaluation
|       +---Descriptor_euclidean_dist
|       |   +---cd_bg_144bins     
|       |   +---cd_bg_400bins    
|       |   +---cd_bg_80bins      
|       |   +---cd_fg_144bins       
|       |   +---cd_fg_80bins
|       |   +---cd_fg_bg_80bins      
|       |   +---hu_moments_fg      
|       |   +---lbp_bg_24_3_256
|       |   +---lbp_fg_14_4
|       |   +---lbp_fg_24_3_256bins  
|       |   +---lbp_fg_24_4      
|       |   +---zernike_fg_10
|       |   +---zernike_fg_21      
|       |   \---zernike_fg_5|       |           
|       \---distance_measure
|           +---cd_fg_bg_80bins_chi      
|           +---cd_fg_bg_80bins_cosine    
|           +---cd_fg_bg_80bins_emd    
|           +---lbp_fg_24_3_256bins_chi       
|           +---lbp_fg_24_3_256bins_cosine
|           +---lbp_fg_24_3_256bins_emd
|           +---zernike_fg_10_chi
|           +---zernike_fg_10_cosine
|           \---zernike_fg_10_emd  
+---Pascal_VOC
+---query  
\---segment
    |   disjointSet.py
    |   LocalBinaryPatterns.py
    |   SaliencyRC.py
    |   searcher.py
    |   Segmentation.py
    |   segmentGraph.py
    |   segmentImage.py
    |   utils.py
```



#### Execution Instructions

* Open the command line interface (CMD) from the cloned repository path.

* The index.py script loops over the dataset and creates a index csv file. The dataset of images to be indexed needs to be stored in <dataset> folder and the index file will be created in current working directory as <index.csv>. The index file consist of the unique image id followed by the feature vector for all the images in dataset. The index file can be created using the following script

```
python index.py --dataset dataset --index index.csv
```

* After creating the index, we can pass a query image to the retrieval engine. The query image needs to be stored in the <query> folder  and needs to be passed as argument to the command line as shown below

```
python search.py  --index index.csv --query query/9896_bird.png --result dataset
```

Feature vector is generated for the given query image and similarity measure is computed with the feature vector stored in csv and the score and the retrieval ranking is displayed to the user. The search.py script creates a folder <queryresult> which holds the ranked output of retrieval system for further evaluation.

#### Tools and Libraries Used

* OpenCV 4.2.0
* Python 3.8.2
* Mahotas
* skimage

#### Evaluation

The retrieval system was extensively tested on CIFAR benchmark dataset with a subset of 190 sample images. The evaluation was performed using the following local feature descriptors on the foreground and background segments.

* Color Descriptor - Color Histogram with varying number of bins
* Shape Descriptor - Zernike Moments with varying values of radius initialization
* Texture Descriptor - Local binary pattern with varying values of number of points and radius

For each of the descriptors we can find the result of the retrieval system in the subfolders of the directory <Descriptor_Similariy_evaluation> . Index files created for the given sample data set is stored in the path <Descriptor_Index_csv> for further reference and evaluation.

Segmentations results are also evaluated on 50 sample images of PASCAL VOC 2012 and the results are in the subdirectory.

#### References

* Bai, Cong & Chen, Jia-Nan & Huang, Ling & Kpalma, Kidiyo & Chen, Shengyong**. (2017). Saliency-based multi-feature modeling for semantic image retrieval. Journal of Visual Communication and Image Representation. 50. 10.1016/j.jvcir.2017.11.021.
* **Cheng Ming-Ming [et al.]** Global Contrast based Salient Region Detection [Journal]. - [s.l.] : IEEE, 2015. - 3 : Vol. 37.