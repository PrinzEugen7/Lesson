# -*- coding: utf-8 -*-
import cv2
import numpy as np
import pylab as plt

# ヒストグラムの計算
def calc_hist(im):

    hist = [0]*256
    h = im.shape[0] # 画像の高さ
    w = im.shape[1] # 画像の幅

    for x in range(w):
        for y in range(h):
            # その画素値のヒストグラムの値を１増加
            hist[im[y,x]] += 1

    return hist

# ヒストグラム平坦化
def hist_equal(im,hist):

    F = [0]*256
    S = 0
    h = im.shape[0] # 画像の高さ
    w = im.shape[1] # 画像の幅

    im_eq = np.zeros((h,w),np.uint8)
    # ヒストグラムの積分を計算し，結果をFに記録
    for v in range(255):
        S += hist[v]
        F[v] = S

    # Fの各要素に255/Sを掛ける
    for v in range(255):
        F[v] = (F[v]*255)/S

    # 画像中の画素の一個ずつに対し，その画素値を変換
    for x in range(w):
        for y in range(h):
            im_eq[y,x]=F[im[y,x]]

    return im_eq

# 結果の表示
def show_result(im,hist_im,im_eq,hist_imeq):

    graph = plt.figure()
    plt.rcParams["font.size"]=17
    # 入力画像
    plt.subplot(2,2,1),plt.imshow(im,"gray")
    plt.title("Input Image")
    # 平坦化画像
    plt.subplot(2,2,2),plt.imshow(im_eq,"gray")
    plt.title("Histogram Equalization Image")
    # ヒストグラム(入力)
    plt.subplot(2,2,3),plt.plot(hist_im)
    plt.xlim(0,255),plt.title("Histogram")
    # ヒストグラム(平坦化)
    plt.subplot(2,2,4),plt.plot(hist_imeq)
    plt.xlim(0,255),plt.title("Equalization Histogram")
    plt.show()


if __name__ == '__main__':

    # 画像取得
    im = cv2.imread("input.jpg",0)
    # ヒストグラムを計算
    hist = calc_hist(im)
    # ヒストグラムを平坦化
    im_eq = hist_equal(im,hist)
    # 平坦化処理した画像のヒストグラムを計算
    hist_eq = calc_hist(im_eq)
    show_result(im,hist,im_eq,hist_eq)
