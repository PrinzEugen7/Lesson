import gab.opencv.*;
OpenCV cv;
PImage im;

void setup() {
  // 画像の読み込み
  im = loadImage("test.png");
  cv = new OpenCV(this, im);
  // 画面サイズ
  size(cv.width, cv.height);
}

void draw() {
  // 画像取得
  cv.loadImage(im);
  // 処理したい矩形領域(ROI)を指定
  cv.setROI(mouseX, mouseY, 100, 100);
  // 矩形領域でエッジ検出
  cv.findCannyEdges(20,75);
  // 画面に表示
  image(cv.getOutput(), 0, 0);
}
