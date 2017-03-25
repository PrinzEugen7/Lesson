import gab.opencv.*;
import org.opencv.core.Mat;
import org.opencv.core.CvType;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Core.MinMaxLocResult;
import org.opencv.core.Core;

void setup(){
  // 入力画像
  PImage pimg = loadImage("test.jpg", "jpg");
  OpenCV cv = new OpenCV(this, pimg);
  Mat img = OpenCV.imitate(cv.getGray());

  // テンプレート画像
  PImage ptemp = loadImage("temp.jpg", "jpg");
  OpenCV cvtemp = new OpenCV(this, pimg);
  Mat temp = OpenCV.imitate(cvtemp.getGray());

  // 結果格納用
  int h = img.cols() - temp.cols() + 1;
  int w = img.rows() - temp.rows() + 1;
  Mat result = new Mat(w, h, CvType.CV_32FC1);

  // テンプレートマッチングを実行
  Imgproc.matchTemplate(cv.getColor(), cvtemp.getColor(), result, Imgproc.TM_CCOEFF_NORMED);

  // 結果を描画
  image(img, 0, 0);

  MinMaxLocResult mmlr = Core.minMaxLoc(result);

  if (mmlr.maxVal > 0.9) {
    println("Val: " + mmlr.maxVal);
    stroke(255, 0, 0);
    strokeWeight(3);
    noFill();
    rect((int)mmlr.maxLoc.x + 100, (int)mmlr.maxLoc.y, temp.cols(), temp.rows());
  }
}
