#include <stdio.h>

int main(void)
{
  int i = 1;

  // iが5になるまで反復処理
  while(i<=5){ 
    printf("%d回目の実行\n", i);
    i++; // i = i + 1;と同じ
  }
  return 0;
}
