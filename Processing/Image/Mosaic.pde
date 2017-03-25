PImage img;
// モザイクの窓サイズ
int mosaicWidth = 20;
int mosaicHeight = 20;

void setup(){ 
  img = loadImage("test.jpg");    // 入力画像の読み込み 
  surface.setResizable(true);
  surface.setSize(img.width, img.height);   // 画面サイズ
} 
 
void draw(){
  // 背景色
  background(0);
  // 表示位置
  image(img, 0, 0);
  
  loadPixels();
 
  // モザイク処理
  for(int j = 0; j < height; j+=mosaicHeight) {  
    for(int i = 0; i < width; i+=mosaicWidth) {  
      color c = pixels[j * width + i];
      fill(c);
      rect(i, j, mosaicWidth, mosaicHeight);
    }
  }
} 
 
