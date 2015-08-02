import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Size;

public class Canny{
	public static void main(String[] args){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat gray = Imgcodecs.imread("test.jpg", 0);	// 入力画像の取得
		Imgproc.Canny(gray, gray, 100, 200, 3, true); 
		Imgcodecs.imwrite("test2.jpg", gray);			// 画像データをJPG形式で保存
	}
}
