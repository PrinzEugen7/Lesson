import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;

public class CvTest {
	public static void main(String args[]){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");					// 入力画像の取得
		
	    double gamma = 1;												// ガンマ定数
	    // ルックアップテーブルの計算
	    Mat lut = new Mat(1, 256, CvType.CV_8UC1);	    	//　ルックアップテーブル作成
	    lut.setTo(new Scalar(0));
	    
	    for (int i = 0; i < 256; i++) {
	    	lut.put(0, i, Math.pow((double)(1.0 * i/255), 1/gamma) * 255);	
	    }
	    // ガンマ変換
	    Core.LUT(im, lut, im);
	    // 画像の出力
		Imgcodecs.imwrite("test2.jpg", im);		
	}
}
