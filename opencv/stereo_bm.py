# -*- coding: utf-8 -*-
import cv2

def main():
    # 画像取得
    gray_l = cv2.imread("left.png",0)
    gray_r = cv2.imread("right.png",0)
    # 画像のヒストグラム平坦化・平滑化
    gray_l = cv2.GaussianBlur( cv2.equalizeHist(gray_l),(5,5), 0)
    gray_r = cv2.GaussianBlur( cv2.equalizeHist(gray_r),(5,5), 0)
    # BM法でステレオ対応点探索
    stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET,ndisparities=32, SADWindowSize=21)
    disp = stereo.compute(gray_l,gray_r)    # 視差を計算
    # 視差データを8bitデータに変換(imshowで表示させるため)
    disp = cv2.normalize(disp, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imshow("disp",disp)                 # 視差画像の表示
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
