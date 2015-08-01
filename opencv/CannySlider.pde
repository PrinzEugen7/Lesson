import gab.opencv.*;
import controlP5.*;

ControlP5 cp5;
OpenCV cv;
PImage im, im2;
int th1=0;  // 閾値1
int th2=0;  // 閾値2

void setup() {
  // 入力画像の取得
  im = loadImage("test.png");
  // ウィンドウの作成
  size(im.width, im.height);
  // スライダーの作成
  cp5 = new ControlP5(this);
  cp5.addSlider("th1",0,255,128,10,10,100,30);
  cp5.addSlider("th2",0,255,128,10,50,100,30);
}

void draw() {
  cv = new OpenCV(this, im);
  // 画像のエッジを検出
  cv.findCannyEdges(th1,th2);
  // エッジ画像を取得
  im2 = cv.getSnapshot();
  // エッジ画像を表示
  image(im2, 0, 0);
}
