package info.cvtest;
import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

public class CvTest {
	public static void main(String args[]){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");					// 入力画像の取得			// 入力画像の取得
        Mat result = new Mat();
        Mat bgModel = new Mat();
        Mat fgModel = new Mat();
        Rect rect = new Rect(10, 10,250,290);
        Mat source = new Mat(1, 1, CvType.CV_8U, new Scalar(3));
        Imgproc.grabCut(im, result, rect, bgModel, fgModel, 1, 0);
        Core.compare(result, source,result, Core.CMP_EQ);
        Mat fg = new Mat(im.size(), CvType.CV_8UC1, new Scalar(0, 0, 0));
        im.copyTo(fg, result);
		Imgcodecs.imwrite("test2.jpg", fg);					// 画像の出力
	}
}
