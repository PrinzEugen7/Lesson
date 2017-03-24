PImage im, gray; 
 
void setup(){ 
  im = loadImage("test.png");    // 入力画像の読み込み 
  size(im.width*2, im.height);   // 画面サイズ
  gray = createImage(im.width, im.height, RGB);  // 出力画像用の画像配列(gray)を用意(サイズは入力画像と同じ) 
  im.filter(GRAY);               // グレースケール変換
  float a[] = new float[9];      // 周囲9画素分の画素値を格納するための配列を用意   
  // メディアンフィルタ処理
  for(int y = 1; y < im.height-1; y++){ 
    for(int x = 1; x < im.width-1; x++){ 
      a[0] = red(im.get(x-1,y-1));
      a[1] = red(im.get(x  ,y-1));
      a[2] = red(im.get(x+1,y-1)); 
      a[3] = red(im.get(x-1,y  ));
      a[4] = red(im.get(x  ,y  ));
      a[5] = red(im.get(x+1,y  )); 
      a[6] = red(im.get(x-1,y+1));
      a[7] = red(im.get(x  ,y+1));
      a[8] = red(im.get(x+1,y+1)); 
      // 配列a内のデータを昇順ソート
      a = sort(a);
      gray.set(x, y, color(a[4])); // 中央値を画素値に設定  
    } 
  }
  image(im, 0, 0);                 // 入力画像を画面左に貼る 
  image(gray, im.width, 0);        // 出力画像を画面右に貼る    
} 
 
void draw(){ 
} 
