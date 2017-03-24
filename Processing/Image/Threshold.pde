PImage im;

void setup() {
  im = loadImage("test.png");
  size(im.width, im.height);
  image(im, 0, 0);
  filter(THRESHOLD,0.8);
}

void draw() {
}
