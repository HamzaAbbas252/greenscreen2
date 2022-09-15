import cv2
import numpy as np

img= cv2.imread("gsreen.jpg")
image= cv2.imread("pepsi.jpg")
image = cv2.resize(image, (1023,673))
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_range = np.array([45,45,70])
upper_range = np.array([70,255,255])
mask= cv2.inRange(hsv,lower_range,upper_range)

res= cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("image",img)

f= img - res
f= np.where(f==0 ,image ,f )
cv2.imshow("Mask",mask)
cv2.imshow("Mask",f)

cv2.waitKey()
cv2.destroyAllWindows()