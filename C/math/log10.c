#include <stdio.h>
#include <math.h>
 
int main(void)
{
    double x = 10;
    double y = 0; 
    // 10を底とする対数の計算
    y = log10(x);
    // 計算結果の表示
    printf("y=%f", y);
  
    return 0;
}
