import numpy as np
import cv2

frame = cv2.imread(f'./image/02/02.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of green color in HSV
lower_green = np.array([0, 0, 46])
upper_green = np.array([180, 43, 220])
# Threshold the HSV image to get only blue colors
mask_white = cv2.inRange(hsv,lower_green, upper_green)
mask_black = cv2.bitwise_not(mask_white)

#converting mask_black to 3 channels
W,L = mask_black.shape
mask_black_3CH = np.empty((W, L, 3), dtype=np.uint8)
mask_black_3CH[:, :, 0] = mask_black
mask_black_3CH[:, :, 1] = mask_black
mask_black_3CH[:, :, 2] = mask_black

cv2.imwrite('./orignal.png',frame)
cv2.imwrite('./mask_black.png',mask_black_3CH)

dst3 = cv2.bitwise_and(mask_black_3CH,frame)
cv2.imwrite('./Pic+mask_inverse.png',dst3)

#///////
W,L = mask_white.shape
mask_white_3CH = np.empty((W, L, 3), dtype=np.uint8)
mask_white_3CH[:, :, 0] = mask_white
mask_white_3CH[:, :, 1] = mask_white
mask_white_3CH[:, :, 2] = mask_white

cv2.imwrite('./Wh_mask.png',mask_white_3CH)
dst3_wh = cv2.bitwise_or(mask_white_3CH,dst3)
cv2.imwrite('./Pic+mask_wh.png',dst3_wh)

#/////////////////

# changing for design
design = cv2.imread(f'./image/01/01_cloth.jpg')
design = cv2.resize(design, mask_black.shape[1::-1])
cv2.imwrite('./design_resize.png',design)

design_mask_mixed = cv2.bitwise_or(mask_black_3CH,design)
cv2.imwrite('./design_mask_mixed.png',design_mask_mixed)

final_mask_black_3CH = cv2.bitwise_and(design_mask_mixed,dst3_wh)
cv2.imwrite('./final_out.png',final_mask_black_3CH)


cv2.waitKey() 