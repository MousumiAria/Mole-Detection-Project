
<h1> <align="center">Mole-Detection-Project</h1>

## Developer: 

<a href="https://https://github.com/MousumiAria"> Mousumi Sen</a>

## Level: 
* Junior Developer

## Organization:
* Becode Company (Ghent)

## The timeline of the project: 
**16/05/2022 - 24/05/2022 4:30**

## Duration: 
* 8 days

## Dataset details:
* The dataset provided by the client can be found here: https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000 


## Description:

Skin cancer is a common disease that affect a big amount of peoples.The purpose of this project is to create a tool that considering the image of a mole, can calculate the probability and predict which skin cancer type of the given mole.The steps of the project are following:

# Preprocessing:
The following preprocessing tasks are developed for each image:

Visual inspection to detect images with low quality or not representative
Image resizing: Transform images to 224x224x3
Other to define later in order to improve model quality

# CNN Model:
The idea is to develop a simple CNN model from scratch, and evaluate the performance to set a baseline. The following steps to improve the model are:

* Data augmentation: used ImageDataGenerator, scaling to avoid overfitting
* Used  MobileNetV2 as model. 
* For compile: as optimizer used 'adam',
               for loss used 'CategoricalCrossentropy',
               for  metricsused 'accuracy'


# Model Evaluation:

To evaluate the different models we will use ROC Curves and AUC score. To choose the correct model we will evaluate the precision and accuracy to set the threshold level that represent a good tradeoff between TPR and FPR.

## Used Language and Libraries:

* Python
* Numpy
* Pandas 
* Matplotlib
* Flask
* sklearn
* Tensorflow
* keras



