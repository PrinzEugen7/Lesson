import gab.opencv.*;
import processing.video.*;
import java.awt.*;

Capture video;
OpenCV opencv;

void setup() {
  // 画面サイズ
  size(640, 480);
  // カメラのキャプチャ
  video = new Capture(this, 640/2, 480/2);
  opencv = new OpenCV(this, 640/2, 480/2);
  // 顔の分類器をロード
  opencv.loadCascade("haarcascade_frontalface_alt.xml");  
  // ビデオ再生開始
  video.start();
}

void draw() {
  scale(2);
  // フレーム取得
  opencv.loadImage(video);
  image(video, 0, 0 );
  // 顔検出
  Rectangle[] faces = opencv.detect();
  noFill();
  stroke(255,0,0);
  strokeWeight(5);
  // 検出した顔を矩形で囲む
  for (int i = 0; i &lt; faces.length; i++) {
    rect(faces[i].x, faces[i].y, faces[i].width, faces[i].height);
  }
}

// キャプチャイベント
void captureEvent(Capture c) {
  c.read();
}
