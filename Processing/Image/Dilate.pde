
PImage im, gray; 
 
void setup(){ 
  im = loadImage("test.jpg");    // 入力画像の読み込み 
  surface.setResizable(true);
  surface.setSize(im.width, im.height);   // 画面サイズ
} 
 
void draw(){
  image(im, 0, 0);
  filter(DILATE);
} 
