# -*- coding: utf-8 -*-
import cv2

def main():

    im = cv2.imread("test.jpg")                     # 入力画像の取得
    im_g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)     # 入力画像をグレースケール変換
    th = cv2.threshold(im_g,127,255,0)[1]           # グレースケール画像の2値化
    cnt = cv2.findContours(th,1,2)[0][0]            # 2値化画像から輪郭検出
    M = cv2.moments(cnt)                            # 輪郭点から白色領域の重心を計算
    (cx,cy) = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
    print(u"重心("+ str(cx) +","+str(cy) + ")")     # 重心を表示
    cv2.circle(im,(cx,cy),5, (0,0,255), -1)         # 重心を赤円で描く
    cv2.imshow("Show Image",im)                     # 結果表示
    cv2.waitKey(0)                                  # キー入力待機
    cv2.destroyAllWindows()                         # ウィンドウ破棄


if __name__ == "__main__":
    main()
