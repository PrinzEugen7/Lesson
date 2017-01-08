#include<stdio.h>

int main()
{
    // 構造体の定義
    struct score{
        int english;
        int math;
        char name[10];
    }SCORE;
    
    // 構造体の宣言・初期化
    SCORE scores = {80, 91, "Ayase"};
    
    return 0;
}
