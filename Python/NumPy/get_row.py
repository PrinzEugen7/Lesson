# -*- coding: utf-8
import numpy as np

def main():
    # 2次元配列
    A = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])

    # 1行目の値を取り出し
    a1 = A[0]
    # 結果表示
    print(a1) # [1 2]

if __name__ == "__main__":
    main()
