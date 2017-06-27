# Lab5: Vision and Language

The recent work in the deep learning which combines visual and liguistic cues include image captioning, multimodal retrieval and visual question answering. Through toy problems this lab tutorial session intends to introduce basic programming concepts required to build deep learning models at scale. 

## Problem 1: Recurrent Neural Networks [50 points, 1 hour] 

Recurrent neural networks (RNN) are the workhorse in deep learning problems involving sequences. Deep language models, therefore, often use RNNs. Here, we learn to code Long Short Term Memory (LSTM) in PyTorch. 

* Dataset: MNIST

* Problem statement: MNIST digit image which is 28x28 can be considered as a sequence of length 28, 28-D vectors. Here, implement a many-to-one sequence learning LSTM model to classify MNIST digits. 

* Exercise 1 : Convert to BiLSTM, GRU, RNN

* Exercise 2 (challenge) : Learn 4 digit sequences of numbers formed from MNIST dataset

* Exercise 3 (challenge) : Code LSTM network to generate [speeches of Dr A P J Abdul Kalam](http://www.abdulkalam.com/kalam/theme/jsp/guest/content-display-more.jsp) 

* Question 1 : How does LSTM cell help alleviate the vanishing or exploding gradient problem present in vanilla RNN.

* Question 2 : What is the difference between stateful and stateless RNNs ? 


## Problem 2: Image Captioning [50 points, 1 hour]

* Dataset: MS COCO, MS COCO captions 

* Problem statement: Given a dataset of images and their captions (sentence descriptions), train a network to generate captions for novel images. The network we demonstrate here consists of a CNN encoder and RNN decoder. 

* Exercise 1: Test the network over few images of your choice. Can you reason about the success and failure cases.

* Question 1: What changes are required in the architecture to make the network focus over regions in an image. 
