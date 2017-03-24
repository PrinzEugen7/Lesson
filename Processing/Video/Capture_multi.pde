import processing.video.*;
 
Capture cam1;
Capture cam2;
 
void setup()
{
    /* 画面サイズ */
    size(640*2, 480);
    /* 接続されている全てのカメラの名前を取得 */
    String[] cams = Capture.list();
    /* カメラのキャプチャー */
    cam1 = new Capture(this, cams[0]);
    cam2 = new Capture(this, cams[1]);
    cam1.start();
    cam2.start();
}
 
void draw()
{
     /* カメラの画像を取得 */
     if (cam1.available()&amp;&amp;cam2.available())
     {
         cam1.read();
         cam2.read();
     }
	/* 画像を表示 */
	set(0, 0, cam1);
	set(0, 640, cam2);
}
