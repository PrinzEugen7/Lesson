import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.photo.Photo;
public class CvTest {
	public static void main(String args[]){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");					// 入力画像の取得
		Photo.fastNlMeansDenoising(im, im);
		Imgcodecs.imwrite("test2.jpg", im);			    // 画像の出力
	}
}
