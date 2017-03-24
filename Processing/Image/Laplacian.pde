PImage im, gray; 
 
void setup(){ 
  im = loadImage("test.png");    // 入力画像の読み込み 
  size(im.width*2, im.height);   // 画面サイズ
  gray = createImage(im.width, im.height, RGB);  // 出力画像用の画像配列(gray)を用意(サイズは入力画像と同じ) 
  im.filter(GRAY);               // グレースケール変換
  float a; 
  // ラプラシアンフィルタ処理
  for(int y=1; y<im.height-1; y++){ 
    for(int x=1; x<im.width-1; x++){
      // 畳み込み計算
      a =  - red(im.get(x,y-1)) - red(im.get(x-1,y)) + 4*red(im.get(x,y)) - red(im.get(x+1,y)) - red(im.get(x,y+1)); 
      gray.set(x, y, color(abs(a)));  // 出力画像の画素値を設定
    } 
  }
  image(im, 0, 0);                 // 入力画像を画面左に貼る 
  image(gray, im.width, 0);        // 出力画像を画面右に貼る    
} 
 
void draw(){ 
} 
