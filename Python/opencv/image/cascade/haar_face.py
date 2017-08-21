# -*- coding: utf-8 -*-
import cv2


def main():

    # 入力画像の読み込み
    img = cv2.imread("test.png")
    
    # カスケード型識別器の読み込み
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 顔領域の探索
    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))
    
    # 顔領域を赤色の矩形で囲む
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)

    # 結果を出力
    cv2.imshow("result.jpg",img)

    
if __name__ == '__main__':
    main()
