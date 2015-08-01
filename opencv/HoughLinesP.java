import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Size;

public class HoughLinesP{
	public static void main(String[] args){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");								// 入力画像の取得
		Mat gray = new Mat(im.rows(), im.cols(), CvType.CV_8SC1);	
		Imgproc.cvtColor(im, gray, Imgproc.COLOR_RGB2GRAY); 		// グレースケール変換
		Imgproc.Canny(gray, gray, 80, 100);										// 輪郭線検出
		Mat lines = new Mat();
		// 確率的ハフ変換で直線検出
		Imgproc.HoughLinesP(gray, lines, 1, Math.PI/180, 50, 100 ,50);
		double[] data;
		Point pt1 = new Point();
		Point pt2 = new Point();
		// 検出した直線上を赤線で塗る
		for (int i = 0; i &lt; lines.cols(); i++){
			data = lines.get(0, i);
			pt1.x = data[0];
			pt1.y = data[1];
			pt2.x = data[2];
			pt2.y = data[3];
			Imgproc.line(im, pt1, pt2, new Scalar(0, 0, 200), 3);
		}
		Imgcodecs.imwrite("test2.jpg", im);								// 出力画像の保存
	}
}
