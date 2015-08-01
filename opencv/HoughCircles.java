import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Size;

public class HoughCircles{
	public static void main(String[] args){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");								// 入力画像の取得
		Mat gray = new Mat(im.rows(), im.cols(), CvType.CV_8SC1);	
		Imgproc.cvtColor(im, gray, Imgproc.COLOR_RGB2GRAY); 		// グレースケール変換
		//Imgproc.Canny(gray, gray, 80, 100);										// 輪郭線検出
		Mat circles = new Mat();
		// ハフ変換で円検出
		Imgproc.HoughCircles(gray, circles, Imgproc.CV_HOUGH_GRADIENT, 2, 10, 160, 50, 10, 20); 
		Point pt = new Point();
		// 検出した直線上を赤線で塗る
		for (int i = 0; i &lt; circles.cols(); i++){
			double data[] = circles.get(0, i);
			pt.x = data[0];
			pt.y = data[1];
			double rho = data[2];
			Imgproc.circle(im, pt, (int)rho, new Scalar(0, 200, 0), 5);
		}
		Imgcodecs.imwrite("test2.jpg", im);								// 出力画像の保存
	}
}
