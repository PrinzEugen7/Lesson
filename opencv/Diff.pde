import gab.opencv.*;
OpenCV opencv;
PImage  bg, fg, grayDiff;

void setup() {
  // 背景画像の取得
  bg = loadImage("bg.png");
  // 前景画像の取得
  fg = loadImage("fg.png");
  // 画面サイズ
  size(bg.width, bg.height);
  cv = new OpenCV(this, bg);  
  // 前景と背景の差分を計算  
  cv.diff(fg);
  grayDiff = cv.getSnapshot(); 
  // 差分画像の表示
  image(grayDiff, 0, 0);
}

void draw() {
}
