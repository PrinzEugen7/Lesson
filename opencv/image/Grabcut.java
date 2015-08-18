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
	Mat im = Imgcodecs.imread("test.jpg");					// 入力画像の取得
        Mat mask = new Mat();							// マスク画像用
        Mat bgModel = new Mat();						// 背景モデル用
        Mat fgModel = new Mat();						// 前景モデル用
        Rect rect = new Rect(10, 10,250,290);					// 大まかな前景と背景の境目(矩形)
        Mat source = new Mat(1, 1, CvType.CV_8U, new Scalar(3));		
        Imgproc.grabCut(im, mask, rect, bgModel, fgModel, 1, 0);		// グラフカットで前景と背景を分離
        Core.compare(mask, source, mask, Core.CMP_EQ);
        Mat fg = new Mat(im.size(), CvType.CV_8UC1, new Scalar(0, 0, 0));	// 前景画像用
        im.copyTo(fg, mask);							// 前景画像の作成
	Imgcodecs.imwrite("test2.jpg", fg);					// 画像の出力
	}
}
