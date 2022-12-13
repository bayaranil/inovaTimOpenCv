import cv2
cap = cv2.VideoCapture("dog.mp4")

while True:
	ret,frame = cap.read()
	frame = cv2.flip(frame,1)
	edges = cv2.Canny(frame,100,200) # 100,200 threshold aralığı

	cv2.imshow("frame", frame)
	cv2.imshow("Edges", edges)

	if cv2.waitKey(5) and 0xFF == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()