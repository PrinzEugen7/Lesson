import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.Size;

public class Sobel{
	public static void main(String[] args){
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		Mat gray = Imgcodecs.imread("test.jpg", 0);
		Imgproc.Sobel(gray, gray, gray.depth(), 2, 2);
		Imgcodecs.imwrite("test2.jpg", gray);
	}
}
