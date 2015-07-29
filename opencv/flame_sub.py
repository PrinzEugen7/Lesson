# -*- coding: utf-8 -*-
import cv2
import numpy as np

def flame_sub(im1,im2,im3,th,blur):

    d1 = cv2.absdiff(im3, im2)
    d2 = cv2.absdiff(im2, im1)
    diff = cv2.bitwise_and(d1, d2)
    # 差分が閾値より小さければTrue
    mask = diff < th
    # 背景画像と同じサイズの配列生成
    im_mask = np.empty((im1.shape[0],im1.shape[1]),np.uint8)
    im_mask[:][:]=255
    # Trueの部分（背景）は黒塗り
    im_mask[mask]=0
    # ゴマ塩ノイズ除去
    im_mask = cv2.medianBlur(im_mask,blur)

    return  im_mask


if __name__ == '__main__':

    cam = cv2.VideoCapture(0)
    im1 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    im2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    im3 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    while True:
        # フレーム間差分計算
        im_fs = flame_sub(im1,im2,im3,5,7)
        cv2.imshow("Input",im2)
        cv2.imshow("Motion Mask",im_fs)
        im1 = im2
        im2 = im3
        im3 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
        key = cv2.waitKey(10)
        # Escキーが押されたら
        if key == 27:
            cv2.imwrite("input.jpg",im3)
            cv2.imwrite("frame_sub.jpg",im_fs)
            cv2.destroyAllWindows()
            break
