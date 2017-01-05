#include <stdio.h>

int main(void)
{
  int i = 1;

  switch (i)
  {
    case 1:
    printf("iは1です。\n");

    case 2:
    printf("iは2です。\n");
    
    case 3:
    printf("iは3です。\n");
    
    default:
    printf("iは1～3以外です。");
  }
  return 0;
}
