import gab.opencv.*;
import processing.video.*;

Movie video;
OpenCV cv;

void setup() {
  // 画面サイズ
  size(720, 480);
  // 動画の読み込み
  video = new Movie(this, "street.mov");
  cv = new OpenCV(this, 720, 480);
  // 背景差分の初期設定
  cv.startBackgroundSubtraction(5, 3, 0.5);
  video.loop();
  // 動画の再生開始
  video.play();
}

void draw() {
  image(video, 0, 0);  
  cv.loadImage(video);
  // 背景データの更新
  cv.updateBackground();
  cv.dilate();
  cv.erode();

  noFill();
  stroke(255, 0, 0);
  strokeWeight(3);
  // 移動物体の輪郭を赤く塗る
  for (Contour contour : cv.findContours()) {
    contour.draw();
  }
}

// 動画イベント
void movieEvent(Movie m) {
  m.read();
}
