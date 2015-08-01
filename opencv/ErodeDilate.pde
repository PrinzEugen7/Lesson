import gab.opencv.*;

PImage im, im2;
OpenCV cv;

void setup() {
  // 画像の取得
  im = loadImage("test.png"); 
  // 画面サイズ
  size(im.width, im.height);
  cv = new OpenCV(this, im);
  // グレースケール変換，2値化
  cv.gray();
  cv.threshold(100);
  // 膨張収縮化処理(白色領域が減少→増加)
  cv.erode();
  cv.dilate();
  // 画像を表示
  im2 = cv.getSnapshot();
  image(im2, 0, 0);
}

void draw() {
}
