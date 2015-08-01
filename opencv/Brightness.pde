import gab.opencv.*;
PImage im;
OpenCV cv;

void setup(){
  // 画像のロード
  im = loadImage("test.jpg")
  // 画面サイズ;
  size(im.width, im.height);
  cv = new OpenCV(this, im);  
}

void draw(){
  cv.loadImage(im);
  // マウスの座標で明るさを設定
  cv.brightness((int)map(mouseX, 0, width, -255, 255));
  // 明るさを変更した画像を画面に出力
  image(cv.getOutput(),0,0);
}
