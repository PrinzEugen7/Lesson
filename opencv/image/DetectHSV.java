import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

public class CvTest {
	public static void main(String args[]){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");											// 入力画像の取得
		Mat hsv = new Mat();
		Mat mask = new Mat();
		Mat im2 = new Mat();
		Imgproc.cvtColor(im, hsv, Imgproc.COLOR_BGR2HSV);						// HSV色空間に変換
		Core.inRange(hsv, new Scalar(40,10,0), new Scalar(70,255,255), mask);	// 緑色領域のマスク作成
		im.copyTo(im2, mask);																	// マスクを 用いて入力画像から緑色領域を抽出
		Imgcodecs.imwrite("test2.jpg", im2);												// 画像の出力
	}
}
