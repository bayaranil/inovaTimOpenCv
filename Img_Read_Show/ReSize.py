import cv2
img = cv2.imread("inovatim.jpeg")
cv2.resize(img, (640, 480))
cv2.namedWindow("inovatim")
cv2.imshow("inovatim", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
