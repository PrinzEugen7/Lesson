import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Size;

public GaussianBlur Test{
	public static void main(String[] args){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");	// 入力画像の取得
		Mat dst = new Mat();
		Imgproc.GaussianBlur(im, dst, new Size(5, 5) ,1 ,1);
		Imgcodecs.imwrite("test2.jpg", dst);			// 出力画像の保存
	}
}
