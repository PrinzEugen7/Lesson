#include <stdio.h>
#include <math.h>
 
int main(void)
{
    double x = 2.0;
    double y = 0; 
    // 2を底とする対数の計算
    y = log2(x);
    // 計算結果の表示
    printf("y=%f", y);
  
    return 0;
}
