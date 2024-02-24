import cv2
import numpy as np
a = cv2.imread("C:/Users/welcome/Pictures/Camera Roll/rose-729509_640.jpg")
Lap = np.array([[0, 1, 0],
                [1, -4, 1],
                [0, 1, 0]])
a1 = cv2.filter2D(a, -1, Lap)
a2 = np.uint8(a1)
cv2.imshow("Difference", np.abs(a - a2))
cv2.waitKey(0)
cv2.destroyAllWindows()
lap = np.array([[-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]])
a3 = cv2.filter2D(a, -1, lap)
a4 = np.uint8(a3)
cv2.imshow("Enhanced Edges", np.abs(a + a4))
cv2.waitKey(0)
cv2.destroyAllWindows()
