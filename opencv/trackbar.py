# -*- coding: utf-8 -*-
import cv2
import numpy as np

def nothing(x):
    pass

def main():

    # ウィンドウの作成(トラックバー作成の前に必要)
    cv2.namedWindow("TEST")
    # トラックバーの作成(2つ)
    cv2.createTrackbar("X","TEST",0,255,nothing)
    cv2.createTrackbar("Y","TEST",0,255,nothing)

    while(1):
        # 600*480の黒塗り画像を作成
        im = np.zeros((480,600,3), np.uint8)
        # トラックバーから値を取得
        x = cv2.getTrackbarPos("X","TEST")
        y = cv2.getTrackbarPos("Y","TEST")
        # 取得した値を画像に書き込む
        cv2.putText(im,"X:"+str(x),(10,60), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
        cv2.putText(im,"Y:"+str(y),(10,120), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
        cv2.imshow("TEST",im)
        # キーが押されたら終了
        if cv2.waitKey(10) > 0:
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
