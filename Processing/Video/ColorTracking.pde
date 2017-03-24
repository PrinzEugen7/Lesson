import processing.video.*;
Capture cap;
color target = color(255,0,0);				// 追跡する色

void setup(){
  size(640, 480);  							// 画面サイズ
  smooth();    									// 描画を滑らかに
  String[] cams = Capture.list(); 			// 接続されている全カメラ名を取得
  cap = new Capture(this, cams[0]); 	// カメラのキャプチャ
  cap.start();
}

void draw() {
  if (cap.available()){
	// 変数の宣言
    int x = width/2;    	// 追跡対象のx座標
    int y = height/2;  	// 追跡対象のy座標
    int dmax = 21;         // 追跡対象判定の閾値
    int xmin = width; 		// 追跡する画素のx座標最小値
    int ymin = height;  	// 追跡する画素のx座標最大値
    int xmax = 0; 			// 追跡する画素のy座標最小値
    int ymax = 0; 			// 追跡する画素のy座標最大値
    cap.read();            	// カメラ映像の取得
    image(cap, 0, 0);       // カメラ映像の表示
	// 色検出
    for(int i = 0; i < width*height; i++){
      // 目標の色との差を計算
      float dr = abs( red(target) - red(cap.pixels[i]) );
      float dg = abs( green(target) - green(cap.pixels[i]) );
      float db = abs( blue(target) - blue(cap.pixels[i]) );

      // 差がdmax以下なら目標物として認識
      if(dr < dmax && dg < dmax && db < dmax){
        xmin = min(i%width,xmin);  		// 追跡する画素のx座標最小値
        xmax = max(i%width,xmax);  	// 追跡する画素のx座標最大値
        ymin = min(i/width,ymin);  		// 追跡する画素のy座標最小値
        ymax = max(i/width,ymax);  	// 追跡する画素のy座標最大値
      }
    }
    x = (xmin+xmax)/2;  	// 追跡対象のx座標を計算
    y = (ymin+ymax)/2;  	// 追跡対象のy座標を計算    
    stroke(255,0,0);  		// 線色
    strokeWeight(5); 		// 線の太さ
    noFill(); 					// 塗りつぶしなし
    rect(x-25, y-25, 50, 50);  // 追跡対象の中心に矩形を描画
    line( x, 0, x, height); 
    line( 0, y, width, y);
  }
}

// マウスクリックした画素の色を追跡対象にする
void mousePressed(){
  target = cap.pixels[mouseX+mouseY*width];
}
