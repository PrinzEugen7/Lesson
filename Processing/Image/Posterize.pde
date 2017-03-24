PImage im;

void setup() {
  im = loadImage("test.png");
  size(im.width, im.height);
  image(im, 0, 0);
  filter(POSTERIZE, 4);
}

void draw() {
}
