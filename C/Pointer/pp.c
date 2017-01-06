#include <stdio.h>

int main(void){

	int *ps1;
	int **ps2;

	int score1[3] = {10, 20, 30};
	int score2[3] = {40, 50, 60};

	// score1のポインタを代入
	ps1 = score1;

	// ps1(ポインタ)のポインタをps2に代入
	ps2 = &ps1;

	// ps2(ポインタのポインタ)にscore2の先頭要素のアドレスを格納
	*ps2 = score2;

	// 表示
	printf("%d\n",&ps1);

	return 0;

}
