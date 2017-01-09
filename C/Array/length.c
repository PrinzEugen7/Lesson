#include <stdio.h>
 
int main(void)
{
    int data[] = {1,2,3,4,5};
    int N = sizeof(data) / sizeof(data[0]);
     
    printf("配列の長さは%d", N);
 
    return 0;
}
