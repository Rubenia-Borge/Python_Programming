#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
import pandas as pd
from sklearn import neighbors
from sklearn import metrics
from sklearn.metrics import accuracy_score, recall_score, average_precision_score, confusion_matrix, precision_score
from matplotlib.pyplot import *

get_ipython().run_line_magic('matplotlib', 'inline')
#Create a function that generates features depending on a label 
#being either 'A", 'B', or 'C'
def label_features(label):
    if (label == 'A'):
        x = 1 + np.random.normal(0,1,1)
        y = 3 + np.random.normal(0,1,1)
    if (label == 'B'):
        x = 3 + np.random.normal(0,1,1)
        y = 5 + np.random.normal(0,1,1)
    if (label == 'C'):
        x = 5 + np.random.normal(0,1,1)
        y = 1 + np.random.normal(0,1,1)
    return x,y


# In[2]:


#Create array with labels ‘a’,’b’,and ‘c’
letters = []
for count in range(10):
    letters.append('A')
for count in range(10):
    letters.append('B')
for count in range(10):
    letters.append('C')
letters_A = np.array(letters)
print('Labels for Data Points')
print(letters_A)

#Create data points for training set
trainingSet = []
for count in range(10):
    trainingSet.append(label_features('A'))
for count in range(10):
    trainingSet.append(label_features('B'))
for count in range(10):
    trainingSet.append(label_features('C'))
    
#X-values from training set
x_training = [x for x, y in trainingSet]
#Converting the x-training list into a 1D array
x_trainingA = np.array(x_training)

#Y values from training set
y_training = [y for x, y in trainingSet]
#Converting the y-training list into a 1D array
y_trainingA = np.array(y_training)
    
#Creates array with x and y training values
xy_trainingA = np.concatenate((x_trainingA,y_trainingA),1)
print()
print('X & Y Values in the Training Set')
print(xy_trainingA)


# In[3]:


test_targets = []
for count in range(50):
    test_targets.append('A')
for count in range(50):
    test_targets.append('B')
for count in range(50):
    test_targets.append('C')

testSet = []
for letter in test_targets:
    testSet.append(label_features(letter))
    
#X-values from test set
x_test = [x for x, y in testSet]
#Converting the x-training list into a 1D array
x_testA = np.array(x_test)

#Y values from training set
y_test = [y for x, y in testSet]
#Converting the y-training list into a 1D array
y_testA = np.array(y_test)
    
#Creates array with x and y training values
xy_testA = np.concatenate((x_testA,y_testA),1)

#turning the targets into an array
test_targets = np.array(test_targets)


# In[4]:



#k-NN classifier for k=1
#By using ‘distance’, closer neighbors will have greater weight #than further ones
k1 = neighbors.KNeighborsClassifier(n_neighbors=1, weights='distance')
k1.fit(xy_trainingA, letters_A)
# apply the model to the test data
k1_pred = k1.predict(xy_testA)
print(k1_pred)


# In[5]:


#k-NN classifier for k=3
k3 = neighbors.KNeighborsClassifier(3,weights='distance')
# apply the model to the test data
k3.fit(xy_trainingA,letters_A)
k3_pred = k3.predict(xy_testA)
print(k3_pred)


# In[6]:


#k-NN classifier for k=9
k9 = neighbors.KNeighborsClassifier(9,weights='distance')
k9.fit(xy_trainingA,letters_A)
# apply the model to the test data
k9_pred = k9.predict(xy_testA)
print(k9_pred)


# In[7]:


#Plotting the training data
get_ipython().run_line_magic('matplotlib', 'inline')
#Plots the first set of 10 values in the training set-- 'A' values
plot(x_trainingA[0:10],y_trainingA[0:10],'go',label='A')
#Plots the second set of 10 values in the training set -- 'B' values
plot(x_trainingA[10:20],y_trainingA[10:20],'ro',label='B')
#Plots the third set of 10 values in the training set-- 'C' values
plot(x_trainingA[20:30],y_trainingA[20:30],'mo',label='C')
xlabel('X-values for Training Set')
ylabel('Y-values for Training Set')
title('Y vs. X for Training Set')
legend(loc='best')
show()


# In[8]:


#Finding the overall accuracy for each k-value

#k=1
#Returns the percentage of correctly classified samples
accuracy_k1 = accuracy_score(test_targets,k1_pred)
print('Accuracy for k=1')
print(accuracy_k1*100)

#k=3
lettersTest_A = k3.predict(xy_testA)
#Returns the percentage of correctly classified samples
accuracy_k3 = accuracy_score(test_targets,k3_pred)
print('Accuracy for k=3')
print(accuracy_k3*100)

#k=9
lettersTest_A = k9.predict(xy_testA)
#Returns the percentage of correctly classified samples
accuracy_k9 = accuracy_score(test_targets,k9_pred)
print('Accuracy for k=9')
print(accuracy_k9*100)


# In[9]:


#Calculating the average recall-- ability of the classifier to find all the positive samples

#Average recall for k=1
recall_k1 = recall_score(test_targets,k1_pred,average='macro')
print('Average recall for k=1')
print(recall_k1)

#Average recall for k=3
recall_k3 = recall_score(test_targets,k3_pred,average='macro')
print('Average recall for k=3')
print(recall_k3)

#Average recall for k=9
recall_k9 = recall_score(test_targets,k9_pred,average='macro')
print('Average recall for k=9')
print(recall_k9)


# In[10]:


#Calculating the average precision

#Average precision for k=1
precision_k1 = precision_score(test_targets, k1_pred, average ='macro')
print('Average precision for k=1')
print(precision_k1)

#Average precision for k=3
precision_k3 = precision_score(test_targets, k3_pred, average='macro')
print('Average precision for k=3')
print(precision_k3)

#Average precision for k=9
precision_k9 = precision_score(test_targets, k9_pred, average = 'macro')
print('Average precision for k=9')
print(precision_k9)


# In[11]:


#Creating the confusion matrix
#Confusion matrix for k1-classifier
confusion_matrix1 = confusion_matrix(test_targets, k1_pred ,labels=['A','B',"C"])
print('Confusion matrix for k1-classifier')
print(confusion_matrix1)

#Confusion matrix for k3-classifier
confusion_matrix3 = confusion_matrix(test_targets, k3_pred, labels=['A','B',"C"])
print('Confusion matrix for k3-classifier')
print(confusion_matrix3)

#Confusion matrix for k-9 classifier
confusion_matrix9 = confusion_matrix(test_targets, k9_pred, labels=['A','B',"C"])
print('Confusion matrix for k9-classifier')
print(confusion_matrix9)


# In[ ]:




