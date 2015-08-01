import gab.opencv.*;
OpenCV cv;
PImage im;

void setup() {
  // 画像の読み込み
  im = loadImage("test.png");
  cv = new OpenCV(this, im);
  // 画面サイズ
  size(im.width,im.height);
  // 画像データをRGBカラーで扱う
  cv.useColor(RGB); 
  im = cv.getSnapshot();
  // 画像を画面に表示
  image(im,0,0);
}

void draw() {
}
