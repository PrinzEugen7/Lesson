# -*- coding: utf-8 -*-
import cv2
import pylab as plt


def main():
    # 左右画像をグレースケールで取得
    gray_l = cv2.imread("left.png",0)
    gray_r = cv2.imread("right.png",0)
    # 画像のヒストグラム平坦化・平滑化
    gray_l = cv2.GaussianBlur( cv2.equalizeHist(gray_l),(5,5), 0)
    gray_r = cv2.GaussianBlur( cv2.equalizeHist(gray_r),(5,5), 0)
    # セミグローバルブロックマッチング
    window_size = 7
    stereo = cv2.StereoSGBM(
        minDisparity = 0,           # 視差の下限
        numDisparities = 64,        # 最大の上限
        SADWindowSize = window_size,# SADの窓サイズ
        uniquenessRatio = 10,       # パーセント単位で表現されるマージン
        speckleWindowSize = 0,      # 視差領域の最大サイズ
        speckleRange = 16,          # それぞれの連結成分における最大視差値
        disp12MaxDiff = 0,          # left-right 視差チェックにおけて許容される最大の差
        P1 = 8*3*window_size**2,    # 視差のなめらかさを制御するパラメータ1
        P2 = 32*3*window_size**2,   # 視差のなめらかさを制御するパラメータ2
        fullDP = False              # 完全な2パス動的計画法を使うならTrue
    )

    # 視差を求める
    disp = stereo.compute(gray_l, gray_r)
    # 視差データを8bitデータに変換(imshowで表示させるため)
    disp = cv2.normalize(disp, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imshow("disp",disp)                 # 視差画像の表示
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
