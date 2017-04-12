# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():
    a0 = -0.633099
    a1 = 1.204225
    x = [1.1, 2.3, 2.8, 4.2, 5.1];
    y = [0.7, 1.9, 3.1, 4.2, 5.6];
    xd = [1, 2, 3, 4, 5];
    yh = a0 + a1*xh               # 直線の式
    plt.plot(x,y,"r-")      # 直線を引く
    plt.show()              # グラフ表示

if __name__ == '__main__':
    main()
