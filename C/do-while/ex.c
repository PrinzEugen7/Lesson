#include <stdio.h>

int main(void)
{
  int i = 1;

  // iが5になるまで反復処理
  do{
    printf("%d回目の実行\n", i);
    i++; // i = i + 1;と同じ  	
  } while(i<=5);
  return 0;
}
