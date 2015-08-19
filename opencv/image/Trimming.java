import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Rect;
import org.opencv.imgcodecs.Imgcodecs;

public class CvTest {
	public static void main(String args[]){
 
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		// 入力画像の取得	
        Mat im = Imgcodecs.imread("test.jpg"); 
        Rect roi = new Rect(280, 60, 120, 100);
        Mat im2 = new Mat(im, roi);
		// 結果を保存
        Imgcodecs.imwrite("anime.png", im2);
    }
}
