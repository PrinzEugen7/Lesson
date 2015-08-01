import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Size;

public class HoughLines{
	public static void main(String[] args){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");								// 入力画像の取得
		Mat gray = new Mat(im.rows(), im.cols(), CvType.CV_8SC1);	
		Imgproc.cvtColor(im, gray, Imgproc.COLOR_RGB2GRAY); 		// グレースケール変換
		Imgproc.Canny(gray, gray, 70, 110);										// 輪郭線検出
		Mat lines = new Mat();
		// 古典的ハフ変換で直線検出
		Imgproc.HoughLines(gray, lines, 1, 2*Math.PI/180, 20);
		// 検出した直線上を赤線で塗る
		for (int i = 0; i &lt; lines.cols(); i++){
			double data[] = lines.get(0, i);
			double rho = data[0];
			double theta = data[1];
			double cosTheta = Math.cos(theta);
			double sinTheta = Math.sin(theta);
			double x0 = cosTheta * rho;
			double y0 = sinTheta * rho;
			Point pt1 = new Point(x0 + 10000 * (-sinTheta), y0 + 10000 * cosTheta);
			Point pt2 = new Point(x0 - 10000 * (-sinTheta), y0 - 10000 * cosTheta);
			Imgproc.line(im, pt1, pt2, new Scalar(0, 0, 200), 3);
		}
		Imgcodecs.imwrite("test2.jpg", im);								// 出力画像の保存
	}
}
