# Lab5: Vision and Language

The recent work in the deep learning which combines visual and liguistic cues include image captioning, multimodal retrieval and visual question answering. Through toy problems this lab tutorial session intends to introduce basic programming concepts required to build deep learning models at scale. 

## Problem 1: Recurrent Neural Networks [50 points, 1 hour] [Notebooks 0 and 1]

Recurrent neural networks (RNN) are the workhorse in deep learning problems involving sequences. Deep language models, therefore, often use RNNs. Here, we learn to code Long Short Term Memory (LSTM) in PyTorch. 

* Dataset: MNIST

* Problem statement: MNIST digit image which is 28x28 can be considered as a sequence of length 28, 28-D vectors. Here, implement a many-to-one sequence learning LSTM model to classify MNIST digits. 

* Exercise 1 : Convert to BiLSTM, GRU, RNN

* Exercise 2 (challenge) : Learn 4 digit sequences of numbers formed from MNIST dataset

* Exercise 3 (challenge) : Code LSTM network to generate [speeches of Dr A P J Abdul Kalam](http://www.abdulkalam.com/kalam/theme/jsp/guest/content-display-more.jsp) 

* Question 1 : How does LSTM cell help alleviate the vanishing or exploding gradient problem present in vanilla RNN.

* Question 2 : What is the difference between stateful and stateless RNNs ? 


## Problem 2: Image Captioning [50 points, 1 hour] [Notebooks 2 and 3]

* Dataset: MS COCO, MS COCO captions 

* Problem statement: Given a dataset of images and their captions (sentence descriptions), train a network to generate captions for novel images. The network we demonstrate here consists of a CNN encoder and RNN decoder. 

* Exercise 1: Test the network over few images of your choice. Can you reason about the success and failure cases.

* Question 1: What changes are required in the architecture to make the network focus over regions in an image. 


## DATA

For Notebook 3 (challenge problem), data can be downloaded from:

1. [MS COCO captions](http://msvocds.blob.core.windows.net/annotations-1-0-3/captions_train-val2014.zip)

2. [MS COCO training set](http://msvocds.blob.core.windows.net/coco2014/train2014.zip)

3. [MS COCO testing set](http://msvocds.blob.core.windows.net/coco2014/val2014.zip)

The images should be resized to 256x256 and placed at appropriate location in the data folder. 





