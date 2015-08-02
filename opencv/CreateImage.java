import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Scalar;
import org.opencv.highgui.Highgui;

public class CreateImage{
	public static void main(String[] args){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Highgui.imread("test.png");	// 入力画像の取得
		Highgui.imwrite("test.jpg",im);				// 画像をJPG形式で保存
	}
}
