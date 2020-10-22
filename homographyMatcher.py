import cv2
import numpy as np


class HomographyMatcher:
    def __init__(self):
        self.sift =cv2.SIFT().create()
        self.bf = cv2.BFMatcher()

    def match(self, i1, i2, direction=None):
        imageSet1 = self.getSIFTFeatures(i1)
        imageSet2 = self.getSIFTFeatures(i2)
        matches = self.bf.knnMatch(imageSet1['des'],imageSet2['des'],k=2) 
        good = []
        for m in matches:
            if m[0].distance < 0.5*m[1].distance:         
     	        good.append(m)
        matches = np.asarray(good)
        if len(matches[:,0]) >= 4:
            src = np.float32([ imageSet1['kp'][m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
            dst = np.float32([ imageSet2['kp'][m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
            H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
            return H
        else:
            raise AssertionError("Can't find enough keypoints.")  

    def getSIFTFeatures(self, im):

        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        # print(gray)
        kp, des = self.sift.detectAndCompute(gray, None)
        # print("***")
        return {'kp': kp, 'des': des}
