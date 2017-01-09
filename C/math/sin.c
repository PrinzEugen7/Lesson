#include <stdio.h>
#include <math.h>
  
int main(void)
{
    // 変数宣言
    double x = 1.57;    // ラジアン
    double y;

    y = sin(x);         // 正弦の計算

    printf("y=%f", y);  // 計算結果の表示

    return 0;
}
