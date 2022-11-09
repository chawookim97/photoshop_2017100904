# 포토샵 프로그램 만들기
## 프로젝트 기획
포토샵에서 사용되는 기능을 python을 사용해 구현하려고 함. 특히 opencv를 이용하여 이미지를 처리하는 기법을 주로 사용하였음. pyside6의 qtgui를 이용하여 윈도우를 만들고 기능들을 추가함.

## 실행파일
photoshop 파일을 실행하고 이미지 파일은 'cat.jpt', 'face.jpg', 'face2.jpg'를 이용하면 됨.

## 필요조건
>python버전 3.9
>
>pyside6
>
>PIL
>
>numpy
>
>opencv

## 기능설명
1. 이미지 불러오기
  - show_file_dialog 메서드를 이용해 이미지를 불러오고 lable1에 이미지를 띄움
2. 좌우반전
- lable1에 띄운 이미지를 flip_image을 이용하여 좌우를 반전시킴
3. 새로고침
- clear_label를 사용하여 lable2의 이미지를 지움
4.사이즈 줄이기
- lable1의 이미지 크기를 (300,300) 사이즈로 줄임
5.프로필 사진 예측
- img_pred를 사용하여 프로필 사진이 다른 사람들에게 어떻게 보일지 예측하는 이미지를 만듦
6. 모자이크
- mozaic 메서드는 얼굴을 인식하여 모자이크를 해주는 기능을 구현함
7. 워터마크
- 사진에 텍스트를 입혀 워터마크를 넣어주는 기능을 추가함

## 느낀 점
처음으로 직접 코딩하여 눈에 보이는 결과물을 만들었다는 점이 재미있었다. 아직 부족한 부분이 매우 많아 하나하나 고치고 피드백하며 발전시켜야겠다.

## 앞으로의 방향
디자인적으로 윈도우가 매우 부족했다. 기능적으로 보완하는것도 중요하지만, 우선 직관적으로 알아볼 수 있도록 수정해야겠다. 