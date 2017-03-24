import gab.opencv.*;
OpenCV cv;
PImage im;

void setup() {
  // 画像の読み込み
  im = loadImage("test.png");
  cv = new OpenCV(this,im);
  // 画面サイズ
  size(cv.width, cv.height);
  // 読み込んだ画像を表示
  image(im, 0, 0);
}

void draw() {
}
