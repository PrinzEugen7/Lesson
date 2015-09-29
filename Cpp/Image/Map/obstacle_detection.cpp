#include <iostream>
#include <vector>
#include "opencv2\opencv.hpp"

using namespace cv;
using namespace std;

vector<int> loadMap(char* fname){
	Mat gray;													// 画像格納用
	Mat im = imread(fname);										// 画像の取得
	vector<int> map;
	cvtColor(im, gray, CV_RGB2GRAY);							// グレースケール変換
	threshold(gray, gray, 0, 255, THRESH_BINARY | THRESH_OTSU);	// 2値化
	int h = gray.rows;
	int w = gray.cols;
	for (int y = 0; y < h; y++){
		for (int x = 0; x < w; x++){
			if (gray.data[y * h + x] == 255){
				map.push_back(1);
			}
			else{
				map.push_back(0);
			}
		}
	}
	return map;
}

int main(int argc, char *argv[])
{
	vector<int> map;
	map = loadMap("map.jpg");

	// 10個の要素を出力
	for (int i = 0; i < 10; ++i)
	{
		cout << map[i] << endl;
	}
}
