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
    face = cascade.detectMultiScale(gray, 1.1, 3)
    
    # 顔領域を赤枠で囲む
    for (x, y, w, h) in face:
        im2 = im[y:y+h, x:x+w]
        im2 = cv2.resize(im2, (w/10, h/10))
        im2 = cv2.resize(im2, (w, h), interpolation=cv2.cv.CV_INTER_NN)
        im[y:y+h, x:x+w] = im2

    # 結果を表示
    cv2.imshow("Show Image",img)
    cv2.waitKey(0)              # キー入力待機
    cv2.destroyAllWindows()     # ウィンドウ破棄

if __name__ == '__main__':
main()
