import sys
import cv2
import os
import numpy as np
import pylab as plt

def main():
    dir_path = "D:/desktop/cv/openpose"
    try:
        # Change these variables to point to the correct folder (Release/x64 etc.)
        sys.path.append(dir_path + '/bin/python/openpose/Release');
        os.environ['PATH'] = os.environ['PATH'] + ';' + dir_path + '/x64/Release;' + dir_path + '/bin;'
        import pyopenpose as op
    except ImportError as e:
        print(
            'Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
        raise e

    params = dict()
    params["model_folder"] = dir_path + "/models/"

    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    # Process Image
    datum = op.Datum()
    imageToProcess = cv2.imread("D:/desktop/cv/05.jpg")
    img_cloth = cv2.imread('D:/desktop/cv/05_cloth.jpg')
    cloth_select = 4
    points_cloth = [
        [(170,549),(280,547),(128,290),(314,290)],
        [(155,529),(290,529),(125,220),(315,220)],
        [(155,554),(270,549),(119,270),(330,275)],
        [(159,550),(272,550),(113,248),(326,252)],
        [(174,495),(270,495),(146,238),(301,249)]
    ]

    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))

    # Display Image
    print("Body keypoints: \n" + str(datum.poseKeypoints))
    points = datum.poseKeypoints[0]
    neck = points[1]
    shoulder_l = points[2]
    shoulder_r = points[5]
    hip = points[8]
    hip_l = points[9]
    hip_r = points[12]
    #cv2.imshow("OpenPose", datum.cvOutputData)
    cv2.waitKey(0)


    img_h, img_w, img_c = imageToProcess.shape
    img_cloth = cv2.resize(img_cloth, (img_w, img_h))
    # cv2.imshow("OpenPose", img_cloth)
    h, w, c = img_cloth.shape

    '''
    datum_cloth = op.Datum()
    datum_cloth.cvInputData = img_cloth
    opWrapper.emplaceAndPop(op.VectorDatum([datum_cloth]))
    print("Cloth keypoints: \n" + str(datum_cloth.poseKeypoints))
    points_cloth = datum_cloth.poseKeypoints[0]
    shoulder_l_cloth = points_cloth[2]
    shoulder_r_cloth = points_cloth[5]
    hip_l_cloth = points_cloth[9]
    hip_r_cloth = points_cloth[12]
    cv2.imshow("Cloth", datum_cloth.cvOutputData)
    '''

    pts_src = np.array([(points_cloth[cloth_select][0][0], points_cloth[cloth_select][0][1]), (points_cloth[cloth_select][1][0], points_cloth[cloth_select][1][1]),(points_cloth[cloth_select][2][0], points_cloth[cloth_select][2][1]), (points_cloth[cloth_select][3][0], points_cloth[cloth_select][3][1])])
    pts_dst = np.array([(hip_l[0], hip_l[1]), (hip_r[0], hip_r[1]), (shoulder_l[0], shoulder_l[1]), (shoulder_r[0], shoulder_r[1])])
    homography, status = cv2.findHomography(pts_src, pts_dst)
    print(homography.shape)
    print(homography)

    img_out = cv2.warpPerspective(img_cloth, homography, (w, h), borderValue=(255,255,255))
    img_out = cv2.resize(img_out, (img_w, img_h))
    img_combine = cv2.add(imageToProcess,img_out)

    cv2.imwrite("D:\\desktop\\cv\\output1.jpg", datum.cvOutputData)
    cv2.imwrite("D:\\desktop\\cv\\output2.jpg", img_out)
    cv2.imwrite("D:\\desktop\\cv\\output3.jpg", img_combine)

    plt.figure()
    plt.subplot(1, 3, 1), plt.imshow(datum.cvOutputData[:, :, ::-1]), plt.title('src')
    plt.xticks([]), plt.yticks([])
    plt.subplot(1, 3, 2), plt.imshow(img_out[:, :, ::-1]), plt.title('cloth')
    plt.xticks([]), plt.yticks([])
    plt.subplot(1, 3, 3), plt.imshow(img_combine[:, :, ::-1]), plt.title('out')
    plt.xticks([]), plt.yticks([])
    plt.show()  # show dst

    cv2.imshow("OpenPose", img_out)

if __name__ == "__main__":
    main()
