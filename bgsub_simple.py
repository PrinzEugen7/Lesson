# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os.path

# 背景差分
def bg_diff(fn_bg,im_in,th,blur):

    # 背景, 入力画像の取得
    im_bg = cv2.imread(fn_bg,0);
    # 差分計算
    diff = cv2.absdiff(im_in,im_bg)
    # 差分が閾値より小さければTrue
    mask = diff < th
    # 配列（画像）の高さ・幅
    hight = im_bg.shape[0]
    width = im_bg.shape[1]
    # 背景画像と同じサイズの配列生成
    im_mask = np.zeros((hight,width),np.uint8)
    # Trueの部分（背景）は白塗り
    im_mask[mask]=255
    # ゴマ塩ノイズ除去
    im_mask = cv2.medianBlur(im_mask,blur)
    # エッジ検出
    im_edge = cv2.Canny(im_mask,100,200)

    return im_bg, im_in, im_mask, im_edge


def nothing(x):
    pass


if __name__ == '__main__':

    # 閾値調整用のスライダー生成
    cv2.namedWindow("Motion Edge")
    cv2.createTrackbar("threshold", "Motion Edge", 60, 255, nothing)

    # カメラ映像の取得
    capture = cv2.VideoCapture(0)
    while True:
        ret,frame = capture.read()
        th = cv2.getTrackbarPos("threshold", "Motion Edge")
        # 取得した映像をグレースケール変換
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 背景画像がないときのフレームを背景画像として生成
        if os.path.exists("bg.jpg")==False:
            cv2.imwrite('bg.jpg',frame)
        # 背景差分の取得
        im_bg,im_in,im_mask,im_edge = bg_diff("bg.jpg",frame,th,blur=7)
        # 各画像の表示
        cv2.imshow("Input",im_in)
        cv2.imshow("Background",im_bg)
        cv2.imshow("Motion mask",im_mask)
        cv2.imshow("Motion Edge",im_edge)
        key = cv2.waitKey(10)
        # 空白キー押したときのフレームを背景画像として生成
        if key == 32:
            cv2.imwrite('bg.jpg',frame)
        # 空白キー以外のキーが押されたら終了
        elif key > 0:
            cv2.imwrite("Input.jpg",im_in)
            cv2.imwrite("Background.jpg",im_bg)
            cv2.imwrite("Motion mask.jpg",im_mask)
            cv2.imwrite("Motion Edge.jpg",im_edge)
            break

    # キャプチャー解放
    capture.release()
    # ウィンドウ破棄
    cv2.destroyAllWindows()
