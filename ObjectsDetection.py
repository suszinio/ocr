from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import imutils
import cv2

#inicializacja HOG descriptor/ wykrywacza osób
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# ladowanie zdjecia
imPath = 'C:\\Users\\rb34187\\Documents\\detector\\example_03.png'
image = cv2.imread(imPath)
image = imutils.resize(image,width=min(1200, image.shape[1]))
orig = image.copy()

# wyszukaj ludzi na zdjeciu
(rects, weights ) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8,8), scale=1.05)

# obrysuj ksztalt ludzi
for (x,y,w,h) in rects:
    cv2.rectangle(orig,(x,y), (x + w, y + h ), (0, 0, 255),2)

#uzywamy non-maxima suppression zeby ograniczyc kontury do jednego,sensownego
rects = np.array([[x, y, x + w, y + h] for (x,y,w,h) in rects])
pick = non_max_suppression(rects,probs = None,overlapThresh=0.65)

# obrysuj finalny ksztalt
for(xA,yA,xB,yB) in pick:
    cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255,0),2)

# pokaz informacje o obrysach
filename = imPath[imPath.rfind("/")+1:]
print("[INFO] {}: {} original boxes, {} after suppression".format(
		filename, len(rects), len(pick)))
#pokaz wynik
cv2.imshow("Before NMS",orig)
cv2.imshow("After NMS",image)
cv2.waitKey(0)

