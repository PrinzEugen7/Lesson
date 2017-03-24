import gab.opencv.*;

OpenCV cv;
PImage im, im2;

void setup() {
  // 入力画像の取得
  im = loadImage("test.png");
  // ウィンドウの作成
  size(im.width, im.height);
  cv = new OpenCV(this, im);
  // 画像のエッジを検出
  cv.findCannyEdges(20,75);
  // エッジ画像を取得
  im2 = cv.getSnapshot();
  // エッジ画像を表示
  image(im2, 0, 0);
}

void draw() {
}
