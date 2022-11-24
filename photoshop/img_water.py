import sys
import cv2
import numpy as np
from PIL import ImageQt
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
)

class Water_mark:
    def __init__(self, parent=None):
        self.parent = parent

    def water_mark(self):
        image1 = self.parent.image
        w, h = image1.shape[:2]
        x = w//2
        y = h//2
        font =  cv2.FONT_HERSHEY_PLAIN
        image1 = cv2.putText(image1, "chanwoo's", (x, y), font, 2, (255,255,255), 1, cv2.LINE_AA)

        h, w, _ = image1.shape
        bytes_per_line = 3 * w
        image1 = QImage(
            image1.data, w, h, bytes_per_line,QImage.Format_RGB888
        ).rgbSwapped()
        self.pixmap = QPixmap(image1)
        self.label2.setPixmap(self.pixmap)
