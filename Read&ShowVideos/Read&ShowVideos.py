import cv2

cap = cv2.VideoCapture("antalya.mp4")

while True:
	ret, frame = cap.read()
	if ret == 0:
		break
	frame = cv2.flip(frame,1)
	cv2.imshow("Video", frame)
	cv2.waitKey(10)

cap.release()
cv2.destroyAllWindows()