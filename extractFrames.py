# # Importing all necessary libraries 
# # venv path => E:\demoProj\DLProjs\opencvenv\Scripts\activate.bat
import cv2 
import os 
import glob
# Read the video from specified path
cam = cv2.VideoCapture("E:\\demoProj\\DLProjs\\synergyTask2\\stitch.avi")
try:
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
# frame
currentframe = 0

while(True):
    # reading from frame
    ret,frame = cam.read()
    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
        # writing the extracted images
        cv2.imwrite(name, frame)
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 10
        cam.set(1,currentframe)
    else:
        break
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()


# imgfolderPath = 'E:\\demoProj\\DLProjs\\data\\truck'
# imgesPath = ['ghh']
# imagesPath = glob.glob(imgfolderPath + "/*")
# print("List",imagesPath)
# allImages = []
# dim = (1024,768)
# for img in imagesPath:
#     temp=cv2.imread(img, cv2.IMREAD_COLOR)
#     temp = cv2.resize(temp,(480,320))
#     allImages.append(temp)
# print('images Read')
#
# stitcher = cv2.Stitcher.create()
# ret,pano = stitcher.stitch(allImages)
#
# # if ret==cv2.STITCHER_OK:
# cv2.imshow('Panorama',pano)
# cv2.waitKey()
# cv2.destroyAllWindows()
# # else:
# #     print("Error during Stitching")
