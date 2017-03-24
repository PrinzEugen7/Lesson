import gab.opencv.*;
OpenCV cv;
PImage im, r, g, b;
 
void setup() {
  // 画像の読み込み
  im = loadImage("test.png");
  cv = new OpenCV(this, im);
  // 画面サイズ
  size(im.width*2,im.height*2);
  // 画像データをRGBカラーで扱う
  cv.useColor(RGB);
  r = cv.getSnapshot(cv.getR());
  g = cv.getSnapshot(cv.getG());
  b = cv.getSnapshot(cv.getB());  
  // 画像を画面に表示
  image(im,0,0);
  // R成分のみ表示
  tint(255,0,0);
  image(r,im.width,0);
  // G成分のみ表示
  tint(0,255,0);
  image(g,0,im.height);
  // B成分のみ表示
  tint(0,0,255);
  image(b,im.width,im.height);
}
 
void draw() {}
