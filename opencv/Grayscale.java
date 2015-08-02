import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

public class Grayscale{
    public static void main(String[] args){
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        Mat im = Imgcodecs.imread("test.png");	// 入力画像の取得
        Imgproc.cvtColor(im, im, Imgproc.COLOR_RGB2GRAY);       // 画像のグレースケール変換
        Imgcodecs.imwrite("test.jpg",im);			// 画像データをJPG形式で保存
    }
}
