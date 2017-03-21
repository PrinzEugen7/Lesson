# -*- coding: utf-8
import numpy as np

    
def main():
    # 配列生成
    A = np.array([[1, 0],
                  [0, 1]])
    
    A.flags.writeable = False
    
    A[0, 0] = 5
    
    # 結果表示
    print(A)
   
    
if __name__ == "__main__":
    main()
