package info.cvtest;
import java.io.File;
import java.io.IOException;
import com.drew.imaging.ImageMetadataReader;
import com.drew.imaging.ImageProcessingException;
import com.drew.metadata.Directory;
import com.drew.metadata.Metadata;
import com.drew.metadata.Tag;

public class CvTest {
	public static void main(String args[]) throws ImageProcessingException, IOException 
	{
	      File jpegFile = new File("test.jpg");								// JPEG画像の読み込み
	      Metadata metadata = ImageMetadataReader.readMetadata(jpegFile);	// 画像からExif情報を抽出
	      // Exif情報を全て表示
	      for (Directory directory : metadata.getDirectories()) {
	          for (Tag tag : directory.getTags()) {
	              System.out.println(tag);
	          }
	      }
	}
}
