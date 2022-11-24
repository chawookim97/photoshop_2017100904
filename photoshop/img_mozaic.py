import sys
import cv2
import numpy as np
from PIL import ImageQt
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
)

class Mozaic:
    def __init__(self, parent=None):
        self.parent = parent
    
    def mozaic(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
        img = cv2.resize(self.parent.image, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.2,5)
        for (x,y,w,h) in faces:
            face_img = img[y:y+h, x:x+w]
            face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.05, fy=0.05) 
            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
            img[y:y+h, x:x+w] = face_img

            h, w, _ = img.shape
            bytes_per_line = 3 * w
            img = QImage(
                img.data, w, h, bytes_per_line,QImage.Format_RGB888
            ).rgbSwapped()
            self.pixmap = QPixmap(img)
            self.label2.setPixmap(self.pixmap)