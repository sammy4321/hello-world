import cv2
img=cv2.imread("cropped.jpg")
#gray=cv2.cvtColor(img.cv2.COLOR_BGR2GRAY)
for i in range(0,28):
	for j in range(0,28):
		if(img[i][j]==255):
			img[i][j]=0
		else:
			img[i][j]=255
cv2.imwrite("cropped.jpg",img)
cv2.imshow("cropped",img)
cv2.waitKey(0)
