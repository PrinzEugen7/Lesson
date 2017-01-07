#include <stdio.h>

// グローバル変数の宣言
int x = 10;
int y = 20;

int test()
{
  // ローカル変数の宣言
  int z = 0;
  
  z = x + y;
  
  return 0;
}

int main()
{
  // ローカル変数の宣言
  int z = 0;
  
  z = x - y;
  
  return 0;
}
