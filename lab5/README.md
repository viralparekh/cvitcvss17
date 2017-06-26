# Lab5: Vision and Language

The recent work in the deep learning which combines visual and liguistic cues include image captioning, multimodal retrieval and visual question answering. Through toy problems this lab tutorial session intends to introduce basic programming concepts required to build deep learning models at scale. 

## Problem 1: Recurrent Neural Networks 

Recurrent neural networks (RNN) are the workhorse in deep learning problems involving sequences. Deep language models, therefore, often use RNNs. Here, we learn to code Long Short Term Memory (LSTM) in PyTorch. 

* Dataset: MNIST

* Problem statement: MNIST digit image which is 28x28 can be considered as a sequence of length 28, 28-D vectors. Here, implement a many-to-one sequence learning LSTM model to classify MNIST digits. 

* Exercise 1 : Convert to BiLSTM, GRU, RNN

* Exercise 2 : Learn 4 digit sequences of numbers formed from MNIST dataset

* Exercise 3 : Code LSTM network to generate [speeches of Dr A P J Abdul Kalam](http://www.abdulkalam.com/kalam/theme/jsp/guest/content-display-more.jsp) 

* Question 1 : How does LSTM cell help alleviate the vanishing or exploding gradient problem present in vanilla RNN.

* Question 2 : What is the differnce between stateful and stateless RNNs ? 

