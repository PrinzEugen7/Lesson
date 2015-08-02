import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Size;

public class DrawEllipse{
	public static void main(String[] args){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");	// 入力画像の取得
		// 直線描画
		Imgproc.ellipse(im, new Point(100,100), new Size(100,50), 0, 0, 360, new Scalar(250, 0, 0, 55), 5);
		Imgcodecs.imwrite("test2.jpg", im);			// 出力画像の保存
	}
}
