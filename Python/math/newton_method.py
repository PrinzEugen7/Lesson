# 解を求める関数
def f(x):
    return x*x - 4.0
 
# 導関数
def df(x):
    return 2.0*x

# ニュートン法
def newton_method(a, eps):
    for i in range(1000):
    	  # 漸化式
        ah = a - f(a)/df(a)
        # 収束条件(近似解の変化が十分小さい)を満たせば計算終了
        if abs(ah - a) < eps:break
        #　近似解の更新
        a = ah      
    return a, i
    
    
def main():
    a , i = newton_method(1.0, 0.0001)
    print("解:",a ,"(計算回数:", i+1, ")") # 解: 2.00000... (計算回数: 5 )
    
if __name__ == '__main__':
    main()
