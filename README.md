# Cross-Validation

#What is Cross-Validation?
Cross-validation, sometimes called rotation estimation, is a model validation technique for assessing how the results of 
a statistical analysis will generalize to an independent data set. It is mainly used in settings where the goal is prediction,
and one wants to estimate how accurately a predictive model will perform in practice. In a prediction problem, a model is 
usually given a dataset of known data on which training is run (training dataset), and a dataset of unknown data (or first
seen data) against which the model is tested (testing dataset). The goal of cross validation is to define a dataset to “test”
the model in the training phase (i.e., the validation dataset), in order to limit problems like overfitting, give an insight 
on how the model will generalize to an independent dataset.

One round of cross-validation involves partitioning a sample of data into complementary subsets, performing the analysis on 
one subset (called the training set), and validating the analysis on the other subset (called the validation set or testing set). 
To reduce variability, multiple rounds of cross-validation are performed using different partitions, and the validation results 
are averaged over the rounds.

#Methods
#k-fold cross-validation
 k-fold cross-validation, the original sample is randomly partitioned into k equal size subsamples. Of the k subsamples,
 a single subsample is retained as the validation data for testing the model, and the remaining k − 1 subsamples are used as
 training data. The cross-validation process is then repeated k times (the folds), with each of the k subsamples used exactly 
 once as the validation data. The k results from the folds can then be averaged (or otherwise combined) to produce a single 
 estimation. The advantage of this method over repeated random sub-sampling (see below) is that all observations are used for
 both training and validation, and each observation is used for validation exactly once. 10-fold cross-validation is commonly 
 used, but in general k remains an unfixed parameter.
 
 #Leave-one-out cross-validation
 When k=n (the number of observations), the k-fold cross-validation is exactly the leave-one-out cross-validation.
 
 #Example Output
 
Data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

k-fold cross validation
where k is 2:
     training        test
[1, 3, 5, 7, 9] [0, 2, 4, 6, 8]
[0, 2, 4, 6, 8] [1, 3, 5, 7, 9]

where k is 3:
     training         test
[1, 2, 4, 5, 7, 8] [0, 3, 6, 9]
[0, 2, 3, 5, 6, 8, 9] [1, 4, 7]
[0, 1, 3, 4, 6, 7, 9] [2, 5, 8]

where k is 4:
     training           test
[1, 2, 3, 5, 6, 7, 9] [0, 4, 8]
[0, 2, 3, 4, 6, 7, 8] [1, 5, 9]
[0, 1, 3, 4, 5, 7, 8, 9] [2, 6]
[0, 1, 2, 4, 5, 6, 8, 9] [3, 7]

where k is 5:
     training             test
[1, 2, 3, 4, 6, 7, 8, 9] [0, 5]
[0, 2, 3, 4, 5, 7, 8, 9] [1, 6]
[0, 1, 3, 4, 5, 6, 8, 9] [2, 7]
[0, 1, 2, 4, 5, 6, 7, 9] [3, 8]
[0, 1, 2, 3, 5, 6, 7, 8] [4, 9]

Leave-one-out cross-validation
     training               test
[1, 2, 3, 4, 5, 6, 7, 8, 9] [0]
[0, 2, 3, 4, 5, 6, 7, 8, 9] [1]
[0, 1, 3, 4, 5, 6, 7, 8, 9] [2]
[0, 1, 2, 4, 5, 6, 7, 8, 9] [3]
[0, 1, 2, 3, 5, 6, 7, 8, 9] [4]
[0, 1, 2, 3, 4, 6, 7, 8, 9] [5]
[0, 1, 2, 3, 4, 5, 7, 8, 9] [6]
[0, 1, 2, 3, 4, 5, 6, 8, 9] [7]
[0, 1, 2, 3, 4, 5, 6, 7, 9] [8]
[0, 1, 2, 3, 4, 5, 6, 7, 8] [9]

Reference:https://en.wikipedia.org/wiki/Cross-validation_%28statistics%29
**************************************************************************************************************************

usage: python crossvalidation.py
 

