PImage img;

void setup() {
  img = loadImage("test.jpg");
  surface.setResizable(true);
  surface.setSize(img.width*2, img.height);   // 画面サイズ
}

void draw() {
  image(img, img.width, 0);
  filter(THRESHOLD,0.8);
  image(img, 0, 0);
}
