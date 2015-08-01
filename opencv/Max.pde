import gab.opencv.*;
OpenCV cv;

void setup() {
  // 画像のロード
  PImage im = loadImage("test.jpg");
  // 画面サイズの設定;
  size(im.width, im.height);	
  cv = new OpenCV(this, im);
  image(cv.getOutput(), 0, 0); 
  // 明るさ最大の点を探索
  PVector loc = cv.max();
  stroke(255, 0, 0);
  strokeWeight(4);
  noFill();
  // 明るさ最大の点に円を描画
  ellipse(loc.x, loc.y, 10, 10);  
}

void draw() {
}
