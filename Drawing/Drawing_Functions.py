import cv2
import numpy as np

#BGR karşılığı siyah olan sıfırlardan oluşan matrisle bir tuval oluşturur.
#3 --> renklendirmeye izin verir.
#dtype --> Çizim yapılması için default veri tipi
canvas = np.zeros((512,512,3), dtype=np.uint8) + 255 #Beyaz


#canvas = np.zeros((512,512,3), dtype=np.uint8 (SİYAH)
#print(canvas)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()