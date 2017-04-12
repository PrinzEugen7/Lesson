# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():
    # 係数
    a0 = -0.633099
    a1 = 1.204225

    # サンプルデータ
    x = [1.1, 2.3, 2.8, 4.2, 5.1]
    y = [0.7, 1.9, 3.1, 4.2, 5.6]

    #　近似直線のx値
    xd =np.linspace(1,5,5)

    # 近似直線
    yd = a0 + a1 * xd 

    # グラフ描画
    plt.plot(x,y,"ro") 
    plt.plot(xd,yd,"b-") 
    plt.grid()
    plt.show() 

if __name__ == '__main__':
    main()
