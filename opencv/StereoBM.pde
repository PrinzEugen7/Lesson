import gab.opencv.*;
import org.opencv.core.Mat;
import org.opencv.calib3d.StereoBM;
import org.opencv.core.CvType;
import org.opencv.calib3d.StereoSGBM;

OpenCV cvL, cvR;
PImage depth;

void setup() {
  // 画像取得
  cvL = new OpenCV(this, loadImage("scene_l.jpg"));
  cvR = new OpenCV(this, loadImage("scene_r.jpg"));
  // ウィンドウ作成
  size(cvL.width, cvL.height);
  // 画像をグレースケール変換
  cvL.gray();
  cvR.gray();
  Mat grayL = cvL.getGray();
  Mat grayR = cvR.getGray();
  // 視差マップ格納用
  Mat disparity = OpenCV.imitate(grayL);
  // BMでステレオマッチング(視差計算)
  StereoBM stereo =  new StereoBM();
  stereo.compute(grayL, grayR, disparity );
  Mat depthMat = OpenCV.imitate(grayL);
  disparity.convertTo(depthMat, depthMat.type());
   // 得られた奥行きデータを画像化
  depth = createImage(depthMat.width(), depthMat.height(), RGB);
  cvL.toPImage(depthMat, depth);
  image(depth, 0, 0);
}

void draw() {
}
