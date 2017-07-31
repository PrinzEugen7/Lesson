#-*- coding:utf-8 -*-
import cv2
import numpy as np

# 膨張処理
def threshold_otsu(gray, min_value=0, max_value=255):

    # ヒストグラム算出
    hist = [np.sum(gray == i) for i in range(256)]

    s_max = (0,-10)
    ss = []
    
    for th in range(256):
        # update
        w0 = sum(hist[:th])
        w1 = sum(hist[th:])

        mu0 = sum([i * hist[i] for i in range(0,th)]) / w0 if w0 > 0 else 0       
        mu1 = sum([i * hist[i] for i in range(th, 256)]) / w1 if w1 > 0 else 0

        # calculate 
        s = w0 * w1 * (mu0 - mu1) ** 2
        ss.append(s)

        if s > s_max[1]:
            s_max = (th, s)
            
    t = s_max[0]

    # 算出した閾値で2値化
    gray[gray<t] = min_value
    gray[gray>=t] = max_value
    
    return gray


def main():
    # 入力画像の読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 方法1
    th1 = threshold_otsu(gray, 0, 255)
    
    # 方法2       
    ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)    

    # 結果を出力
    cv2.imwrite("th1.jpg", th1)
    cv2.imwrite("th2.jpg", th2)


if __name__ == "__main__":
    main()

