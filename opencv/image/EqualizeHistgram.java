import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;


public class CvTest {
	public static void main(String args[]){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");			// 入力画像の取得
		Mat gray = new Mat();
		Imgproc.cvtColor(im, gray, Imgproc.COLOR_RGB2GRAY)	// 画像のグレースケール変換
    		Imgproc.equalizeHist(gray, gray)			// グレースケール画像のヒストグラムを平坦化
		Imgcodecs.imwrite("test2.jpg", gray);			// 画像の出力
	}
}
