import gab.opencv.*;
 
OpenCV cv;
ArrayList<line> lines;
 
void setup() {
  // 画像取得
  PImage im = loadImage("test.png");
  //　ウィンドウ作成
  size(im.width, im.height);
  cv = new OpenCV(this, im);
  // エッジ検出
  cv.findCannyEdges(20, 75);
  // 直線の検出
  lines = cv.findLines(100, 30, 20);
  image(cv.getOutput(), 0, 0);
  // 線の太さ
  strokeWeight(3);
  for (Line line : lines) {
      stroke(0, 255, 0);
      line(line.start.x, line.start.y, line.end.x, line.end.y);
  }
}
 
void draw() {
}
