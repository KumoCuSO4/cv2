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

    img_cloth = cv2.imread('D:/desktop/cv/05_cloth.jpg')
    datum_cloth = op.Datum()
    datum_cloth.cvInputData = img_cloth
    opWrapper.emplaceAndPop(op.VectorDatum([datum_cloth]))
    print("Cloth keypoints: \n" + str(datum_cloth.poseKeypoints))
    points_cloth = datum_cloth.poseKeypoints[0]

    shoulder_l_cloth = points_cloth[2]
    shoulder_r_cloth = points_cloth[5]
    hip_l_cloth = points_cloth[9]
    hip_r_cloth = points_cloth[12]
    print(points_cloth[9])
    print(points_cloth[12])
    print(points_cloth[2])
    print(points_cloth[5])
    # 174 495 270 495 146 238 301 249
    cv2.imshow("Cloth", datum_cloth.cvOutputData)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()