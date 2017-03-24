import gab.opencv.*;
import org.opencv.core.Mat;
import org.opencv.core.CvType;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Core.MinMaxLocResult;
import org.opencv.core.Core;
PImage im, temp;

void setup(){ 
  im = loadImage("test.jpg");      // 入力画像の読み込み
  temp = loadImage("temp.jpg");    // テンプレート画像の読み込み
  OpenCV cvIm = new OpenCV(this,im);
  OpenCV cvTemp = new OpenCV(this, temp);
  // マッチング結果格納用
  Mat matIm = new Mat(im.height, im.width, CvType.CV_32FC1);
  // テンプレートマッチング処理
  Imgproc.matchTemplate(cvIm.getColor(), cvTemp.getColor(), matIm, Imgproc.TM_CCOEFF_NORMED);
  MinMaxLocResult pt = Core.minMaxLoc(matIm);  // マッチングした領域の座標を抽出
  // 結果を描画
  size(im.width, im.height);
  image(im, 0, 0);
  stroke(200, 0, 0);
  strokeWeight(3);
  noFill();
  rect((int)pt.maxLoc.x, (int)pt.maxLoc.y, temp.width, temp.height); 
} 
 
void draw(){ 
} 
