PImage img;

void setup(){
  // 画像読み込み
  img = loadImage("test.jpg");
  // ウィンドウサイズ
  size(img.width*2, img.height/2); 
  // 横2倍，縦1/2倍
  img.resize(img.width*2, img.height/2); 
  // 表示
  image(img,0, 0);
  // 保存
  save("resizejpg");
}
