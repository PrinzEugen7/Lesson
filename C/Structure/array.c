#include<stdio.h>

int main()
{
    // 変数の宣言
    int i = 0;
    
    // 構造体の定義
    typedef struct score{
        int english;      // 英語のと得点
        int math;         // 数学の得点
        char name[10];    // 受験者氏名
    }SCORE;
    
    // 構造体配列の宣言・初期化
    SCORE scores[3] = {
       {80, 91, "Ayase"},
       {84, 81, "Kirino"},
       {72, 71, "Kuroneko"}
    };
    
    // 各メンバのデータを表示
    for(i = 0; i < 3; i++){
        printf("受験者氏名：%s\n", scores[i].name);
        printf("英語の得点：%d\n", scores[i].english);
        printf("数学の得点：%d\n", scores[i].math);
        printf("------------------\n");
    }
    
    // メンバにデータを代入（更新）
    scores[0].english = 88;
    scores[1].math = 90;
    
    // 各メンバのデータを表示
    for(i = 0; i < 3; i++){
        printf("受験者氏名：%s\n", scores[i].name);
        printf("英語の得点：%d\n", scores[i].english);
        printf("数学の得点：%d\n", scores[i].math);
        printf("------------------\n");
    }
    
    return 0;
}
