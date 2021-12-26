import cv2
import os

"""
Run this and take images by clicking space.
Once you have enough images, change the filenames of the images
to the corresponding names of the faces.
"""

# check that dir exists
path = 'known_faces'
if not os.path.exists(path):
    os.makedirs(path)

cam = cv2.VideoCapture(0)
cv2.namedWindow("take_pic")
img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("take_pic", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "known_faces/person_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
