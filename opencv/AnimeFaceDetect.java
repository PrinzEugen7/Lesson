import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.highgui.Highgui;
import org.opencv.imgproc.Imgproc;
import org.opencv.core.MatOfRect;
import org.opencv.core.Rect;
import org.opencv.objdetect.CascadeClassifier;

public class AnimeFaceDetect {
    public static void main(String[] args) {
 
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		// 入力画像の取得	
        Mat im = Highgui.imread("test.png"); 
		// カスケード分類器でアニメ顔探索
		CascadeClassifier faceDetector = new CascadeClassifier("lbpcascade_animeface.xml");
		MatOfRect faceDetections = new MatOfRect();
		faceDetector.detectMultiScale(im, faceDetections);
		// 見つかったアニメ顔を矩形で囲む
        for (Rect rect : faceDetections.toArray()) {
            Core.rectangle(im, new Point(rect.x, rect.y), new Point(rect.x + rect.width, rect.y + rect.height), new Scalar(0, 0, 255), 5);
        }
		// 結果を保存
        Highgui.imwrite("anime.png", im);
    }
}
