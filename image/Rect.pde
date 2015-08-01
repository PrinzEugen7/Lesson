void setup() {
  // 画面サイズ
  size(400, 400);
  // 画面クリア
  background(0, 0, 0);
  // 線幅 
  strokeWeight(5);
  // 角の設定
  // strokeJoin(MITER)  // 留め継ぎ(デフォルト)
  // strokeJoin(BEVEL)  // 斜角
  strokeJoin(ROUND);    // 丸く
  // 線色(緑)
  stroke(0, 130, 0);
  // 塗りつぶし設定
  //noFill();             // 塗りつぶし無し
  fill(0, 50, 0);       // 塗りつぶし有り（深緑色）
  // 矩形の描画(左上頂点のx座標, 左上頂点のy座標, 幅, 高さ)
  rect(60, 80, 240, 180);
}

void draw() {
}
