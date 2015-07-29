import jp.nyatla.nyar4psg.*;
import processing.video.*;
import saito.objloader.*;

Capture cap;
MultiMarker ar;
int id;          // ARマーカーのID番号
OBJModel model;
 
// 初期設定
void setup(){
  size(640,480,P3D);                // 画面サイズ
  // カメラの設定
  cap = new Capture(this, width, height);  // カメラのキャプチャ
  cap.start();                      // カメラの起動
  // ARマーカーの設定
  ar = new MultiMarker(this, width, height, "camera_para.dat", NyAR4PsgConfig.CONFIG_PSG);
  id = ar.addARMarker("patt.kanji", 60);  // 検出するARマーカーの登録
  // 3Dモデル(OBJ)の設定
  model = new OBJModel(this, "test.obj", "absolute", TRIANGLES);  // OBJファイルの読み込み
  model.enableDebug();
  model.scale(5);          // 表示するモデルの大きさ
  model.translateToCenter();  // 中央に配置
  stroke(255);
  noStroke();
}
 
void draw(){
   // エラー処理（カメラ利用できなかった場合）
  if (cap.available() == false) return;
  
  cap.read();              // カメラから映像を取得
  lights();                // 照明追加
  ar.drawBackground(cap);
  ar.detect(cap);            // マーカーの検出
  // マーカーが存在した場合
  if (ar.isExistMarker(id)) {
    ar.beginTransform(id);      // マーカー上に箱を描画
    pushMatrix();            // 座標保存
    rotateX(-3.14/2);       // オブジェクトの回転
    rotateY(0);
    model.draw();            // 3Dモデルの描画
    popMatrix();            // 座標保存
    ar.endTransform();
  }
}
