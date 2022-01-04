import threading

from datetime import datetime
import cv2,time

class takeAPicture(threading.Thread):
    def __init__(self, delai):
        threading.Thread.__init__(self)
        self.delai = delai

    def run(self):
        while True:
            #print("New selfie")
            self.takeOnePicture()
            time.sleep(self.delai)

    def takeOnePicture(self):
        camera = cv2.VideoCapture(0)
        _, image = camera.read()
        cv2.imwrite("RESULT/"+datetime.now().strftime("%d,%m,%Y %H:%M:%S")+".png", image)
        camera.release()