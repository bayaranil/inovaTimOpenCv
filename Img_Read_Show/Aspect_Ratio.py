import cv2

def resizeWithAspectRatio(img, heigh = None, width = None, inter = cv2.INTER_AREA):
	(h, w) = img.shape[:2]
	dimension = None
	if heigh == None and width == None:
		return img

	elif heigh == None:
		ratio = width/float(w)
		dimension = (int(ratio*h), width)

	else:
		ratio = heigh/float(h)
		dimension = (heigh, int(ratio*w))

	return cv2.resize(img, dimension, interpolation = inter)

img = cv2.imread("inovatim.jpeg")
img_1 = resizeWithAspectRatio(img, heigh = 600, width = None, inter = cv2.INTER_AREA)

cv2.imshow("Original",img)
cv2.imshow("AspectRatio",img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()





