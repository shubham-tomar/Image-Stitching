import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
from random import randrange
from homographyMatcher import HomographyMatcher
import time


class Stitch:
    def __init__(self, imgs):
        self.foldername = imgs
        filenames = glob.glob(imgs + "/*")
        # print(filenames)
        self.images = [cv2.resize(cv2.imread(each), (1000, 500)) for each in filenames]
        self.count = len(self.images)
        self.left_list, self.right_list, self.center_im = [], [], None
        self.matcher_obj = HomographyMatcher()
        self.prepare_lists()
        self.mediumImageStitch()

    def prepare_lists(self):
        print("Number of images : %d" % self.count)
        self.centerIdx = self.count / 2
        print("Center index image : %d" % self.centerIdx)
        self.center_im = self.images[int(self.centerIdx)]
        for i in range(self.count):
            if (i <= self.centerIdx):
                self.left_list.append(self.images[i])
            else:
                self.right_list.append(self.images[i])
        print("Image lists prepared")
    
    def mediumImageStitch(self):
        a = self.left_list[0]
        for b in self.left_list[1:]:
            H = self.matcher_obj.match(a, b, 'left')
            dst = cv2.warpPerspective(a,H,(b.shape[1] + a.shape[1], b.shape[0]))     	
            plt.subplot(122),plt.imshow(dst),plt.title('Warped Image')
            plt.show()
            plt.figure()
            dst[0:b.shape[0], 0:b.shape[1]] = b
            plt.imshow(dst)
            plt.show()
            cv2.imwrite(str(self.foldername) + '\\resultant_stitched_panorama.jpg',dst)

if __name__ == '__main__':
    imgfolderPath = 'E:\\demoProj\\DLProjs\\data'
    imagesPath = glob.glob(imgfolderPath + "/*")
    print(imagesPath)
    for folder in imagesPath:
        s = Stitch(folder)
        print("image written")
        cv2.destroyAllWindows()