#include <stdio.h>
#include <math.h>

int main(void)
{
    double x = 2.0; 	// 基数
    double y = 0; 
    double a = 2;  	// 指数
    // べき乗の計算(y=x^a)
    y = pow(x, a);
    // 計算結果の表示
    printf("y=%f", y);
  
    return 0;
}
