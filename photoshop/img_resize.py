import sys
import cv2
import numpy as np
from PIL import ImageQt
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
)

class Resize:
    def __init__(self, parent=None):
        self.parent = parent

    def resize_image(self):
        image= cv2.resize(self.parent.image, (300,300))
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line,QImage.Format_RGB888
        ).rgbSwapped()
        self.pixmap = QPixmap(image)
        self.label2.setPixmap(self.pixmap)