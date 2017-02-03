#include <stdio.h>

int main()
{ 　　// 変数xはこの括弧内で有効
    int x = 10;
    { 　　// 変数yはこの括弧内で有効
        int y = 5;
          
    }
    // 変数yはこの範囲では使えない
    return 0;
}
