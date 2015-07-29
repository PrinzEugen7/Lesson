import saito.objloader.*;
OBJModel model;
float rotX, rotY;

// 初期設定
void setup(){
  // 画面サイズ
  size(400, 300, P3D);
  // フレームレート
  frameRate(30);
  // OBJファイルの読み込み
  model = new OBJModel(this, "test.obj", "absolute", TRIANGLES);
  model.enableDebug();
  // 座標保存
  model.scale(20);
  model.translateToCenter();  // 中央に配置
  stroke(255);
  noStroke();
}

void draw(){
  // 背景色
  background(0,0,0);
  // 照明追加
  lights();
  // 座標保存
  pushMatrix();
  // オブジェクトの移動，回転
  translate(width/2, height/2, 0);
  rotateX(rotY);
  rotateY(rotX);
  // モデルの描画
  model.draw();
  // 座標保存
  popMatrix();
}

// マウスドラッグ時の処理
void mouseDragged(){
  rotX += (mouseX - pmouseX) * 0.01;
  rotY -= (mouseY - pmouseY) * 0.01;
}
