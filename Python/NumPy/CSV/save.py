# -*- coding: utf-8
import numpy as np
    
def main():
    A = np.array([[1, 2],
                  [3, 4],
                  [5, 6]])

    np.savetxt('data1.csv', A, delimiter=",")
    np.savetxt('data2.csv', A.T, delimiter=",")

if __name__ == "__main__":
    main()
