import sys
import cv2
import numpy as np
from PIL import ImageQt
from PySide6.QtGui import QAction, QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
)
import ctypes

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("chanwoo's Photoshop")

        #메뉴바 만들기
        self.menu = self.menuBar()
        self.menu_file = self.menu.addMenu("파일")
        self.menu_file1 = self.menu.addMenu("저장")
        find = QAction("이미지 열기", self, triggered=self.show_file_dialog)
        save = QAction("이미지 저장", self, triggered=self.save_picture)
        self.menu_file.addAction(find)
        self.menu_file1.addAction(save)

        #메인화면 레이아웃
        main_layout = QHBoxLayout()

        #사이드바 메뉴버튼
        sidebar = QVBoxLayout()
        button1 = QPushButton("줄이기")
        button2 = QPushButton("좌우반전")
        button3 = QPushButton("워터마크")
        button4 = QPushButton("프로필사진 예측하기")
        button5 = QPushButton("모자이크")
        button6 = QPushButton("새로고침")
        button7 = QPushButton("스캔")

        button1.clicked.connect(self.resize_image)
        button2.clicked.connect(self.flip_image)
        button3.clicked.connect(self.water_mark)
        button4.clicked.connect(self.img_pred)
        button5.clicked.connect(self.mozaic)
        button6.clicked.connect(self.clear_label)
        button7.clicked.connect(self.clear_label)

        sidebar.addWidget(button1)
        sidebar.addWidget(button2)
        sidebar.addWidget(button3)
        sidebar.addWidget(button4)
        sidebar.addWidget(button5)
        sidebar.addWidget(button6)
        sidebar.addWidget(button7)

        #레이블1
        self.label1 = QLabel(self)
        self.label1.setFixedSize(700, 600)
        main_layout.addWidget(self.label1)
        #메인 레이아웃
        main_layout.addLayout(sidebar)
        #레이블2
        self.label2 = QLabel(self)
        self.label2.setFixedSize(700, 600)
        main_layout.addWidget(self.label2)

        widget = QWidget(self)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    #이미지 불러오기(예외처리)
    def show_file_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, "이미지 열기", "./")
        if file_name[0].split('.')[-1] in ('jpg','jpeg', 'png', 'JPG', 'PNG','JPEG'):
            self.image = cv2.imread(file_name[0])
        else : ctypes.windll.user32.MessageBoxW(0, "이미지 파일을 선택해주세요.", "Warning", 48)

        h, w, _ = self.image.shape
        bytes_per_line = 3 * w
        image = QImage(
            self.image.data, w, h, bytes_per_line,QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label1.setPixmap(pixmap)
        
    #좌우반전 시키기
    def flip_image(self):
        image = cv2.flip(self.image, 1)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line,QImage.Format_RGB888
        ).rgbSwapped()
        self.pixmap = QPixmap(image)
        self.label2.setPixmap(self.pixmap)

    #새로고침
    def clear_label(self):
        self.label2.clear()

    #사이즈 줄이기
    def resize_image(self):
        image= cv2.resize(self.image, (300,300))
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line,QImage.Format_RGB888
        ).rgbSwapped()
        self.pixmap = QPixmap(image)
        self.label2.setPixmap(self.pixmap)
   
    #프로필사진 형태 예측하기
    def img_pred(self):
        image= cv2.resize(self.image, (300,300))
        mask = np.zeros_like(image)
        h, w = image.shape[:2]
        cv2.circle(mask, (h//2, h//2), h//3, (255, 255, 255), -1)
        image = cv2.bitwise_and(image, mask)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line,QImage.Format_RGB888
        ).rgbSwapped()
        self.pixmap = QPixmap(image)
        self.label2.setPixmap(self.pixmap)

    #사진 저장하기
    def save_picture(self):
        _image = ImageQt.fromqpixmap(self.pixmap)
        _image.save("result.png")

    #얼굴 모자이크하기
    def mozaic(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")

        
        img = cv2.resize(self.image, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

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

    #워터마크 넣기
    def water_mark(self):
        image1 = self.image
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


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())