#include <stdio.h>
#include <math.h>
  
int main(void)
{
    double x = 1.2345;
    double y;
  
    y = round(x);       // xの四捨五入を計算
  
    printf("y=%f", y);  // 計算結果の表示
  
    return 0;
}
