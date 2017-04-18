import math

# 解を求める関数
def f(x):
   return x*x*x-3*x*x+9*x-8;
 
# 二分法
def bisection_method(a, b, eps):
    s = 0
    for i in range(1000):
        # 収束条件を満たせば終了
        if(abs(a-b)<eps): break
        # 漸化式
        s = (a+b)/2.0
        # 収束条件(近似解の変化が十分小さい)を満たせば計算終了
        if(f(s) * f(a)<0): b = s
        else: a = s
    return s
    
    
def main():
    a = bisection_method(0.0, 2.0, 0.0001) # 1.16595458984375
    print(a)
    
if __name__ == '__main__':
    main()
