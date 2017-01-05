#include <stdio.h>

int main(void)
{
  int i = 1;

  switch (i)
  {
    case 1:
    printf("iは1です。\n");
    break;

    case 2:
    printf("iは2です。\n");
    break;
    
    case 3:
    printf("iは3です。\n");
    break;
    
    default:
    printf("iは1～3以外です。");
    break;
  }
  return 0;
}
