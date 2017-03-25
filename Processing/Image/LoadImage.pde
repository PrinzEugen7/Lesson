PImage img;

void setup() {
  img = loadImage("test.jpg");
  surface.setResizable(true);
  surface.setSize(img.width, img.height);   // 画面サイズ
}

void draw() {
  image(img, 0, 0);
}

