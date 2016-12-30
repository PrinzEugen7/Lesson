#include <stdio.h>

int main(void)
{
  double x = 1.23;  // 変数xの宣言・初期化
  double y = 4.56;  // 変数yの宣言・初期化
  
  printf("%f\n", x);  // 変数の中身のみ表示
  printf("xは%f\n", x); // 任意の文字列と変数の中身を表示
  printf("xは%f yは%f", x, y); // 任意の文字列と複数の変数の中身を表示
  
  return 0;
}
