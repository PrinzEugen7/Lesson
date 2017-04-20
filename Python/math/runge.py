# 微分方程式の関数
def dxdt(x):
    c = 0.001
    r = 100
    e = 10
 
    return (e-x)/r/c
 
# ルンゲクッタ法
def runge(x0, t0, tn, n):
    x = x0
    t = t0
    h = (tn - t0) /n
    X = []
    # 漸化式を計算
    for i in range(n):
        d1 = dxdt(x);
        d2 = dxdt(x + d1*h*0.5);
        d3 = dxdt(x + d2*h*0.5);
        d4 = dxdt(x + d3*h);
        x += (d1 + 2 * d2 + 2 * d3 + d4)*(h/6.0); 
        X.append(x)
    return X
 
def main():
    X = runge(0.0, 0.0, 1.0, 100)
    print(X)
 
if __name__ == '__main__':
    main()
