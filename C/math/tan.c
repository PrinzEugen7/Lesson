#include <stdio.h>
#include <math.h>
  
int main(void)
{
    double x = 3.14;    // ラジアン
    double y;
  
    y = tan(x);         // 正接の計算
  
    printf("y=%f", y);  // 計算結果の表示
  
    return 0;
}
