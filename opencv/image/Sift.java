import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.MatOfKeyPoint;
import org.opencv.features2d.DescriptorExtractor;
import org.opencv.features2d.FeatureDetector;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

public class CvTest {
	public static void main(String args[]){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat im = Imgcodecs.imread("test.jpg");					// 入力画像の取得
		Mat gray = new Mat();
		Imgproc.cvtColor(im, gray, Imgproc.COLOR_RGB2GRAY); // 画像のグレースケール変換  

	    // ------ SIFTの処理 ここから ------
	    FeatureDetector siftDetector = FeatureDetector.create(FeatureDetector.SIFT);
	    DescriptorExtractor siftExtractor = DescriptorExtractor.create(DescriptorExtractor.SIFT);
	    
	    MatOfKeyPoint kp = new MatOfKeyPoint();
	    siftDetector.detect(gray, kp);

	    Mat des = new Mat(im.rows(), im.cols(), im.type());
	    siftExtractor.compute(gray, kp, des);
	    

		Imgcodecs.imwrite("test2.jpg", gray);					// 画像の出力
	}
}
