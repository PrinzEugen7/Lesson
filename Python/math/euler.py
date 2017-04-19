# 微分方程式の関数
def dxdt(x):
    c = 0.001
    r = 100
    e = 10
    
    return (e-x)/r/c
 
# オイラー法
def euler(x0, t0, tn, n):

    x = x0
    t = t0
    h = (tn - t0) /n
    X = []
    # 漸化式を計算
    for i in range(n):
        x += dxdt(x) * h
        X.append(x)
        t = t0 + i*h
    return X
    
def main():
    X = euler(0.0, 0.0, 1.0, 100)
    print(X)
    
if __name__ == '__main__':
    main()
