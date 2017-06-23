#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

    
def main():
    # 画像ファイルを8bitで読み込む
    gray = cv2.imread('input1.jpg', 0)
    #　画像ヒストグラムの作成
    plt.rcParams["font.family"] = "Times New Roman"
    plt.hist(gray.ravel(),256,[0,256])
    plt.xlim(0, 255)
    plt.ylim(0, 600)
    plt.xticks(fontsize = 17)
    plt.yticks(fontsize = 17)
    plt.xlabel('Pixel value', fontsize=20)
    plt.ylabel('Number of pixels', fontsize=20)
    plt.grid()
    plt.show()

    
if __name__ == "__main__":
    main()
