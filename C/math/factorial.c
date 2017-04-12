#include <stdio.h>

// 階乗(n!)の計算
int factorial(int n)
{
    int x = 1;
 
    while(n > 1){
        x = x * n;
        n--;
    }
 
    return x;
}
 
int main()
{
    int n = 5;

    printf("%d!=%d", n, factorial(n)); // 5!=120
 
    return 0;
}
