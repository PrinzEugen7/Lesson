import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Size;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

public class CvTest {
	public static void main(String args[]){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");					// 入力画像の取得
		Imgproc.resize(im, im, new Size(),0.1, 0.1,Imgproc.INTER_NEAREST);	// 画像サイズを1/10倍
		Imgproc.resize(im, im, new Size(),10.0, 10.0,Imgproc.INTER_NEAREST);	// 画像サイズを10倍
		Imgcodecs.imwrite("test2.jpg", im);					// 画像の出力
	}
}
