#include <stdio.h>

int main(void)
{
  char x = 'X';  // 変数xの宣言・初期化
  char y = 'Y';  // 変数yの宣言・初期化
  
  printf("%c\n", x);  // 変数の中身のみ表示
  printf("xは%c\n", x); // 任意の文字列と変数の中身を表示
  printf("xは%c yは%c", x, y); // 任意の文字列と複数の変数の中身を表示
  
  return 0;
}
