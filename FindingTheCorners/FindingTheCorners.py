import cv2
import numpy as np

img = cv2.imread("triangle.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray) # cv2.goodFeaturesToTrack okuyabilmesi için
corners = cv2.goodFeaturesToTrack(gray, 3, 0.01, 10)
# 3: en fazla kaç köşe
#0.01 : kalite standart
#10 köşeler arası min mesafe

corners = np.int0(corners) #Yeniden int formatına çevirdik.
for i in corners:
	#print(i)
	x,y = i.ravel()
	cv2.circle(img, (x,y), 10, (0,0,255), -1)

cv2.imshow("Corner", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
