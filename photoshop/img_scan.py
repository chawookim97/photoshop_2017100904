import cv2
import numpy as np

point_list = []
src_img = cv2.imread(self.image)
src_img = cv2.resize(src_img, None, fx=0.5, fy=0.5)

COLOR = (255, 255, 255)
THICKNESS = 2
drawing = False

def mouse_handler(event, x, y, flags, param):
    global drawing
    dst_img = src_img.copy()
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        point_list.append((x, y))
     
    if drawing:
        prev_point = None
        for point in point_list:
            cv2.circle(dst_img, point, 10, COLOR, cv2.FILLED)
            if prev_point:
                cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            prev_point = point
        
        next_point = (x, y)
        if len(point_list) == 4:
            show_result()
            next_point = point_list[0]
            
        cv2.line(dst_img, prev_point, next_point, COLOR, THICKNESS, cv2.LINE_AA)
        
    cv2.imshow(label1, dst_img)
    
def show_result():
    width, height = 
    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32) # Output 4개 지점

    matrix = cv2.getPerspectiveTransform(src, dst) # Matrix 얻어옴
    result = cv2.warpPerspective(src_img, matrix, (width, height))
    
    self.pixmap = QPixmap(result)
    self.label2.setPixmap(self.pixmap)