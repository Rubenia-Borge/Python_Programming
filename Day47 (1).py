#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[ ]:




