
PImage im, gray; 
 
void setup(){ 
  im = loadImage("test.jpg");    // 入力画像の読み込み 
  size(480, 270);   // 画面サイズ
  size(im.width, im.height);
  image(im, 0, 0);
  filter(DILATE);
} 
 
void draw(){ 
} 

