float cx, cy, deg;
PImage im;

void setup() {
  // 画面サイズ
  size(400, 400);
  // 画面中央の座標
  cx = width/2;
  cy = height/2;
  // 入力画像を取得
  im = loadImage("test.png");
  // 画像を画面中央に配置
  imageMode(CENTER);
}

void draw() {
  // 画面クリア
  background(0);
  // 座標の保存
  pushMatrix();
  translate(cx, cy);
  rotate(frameCount / 100.0);
  image(im, 0, 0, cx, cy);
  popMatrix();
  // 座標の保存
  pushMatrix();
  // 回転角の増加
  deg = deg + 3;
  // 画面中央を回転中心としてdegだけ回転
  translate(cx, cy);
  rotate(-radians(deg));
  // 座標を元に戻す
  popMatrix();
}
