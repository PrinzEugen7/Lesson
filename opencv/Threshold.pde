import gab.opencv.*;
OpenCV cv;
PImage im, th;

void setup() {
  // 画像の読み込み
  im = loadImage("test.jpg");
  // 画面サイズ  
  size(im.width, im.height);
  cv = new OpenCV(this,im);
  // グレースケール変換
  cv.gray();
  // 2値化
  cv.threshold(150);
  th = cv.getOutput();
  // 画面に2値画像を表示
  image(th, 0, 0);
}

void draw() {
}
