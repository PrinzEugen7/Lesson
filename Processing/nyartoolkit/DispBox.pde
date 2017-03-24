import jp.nyatla.nyar4psg.*;
import processing.video.*;

Capture cap;
MultiMarker ar;
int id;

void setup() {
  // 画面サイズ
  size(640,480,P3D);
  // カメラのキャプチャ
  cap = new Capture(this, width, height);
  ar = new MultiMarker(this, width, height, "camera_para.dat", NyAR4PsgConfig.CONFIG_PSG);
  // 検出するARマーカーの登録
  id = ar.addARMarker("patt.hiro", 60);
  // カメラの起動
  cap.start();
}

void draw() {
   // エラー処理（カメラ利用できなかった場合）
  if (cap.available() == false) return;
  // カメラから映像を取得
  cap.read();
  // 背景描画
  background(0);
  ar.drawBackground(cap);
  // マーカーの検出
  ar.detect(cap);
  // マーカーが存在した場合
  if (ar.isExistMarker(id)) {
    // マーカー上に箱を描画
    ar.beginTransform(id);
    fill(116,163,241,100);
    translate(0,0,15);
    box(30);
    ar.endTransform();
  }
}
