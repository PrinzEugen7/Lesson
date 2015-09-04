import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class CvTest {
	public static void main(String args[]) 
	{
        JFrame frame = new JFrame("画像表示");						// ウィンドウのタイトル名
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setSize(500, 400);									// ウィンドウのサイズ
        ImageIcon icon = new ImageIcon("test.jpg");        			// 画像を取得してアイコンにする
        JLabel label = new JLabel(icon);							// アイコンを表示するラベルを作成
        frame.getContentPane().add(label);							// ウィンドウのContentPaneにラベルを追加
        frame.setVisible(true)										// ウィンドウを表示
	}
	  
}
