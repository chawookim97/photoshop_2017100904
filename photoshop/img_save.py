import sys
import cv2
import numpy as np
from PIL import ImageQt
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
)

class Save:
    def __init__(self, parent=None):
        self.parent = parent

    def save_picture(self):
        _image = ImageQt.fromqpixmap(self.parent.pixmap)
        _image.save("result.png")