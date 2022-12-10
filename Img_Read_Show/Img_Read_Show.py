import cv2
img = cv2.imread("inovatim.jpeg",0) #görsel okuma ,#0 =grayscale
#print(img)
cv2.namedWindow("image",cv2.WINDOW_NORMAL) # pencere boyutlandırması
cv2.imshow("image",img) # görseli gösterme
cv2.imwrite("D:\inovatim\inovatim_2_Gray_Scale.jpeg",img) # görseli uzantıya kaydetme
cv2.waitKey(0) # bekleme time (ms)
cv2.destroyAllWindows() # q tuşuna basınca çıkma