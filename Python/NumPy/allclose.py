# -*- coding: utf-8
import numpy as np

    
def main():
    # 配列生成
    A = np.array([[1, 0],
                  [0, 1]])
    
    B = np.array([[1, 0],
                  [0, 1]])
    
    # 一致判定
    flag =  np.allclose(A, B)
    
    # 結果表示
    print(flag) # True
   
    
if __name__ == "__main__":
    main()
