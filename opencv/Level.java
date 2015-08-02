import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Size;

public class Level{
    public static void main(String[] args){
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        Mat im = Imgcodecs.imread("test.jpg");	// 入力画像の取得
		int n = 100;                     					// 大きいほど階調数が減少
		// 減色処理
		Size sz = im.size();
		for (int i = 0; i &lt; sz.height; i++){
			for (int j = 0; j &lt; sz.width; j++) {
			double[] pixcel = im.get(i, j);
			pixcel[0] = ( (int)pixcel[0] / n)*n + n/2;
			pixcel[1] = ( (int)pixcel[1] / n)*n + n/2;
			pixcel[2] = ( (int)pixcel[2] / n)*n + n/2;
			im.put(i, j, pixcel);
			}
		}
        Imgcodecs.imwrite("test2.jpg",im);			// 画像データをJPG形式で保存
    }
}
