#include <stdio.h>
#include <math.h>
  
int main(void)
{
    double x = 1.57;    // ラジアン
    double y;
    
    y = cos(x);         // 余弦の計算
    
    printf("y=%f", y);  // 計算結果の表示
    
    return 0;
}
