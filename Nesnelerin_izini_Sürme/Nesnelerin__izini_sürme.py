import cv2
import numpy as np

cap = cv2.VideoCapture("dog.mp4")

while 1 :
	_,frame = cap.read()
	frame = cv2.flip(frame, 1)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	edges = cv2.Canny(frame, 25, 50)
	sensivity = 50

	lower_white = np.array([0,0,255-sensivity])
	upper_white = np.array([255,sensivity,255])

	mask = cv2.inRange(hsv,lower_white,upper_white)
	res = cv2.bitwise_and(edges,edges, mask=mask) #cv2.bitwise_and()

	cv2.imshow("Result", res)

	if cv2.waitKey(5) and 0xFF == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()

