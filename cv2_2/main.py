import cv2
import mediapipe as mp
from PIL import Image
import numpy as np

from cvzone.SelfiSegmentationModule import SelfiSegmentation

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation
BG_COLOR = (192, 192, 192)  # gray
MASK_COLOR = (255, 255, 255)  # white

img1 = cv2.imread('./output2(2).jpg')
img2 = cv2.imread('./output3(2).jpg')
img3=cv2.imread('./output4.png')
sz = img1.shape
for i in range(sz[0]):
    for j in range(sz[1]):
        x = img2[i][j][0]
        y = img2[i][j][1]
        z = img2[i][j][2]
        t = 0
        t = x + t
        t = y + t
        t = z + t
        if t < 600:
            img1[i][j] = img2[i][j]
cv2.imwrite(f'./output2.png', img1)


for indx in range(1 ,6, 1):
    # if indx!=3:
    #     continue
    segmentor = SelfiSegmentation()
    # For static images:
    IMAGE_FILES = [f'./image/0{indx}/0{indx}.jpg']
    # IMAGE_FILES = []


    with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as selfie_segmentation:
        for idx, file in enumerate(IMAGE_FILES):
            image = cv2.imread(file)

            image_height, image_width, _ = image.shape
            # 处理前将BGR图像转换为RGB。
            results = selfie_segmentation.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            # 在背景图像上绘制自拍分割。
            # 为了改进边界周围的分割，考虑应用一个联合
            # 使用“图像”对“results.segmentation mask”进行双边过滤。
            condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
            # 生成纯色图像以显示输出的自拍分割蒙版。
            scale=np.zeros(image.shape, dtype=np.uint8)
            scale[:] = MASK_COLOR
            fg_image = np.zeros(image.shape, dtype=np.uint8)
            fg_image[:] = MASK_COLOR
            # fg_image=image
            bg_image = np.zeros(image.shape, dtype=np.uint8)
            bg_image[:] = BG_COLOR

            output_image = np.where(condition, fg_image, bg_image)
            cv2.imwrite(f'./image/0{indx}/0{indx}_mask.jpg', output_image)


            nm=f'./image/0{indx}/0{indx}_background1.jpg'
            bg_image = cv2.imread(nm)
            sz=image.shape
            adder=0
            fin_image = np.zeros(image.shape, dtype=np.uint8)
            for i in range(sz[0]):
                for j in range(sz[1]):
                    fgo=0
                    fgi=0
                    x = image[i][j][0]
                    y = image[i][j][1]
                    z = image[i][j][2]
                    x1 = output_image[i][j][0]
                    y1 = output_image[i][j][1]
                    z1 = output_image[i][j][2]
                    t = 0
                    t = x + t
                    t = y + t
                    t = z + t
                    if t<680 and x1 == 255 and y1 == 255 and z1 == 255 :
                        bg_image[i][j] = image[i][j]


            print(adder)
            # cv2.imwrite(f'./scale_{indx}.png', scale)
            cv2.imwrite(f'./{indx}.png', bg_image)



# For webcam input:
# BG_COLOR = (192, 192, 192)  # gray

# with mp_selfie_segmentation.SelfieSegmentation(
#         model_selection=1) as selfie_segmentation:
#     for i in range(1,6,1):
#         i=str(i)
#         bg_image = None
#         name=f"./image/0{i}/0{i}.jpg"
#         image = cv2.imread(name)
#         # 水平翻转图像以供稍后自拍视图显示，并转换
#         # 将 BGR 图像转为 RGB。
#         sz=image.shape
#         print(sz)
#         image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
#         # 为了提高性能，可选择将图像标记为不可写入
#         # 通过引用传递。
#         image.flags.writeable = False
#         results = selfie_segmentation.process(image)
#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#         # 在背景图像上绘制自拍分割。
#         # 为了改进边界周围的分割，考虑应用一个联合
#         # 使用“图像”对“results.segmentation mask”进行双边过滤。
#         condition = np.stack(
#             (results.segmentation_mask,) * 3, axis=-1) > 0.5
#         # 背景可以自定义。
#         # a) 加载一张图片（与输入图片的宽度和高度相同）到
#         # 作为背景，例如，bg_image = cv2.imread('/path/to/image/file')
#         # b) 通过应用图像过滤来模糊输入图像，例如，
#         # bg_image = cv2.GaussianBlur(image,(55,55),0)
#         im = Image.open(f'./image/0{i}/0{i}_background.jpg')
#         out = im.resize((sz[1],sz[0]), Image.ANTIALIAS)
#         out.save(f'./image/0{i}/0{i}_background1.jpg')
#         bg_image = cv2.imread(f'./image/0{i}/0{i}_background1.jpg')
#         # bg_image = cv2.GaussianBlur(image,(55,55),0)
#         # imgOut = segmentor.removeBG(image, bg_image, threshold=0.83)
#         # imgOut = segmentor.removeBG(imgOut, bg_image, threshold=0.83)
#         # cv2.imwrite('./' + i + '_1.png', imgOut)
#         if bg_image is None:
#             bg_image = np.zeros(image.shape, dtype=np.uint8)
#             bg_image[:] = BG_COLOR
#         # bg_image = cv2.GaussianBlur(image,(55,55),0)
#         # bg_image = cv2.imread('001.png')
#
#         output_image = np.where(condition, image, bg_image)
#         # output_image=cv2.GaussianBlur(output_image,(55,55),1)
#         # cv2.imshow('MediaPipe Selfie Segmentation', output_image)
#         cv2.imwrite('./' + i + '.png', output_image)
#

