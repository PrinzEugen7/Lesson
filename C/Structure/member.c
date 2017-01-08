#include<stdio.h>

int main()
{
    // 構造体の定義
    typedef struct score{
        int english;      // 英語のと得点
        int math;         // 数学の得点
        char name[10];    // 受験者氏名
    }SCORE;
    
    // 構造体の宣言・初期化
    SCORE scores = {80, 91, "Ayase"};
    
    // 各メンバのデータを表示
    printf("英語の得点：%d\n", scores.english);
    printf("数学の得点：%d\n", scores.math);
    printf("受験者氏名：%s\n", scores.name);
    
    // メンバにデータを代入（更新）
    scores.english = 88;
    scores.math = 90;
    
    // 各メンバのデータを表示
    printf("英語の得点：%d\n", scores.english);
    printf("数学の得点：%d\n", scores.math);
    printf("受験者氏名：%s\n", scores.name);
    
    return 0;
}
