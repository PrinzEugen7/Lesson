PImage img;
// モザイクの窓サイズ
int mosaicWidth = 20;
int mosaicHeight = 20;

// 初期設定
void setup(){
  // 画像の読み込み
  img = loadImage("test.jpg");
  // ウィンドウサイズ（入力画像と同じサイズ）
  size(img.width, img.height);
  // 背景色
  background(0);
  // 表示位置
  image(img, 0, 0);
  loadPixels();
 
  // モザイク処理
  for(int j = 0; j &lt; height; j+=mosaicHeight) {  
    for(int i = 0; i &lt; width; i+=mosaicWidth) {  
      color c = pixels[j * width + i];
      fill(c);
      rect(i, j, mosaicWidth, mosaicHeight);
    }
  }
  // モザイク化画像の保存
  save("mosaic.jpg");
}
 
void draw() {
}
