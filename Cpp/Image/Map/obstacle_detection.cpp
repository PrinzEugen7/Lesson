#include <iostream>
#include "opencv2\opencv.hpp"

using namespace cv;

int loadMap(char* fname, int map[][]){
	Mat gray;															// 画像格納用
	Mat im = imread(fname);											// 画像の取得
	cvtColor(im, gray, CV_RGB2GRAY);									// グレースケール変換
	threshold(gray, gray, 0, 255, THRESH_BINARY | THRESH_OTSU); // 2値化
	int h = gray.rows;
	int w = gray.cols;
	int map[200][200];
	for (int y = 0; y < h; y++){
		for (int x = 0; x < w; x++){
			if (gray.data[y * h + x] == 255){
				map[x][y] = 1;
			}
			else{
				map[x][y] = 0;
			}
		}
	}
	return map;
}

int main(int argc, char *argv[])
{
	int map[200][200];
	loadMap("map.jpg", map);
}
