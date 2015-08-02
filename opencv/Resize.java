import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Size;

public class Resize{
	public static void main(String[] args){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");	// 入力画像の取得
		Mat im2 = new Mat();
		Mat im3 = new Mat();
		Size sz = im.size();
		Imgproc.resize(im, im2, new Size(sz.width*2, sz.height*2));				// 2倍拡大
		Imgproc.resize(im, im3, new Size(sz.width*0.5, sz.height*0.5));			// 1/2倍に縮小
		Imgcodecs.imwrite("test2.jpg", im2);			// 出力画像の保存
		Imgcodecs.imwrite("test3.jpg", im3);			// 出力画像の保存
	}
}
