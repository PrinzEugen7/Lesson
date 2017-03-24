void setup() {
  // 画面サイズ
  size(400, 400);
  // 画面クリア
  background(0, 0, 0);
  // 線幅 
  strokeWeight(5);
  // 線色(緑)
  stroke(0, 130, 0);
  // 塗りつぶし設定
  //noFill();             // 塗りつぶし無し
  fill(0, 50, 0);       // 塗りつぶし有り（深緑色）
  // 円の描画(中心のx座標, 中心のy座標, 幅, 高さ)
  ellipse(200, 200, 100, 100);
}
 
void draw() {
}
