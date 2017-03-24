import processing.video.*;

Capture cam;

void setup()
{
    /* 画面サイズ */
    size(640, 480);
    /* 接続されている全てのカメラの名前を取得 */
    String[] cams = Capture.list();
    /* カメラのキャプチャー */
    cam = new Capture(this, cams[0]);
    cam.start();
}

void draw()
{
     /* カメラの画像を取得 */
     if (cam.available()) 
     {
         cam.read();
     }
     /* 画像を表示 */
     set(0, 0, cam); 
}
