# -*- coding: utf-8
import numpy as np

    
def main():
    # 配列生成
    A = np.array([0, 1, 1, 1, 2, 0, 0])
    
    # 値が0でない要素数をカウント
    num = np.count_nonzero(A)
    
    # 結果表示
    print(num) # 4
   
    
if __name__ == "__main__":
    main()
