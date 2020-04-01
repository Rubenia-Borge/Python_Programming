#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

#Reads the image of a sunset into an array
img = mpimg.imread('Documents/images2/images2/city1.jpg')
print(img)

#Plots the image from the array data 
imgplot = plt.imshow(img)

#Prints the shape of the image array
print()
print("Shape of the image array")
print(img.shape)


# In[2]:


#Plots the image from the array data 
imgplot = plt.imshow(img)
plt.show()


# In[3]:


#Portion of the image
#X-range on the right and y-range on the left 
cropped_img = img[138:140, 194:196]
print(cropped_img)

#Plot the cropped image 
cropped_img_plot = plt.imshow(cropped_img)
plt.show()


# In[4]:


#Function to make the color histograms 
def make_histogram(image):
    def getRed(redVal):
        return '#%02x%02x%02x' % (redVal, 0, 0)

    def getGreen(greenVal):
        return '#%02x%02x%02x' % (0, greenVal, 0)

    def getBlue(blueVal):
        return '#%02x%02x%02x' % (0, 0, blueVal)

    # Modify the color of two pixels
    image.putpixel((0,1), (1,1,5))
    image.putpixel((0,2), (2,1,5))

    # Display the image
    image.show()

    # Get the color histogram of the image
    histogram = image.histogram()


    # Take only the Red counts
    red = histogram[0:256]
 
    # Take only the Green counts
    green = histogram[256:512]

    # Take only the Blue counts
    blue = histogram[512:768]
    
    fig = plt.figure()
    
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    
    # Red histogram
    for i in range(0, 256):
        ax1.set_title('Red Histogram')
        ax1.bar(i, red[i], color = getRed(i), edgecolor=getRed(i), alpha=0.3)

    # Green histogram
    for i in range(0, 256):
        ax2.set_title('Green Histogram')
        ax2.bar(i, green[i], color = getGreen(i), edgecolor=getGreen(i),alpha=0.3)

    # Blue histogram
    for i in range(0, 256):
        ax3.set_title('Blue Histogram')
        ax3.bar(i, blue[i], color = getBlue(i), edgecolor=getBlue(i),alpha=0.3)
        
    fig.subplots_adjust(hspace=0.2,top=0.5,wspace=0.2)
    fig.tight_layout()

    plt.show()
    
#Function to make pie-chart of relative RGB values
def make_pie_chart(image):
    #Average of red, green, blue values 
    RGBtuple = np.array(image).mean(axis=(0,1))
    averageRed = RGBtuple[0]
    averageGreen = RGBtuple[1]
    averageBlue = RGBtuple[2]

    #Pie chart with amount of red, green, and blue in the image
    #Data to plot
    labels = 'Red','Green','Blue'
    sizes = [averageRed,averageGreen,averageBlue]
    colors = ['red','green','blue']
    explode = (0.1,0,0)
    #Plotting the pie chart
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=270)
    plt.title('Relative Amount of Red, Green, and Blue in the Image',fontweight='bold')
    plt.axis('equal')
    plt.show()


# In[5]:


#https://pythontic.com/image-processing/pillow/histogram
imageSunset = Image.open('Documents/images2/images2/city1.jpg')
    
#Histogram for sunset image-- reads in the image of the sunset
make_histogram(imageSunset)
make_pie_chart(imageSunset)


# In[10]:


#Reads the image of a strawberry into an array
strawberry= mpimg.imread('Documents/images2/images2/city2.jpg')

#Plots the image of a strawberry from the array data 
strawberry_plot = plt.imshow(strawberry)

#https://pythontic.com/image-processing/pillow/histogram
imageStrawberry = Image.open('Documents/images2/images2/city2.jpg')

#Color histograms and pie chart for strawberry image
make_histogram(imageStrawberry)
make_pie_chart(imageStrawberry)

