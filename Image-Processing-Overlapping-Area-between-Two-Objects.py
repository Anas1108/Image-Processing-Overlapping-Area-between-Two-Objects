import cv2
import matplotlib.pyplot as plt
import numpy as np

# function to display the image and the title of an image
def showImage(image,title):
    plt.title(title)
    plt.axis('off')
    plt.imshow(image)
    plt.show()

"""# Description_Question-1

First we have to Read both images and store them as  image1 and image2.Then apply the AND operation between them to get only the overlap area and display it.As shown below,after applying AND operation the white portion in the resultant shows the overlap region. then we have to just count number of white pixels in the image that represents the area of overlap in the form pixels

# Qustion-1
"""

# read the image1
image1_1 = cv2.imread("Q-1a.jpg")
# read the image2
image1_2 = cv2.imread("Q-1b.jpg")
#display images
showImage(image1_1," Image 1")
showImage(image1_2,"Image 2")
# Take aand operation between both images two extract overlapping area between both the images
img_bwa = cv2.bitwise_and(image1_1,image1_2)
# display the overlap area
showImage(img_bwa,"Resultant Image")

# iterate loop over the last image too find the number of white pixels, which are actually the  area of overlaping area
cnt=0
for i in img_bwa:
    for j in i:
        for k in j:
            if k>250:
                cnt=cnt+1
print("Number of Overlapping pixels are " + str(cnt))
