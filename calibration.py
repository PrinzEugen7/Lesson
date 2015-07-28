# -*- coding: utf-8 -*-
import numpy as np
import cv2
from glob import glob

def main():

    square_size = 1.0      # 正方形のサイズ
    pattern_size = (9, 6)  # 模様のサイズ
    pattern_points = np.zeros( (np.prod(pattern_size), 3), np.float32 )
    pattern_points[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size
    obj_points = []
    img_points = []

    for fn in glob("*.jpg"):
        # 画像の取得
        im = cv2.imread(fn, 0)
        print "loading..." + fn
        # チェスボードのコーナーを検出
        found, corner = cv2.findChessboardCorners(im, pattern_size)
        # コーナーがあれば
        if found:
            term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
            cv2.cornerSubPix(im, corner, (5,5), (-1,-1), term)
        # コーナーがない場合のエラー処理
        if not found:
            print 'chessboard not found'
            continue
        img_points.append(corner.reshape(-1, 2))
        obj_points.append(pattern_points)

    # 内部パラメータを計算
    rms, K, d, r, t = cv2.calibrateCamera(obj_points,img_points,(im.shape[1],im.shape[0]))
    # 計算結果を表示
    print "RMS = ", rms
    print "K = \n", K
    print "d = ", d.ravel()

if __name__ == '__main__':
    main()
