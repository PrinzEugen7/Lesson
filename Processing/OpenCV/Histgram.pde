import gab.opencv.*;
OpenCV cv;
Histogram grayHist, rHist, gHist, bHist;
PImage im;

void setup() {
  // 画面サイズ
  size(640, 400);
  // 画像の読み込み
  im = loadImage("test.png");
  cv = new OpenCV(this, im);
  // グレースケールのヒストグラムを計算
  grayHist = cv.findHistogram(cv.getGray(), 256);
  // 赤成分のヒストグラムを計算
  rHist = cv.findHistogram(cv.getR(), 256);
  // 緑成分のヒストグラムを計算
  gHist = cv.findHistogram(cv.getG(), 256);
  // 青成分のヒストグラムを計算
  bHist = cv.findHistogram(cv.getB(), 256);
  // 画面を真っ黒に
  background(0);
  // 画像を表示
  image(im, 10, 0, 300, 200);
  // グレールケールのヒストグラムを描画
  stroke(125); noFill();  
  rect(320, 10, 310, 180);  // ヒストグラム欄の外枠を描く
  fill(125); noStroke();
  grayHist.draw(320, 10, 310, 180);  // ヒストグラムの棒を描く
  // 赤成分のヒストグラムを描画
  stroke(255, 0, 0); noFill();  
  rect(10, height - 190, 200, 180);
  fill(255, 0, 0); noStroke();
  rHist.draw(10, height - 190, 200, 180);
  // 緑成分のヒストグラムを描画
  stroke(0, 255, 0); noFill();  
  rect(220, height - 190, 200, 180);
  fill(0, 255, 0); noStroke();
  gHist.draw(220, height - 190, 200, 180);
  // 青成分のヒストグラムを描画
  stroke(0, 0, 255); noFill();  
  rect(430, height - 190, 200, 180);
  fill(0, 0, 255); noStroke();
  bHist.draw(430, height - 190, 200, 180);
}

void draw() {
}
