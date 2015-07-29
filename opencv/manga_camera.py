# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 漫画風に加工
def manga(gray, screen, th1, th2):
    # エッジ検出と色反転
    edge = 255 - cv2.Canny(gray, 80, 120)
    # 画像の3値化
    gray[gray <= th1] = 0
    gray[gray >= th2] = 255
    gray[ np.where((gray > th1)&(gray < th2)) ] = screen[ np.where((gray > th1)&(gray < th2)) ]
    # 3値画像とエッジ画像を合わせる
    return cv2.bitwise_and(gray, edge)


def main():
    screen = cv2.imread("screen.png",0)     # スクリーントーン画像の取得
    screen = cv2.resize(screen,(640,480))   # スクリーントーン画像のサイズを640*480にリサイズ
    cap = cv2.VideoCapture(0)
    # カメラ映像の取得
    while(1):
        ret, im = cap.read()                            # カメラからフレームの取得
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)     # フレームのグレースケール変換
        gray = manga(gray, screen, 60, 160)             # フレームを漫画風に加工
        cv2.imshow("Manga",gray)
        k = cv2.waitKey(10)
        # スペースキーが押されたらフレームを保存
        if k == 32:
            cv2.imwrite("Manga.png",gray)

        # Escキーが押されたら終了
        elif k == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
