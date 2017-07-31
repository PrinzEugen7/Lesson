#-*- coding:utf-8 -*-
import cv2
import numpy as np

# 大津の手法
def threshold_otsu(gray, min_value=0, max_value=255):

    # ヒストグラムの算出
    hist = [np.sum(gray == i) for i in range(256)]

    s_max = (0,-10)

    for th in range(256):
        
        # クラス1とクラス2の画素数を計算
        n1 = sum(hist[:th])
        n2 = sum(hist[th:])
        
        # クラス1とクラス2の画素値の平均を計算
        if n1 == 0 : mu1 = 0
        else : mu1 = sum([i * hist[i] for i in range(0,th)]) / n1   
        if n2 == 0 : mu2 = 0
        else : mu2 = sum([i * hist[i] for i in range(th, 256)]) / n2

        # クラス間分散の分子を計算
        s = n1 * n2 * (mu1 - mu2) ** 2

        # クラス間分散の分子が最大のとき、クラス間分散の分子と閾値を記録
        if s > s_max[1]:
            s_max = (th, s)
    
    # クラス間分散が最大のときの閾値を取得
    t = s_max[0]

    # 算出した閾値で二値化処理
    gray[gray<t] = min_value
    gray[gray>=t] = max_value

    return gray



def main():
    # 入力画像の読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 方法1（NumPyで実装）
    th1 = threshold_otsu(gray)
    
    # 方法2 （OpenCVで実装）      
    ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)    

    # 結果を出力
    cv2.imwrite("th1.jpg", th1)
    cv2.imwrite("th2.jpg", th2)


if __name__ == "__main__":
    main()
