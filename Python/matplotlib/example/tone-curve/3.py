#-*- coding:utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

    
def main():

    # xの値を格納したNumPyリスト
    x = np.linspace(0,255,256)
    # yの値を計算
    a1, a2 = 1.3, 0.7
    y = x
    y1 = a1*(x-127) + 127
    y2 = a2*(x-127) + 127
    # フォントの種類
    plt.rcParams["font.family"] = "Times New Roman"

    # アス比を1:1に固定
    plt.axes().set_aspect('equal')

    # 線を引く
    plt.plot(x, y, "k-", label="$a=0$",linewidth=2)
    plt.plot(x, y1, "r--", label="$a=1.3$", linewidth=2)
    plt.plot(x, y2, "b--", label="$a=0.7$", linewidth=2)

    # 軸の設定
    plt.xlim(0, 255)
    plt.ylim(0, 255)
    plt.xticks([0, 127, 255], fontsize = 30)
    plt.yticks([0, 127, 255], fontsize = 30)
    plt.xlabel('$I(x,y)$', fontsize=40)
    plt.ylabel('$I\'(x,y)$', fontsize=40)

    # グリッドの描画
    plt.grid()

    # 凡例表示
    plt.legend(loc=2, fontsize=30)

    # グラフ表示
    plt.show()

    
if __name__ == "__main__":
    main()
