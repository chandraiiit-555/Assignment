
import cv2

"""

OpenCV (Open Source Computer Vision) is one of the most widely used tools 

for computer vision and image processing tasks.

OpenCV Usage:
   
"""

# ********************* 1. Read and write images ******************


# cv2.imread() is used to read an image.
img_grayscale = cv2.imread('no_such_column_issue.png',0)


# cv2.imshow() is used to display an image in a window.
cv2.imshow('graycsale image',img_grayscale)

cv2.waitKey(0)

# cv2.destroyAllWindows() destroys all the windows we created.
cv2.destroyAllWindows()

#cv2.imwrite() is used to write an image.
cv2.imwrite('gray_scale.jpg',img_grayscale)


# ****************** 2. Image Resizing ***************************

sample_img = cv2.imread('no_such_column_issue.png')
cv2.imshow('Original Image', sample_img)
down_width = 300
down_height = 200
down_points = (down_width, down_height)

#downscale the image using new  width and height
resized_img = cv2.resize(sample_img, down_points, interpolation= cv2.INTER_LINEAR)
cv2.imwrite('resized_img.jpg',resized_img)



# ************************ 3. Cropping an image ******************************

img = cv2.imread('no_such_column_issue.png')

print("Image shape",img.shape)
cv2.imshow("original", img)

cropped_image = img[100:300, 150:330]
cv2.imshow("cropped", cropped_image)
cv2.imwrite("cropped_image.jpg", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

They are many other usages with openCV include

4. Reading and writing Videos.

5. Image rotation and translation etc

"""







