import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.highgui.Highgui;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Size;

public class DrawText {
    public static void main(String[] args) {
 
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		// 入力画像の取得	
        Mat im = Highgui.imread("test.png"); 
		// 文字の描画
		Core.putText(im, "Earth", new Point(60, 60), Core.FONT_HERSHEY_SIMPLEX, 1.6f, new Scalar(20, 0, 200), 3);
		// 結果を保存
        Highgui.imwrite("ouput.png", im);
    }
}
