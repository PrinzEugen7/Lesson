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

# ヒストグラムの計算
def calc_hist_rgb(im):

    # RGB毎にヒストグラムを格納する配列
    h_b = [0]*256;h_g = [0]*256;h_r = [0]*256;
    for x in range(im.shape[1]): # 画像の幅
        for y in range(im.shape[0]): # 画像の高さ
            # 画素値毎にヒストグラムの値を計算
            h_b[im[y,x,0]] += 1
            h_g[im[y,x,1]] += 1
            h_r[im[y,x,2]] += 1

    return h_b,h_g,h_r

# ヒストグラム平坦化
def hist_equal_rgb(im,h_b,h_g,h_r):

    F_b = [0]*256;F_g = [0]*256;F_r = [0]*256;
    S_b=0;S_g=0;S_r=0;
    h = im.shape[0] # 入力画像の高さ
    w = im.shape[1] # 入力画像の幅
    d = im.shape[2] # 入力画像の次元

    # 入力画像と同じサイズの画像オブジェクトを生成
    im_eq = np.zeros((h,w,d),np.uint8)

    # ヒストグラムの積分を計算し，結果をFに記録
    for v in range(255):
        S_b += h_b[v]; F_b[v] = S_b;
        S_g += h_g[v]; F_g[v] = S_g;
        S_r += h_r[v]; F_r[v] = S_r;

    # Fの各要素に255/Sを掛ける
    for v in range(255):
        F_b[v] = (F_b[v]*255)/S_b
        F_g[v] = (F_g[v]*255)/S_g
        F_r[v] = (F_r[v]*255)/S_r

    # 画像中の画素の一個ずつに対し，その画素値を変換
    for x in range(w):
        for y in range(h):
            im_eq[y,x,0]=F_b[im[y,x,0]]
            im_eq[y,x,1]=F_g[im[y,x,1]]
            im_eq[y,x,2]=F_r[im[y,x,2]]

    return im_eq

def bgr2rbg(im):
    b,g,r = cv2.split(im)       # get b,g,r
    im = cv2.merge([r,g,b])     # switch it to rgb

    return im

# 結果の表示
def show_result_rgb(im,h_b,h_g,h_r,im_eq,h_be,h_ge,h_re):

    graph = plt.figure()
    plt.rcParams["font.size"]=15
    # 入力画像
    plt.subplot(2,2,1),plt.imshow(bgr2rbg(im))
    plt.title("Input Image")
    # 平坦化画像
    plt.subplot(2,2,2),plt.imshow(bgr2rbg(im_eq))
    plt.title("Histogram Equalization Image")
    # ヒストグラム
    plt.subplot(2,2,3),plt.plot(h_b,"b", h_g,"g", h_r,"r")
    plt.xlim(0,255),plt.title("Histogram")
    plt.legend(["Blue","Green","Red"])
    # 平坦化ヒストグラム
    plt.subplot(2,2,4),plt.plot(h_be,"b", h_ge,"g", h_re,"r")
    plt.xlim(0,255),plt.title("Equalization Histogram")
    plt.legend(["Blue","Green","Red"])
    plt.show()

if __name__ == '__main__':

    # 画像取得
    im = cv2.imread("input.jpg")

    if im.ndim == 2: # 入力画像の次元が2(単色)のとき
        # ヒストグラムを計算
        hist = calc_hist(im)
        # ヒストグラムを平坦化
        im_eq = hist_equal(im,hist)
        # 平坦化処理した画像のヒストグラムを計算
        hist_eq = calc_hist(im_eq)
        # 結果表示
        show_result(im,hist,im_eq,hist_eq)

    elif im.ndim == 3: # 入力画像の次元が3(カラー)のとき
        # 入力画像のヒストグラムを計算
        h_b,h_g,h_r = calc_hist_rgb(im)
        # ヒストグラム平坦化された画像の生成
        im_eq = hist_equal_rgb(im,h_b,h_g,h_r)
        # 平坦化画像のヒストグラムを計算
        h_be,h_ge,h_re = calc_hist_rgb(im_eq)
        # 結果表示
        show_result_rgb(im,h_b,h_g,h_r,im_eq,h_be,h_ge,h_re)

    else:
        print "Not found such RGB or MONO image"
