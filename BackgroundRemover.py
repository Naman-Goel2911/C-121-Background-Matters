# imports
import numpy as np
import time
import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID') 
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

time.sleep(2)
bg = 0

for i in range(60):
    ret, bg = cap.read()

bg = np.flip(bg, axis = 1)

while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break

    img = np.flip(img, axis = 1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])
    mask = cv2.inRange(hsv, l_black, u_black)
    res = cv2.bitwise_and(img, img, mask = mask)
    res2 = cv2.bitwise_and(bg, bg, mask = mask)

    f = ret - res
    f = np.where(f == 0, img, f)

    finalOutput = cv2.addWeighted(res, 1, res2, 1, 0)
    output_file.write(finalOutput)

    # displaying the output to the user
    cv2.imshow('magic', finalOutput)
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()