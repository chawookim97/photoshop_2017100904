import sys
import cv2
import numpy as np
from PIL import ImageQt
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
)
class Clear:
    def __init__(self, parent=None):
        self.parent = parent

    def clear_label(self):
        self.parent.label2.clear()