#include <stdio.h>
#include <math.h>
  
int main(void)
{
  double x = 0;
  double y = 1;
  
  x = acos(y);        // 逆余弦の計算
  
  printf("y=%f", x);  // 計算結果の表示
  
  return 0;
}
