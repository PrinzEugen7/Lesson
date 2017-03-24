import gab.opencv.*;
OpenCV cv;
PImage im, th;
ArrayList<contour> contours;
 
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
  image(th, 0, 0);
  // 2値画像から輪郭抽出
  contours = cv.findContours();
  noFill();
  strokeWeight(3);
  // 抽出した輪郭を赤色で塗る
  for (Contour contour : contours) {
    stroke(200,0,0);
    contour.draw();
  }
}
 
void draw() {
}
