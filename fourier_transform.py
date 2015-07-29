# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    # 画像をグレースケールで取得
    gray = cv2.imread("test.png",0)
    # グレースケール画像を高速フーリエ変換
    fshift = np.fft.fftshift(np.fft.fft2(gray))
    fft = 20*np.log(np.abs(fshift))
    # パワースペクトルを正規化(imshowで表示可能な8bit画像に変換)
    fft = cv2.normalize(fft, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # 画面表示
    cv2.imshow("INPUT",gray)
    cv2.imshow("Magnitude Spectrum",fft)
    cv2.waitKey(0)                      # キー入力待機
    cv2.destroyAllWindows()             # ウィンドウ破棄

if __name__ == '__main__':
    main()
