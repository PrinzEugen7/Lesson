PImage img, img2;

// 量子化の閾値
int level0 = 190; 
int level1 = 180;
int level2 = 170;
int level3 = 160; 
int level4 = 140;
int level5 = 120;
int level6 = 100; 
int level7 = 90;
int level8 = 80;
int level9 = 70; 
int level10 = 60;
int level11 = 50;
int level12 = 40;
int level13 = 20;
int level14 = 0;

void setup(){
  img = loadImage("test.jpg");
  size(img.width, img.height);
  img2 = new PImage(img.width, img.height);
  float level;
  // 16段階で量子化
  for(int i = 0; i < img2.width*img2.height; i++){
    color pix = img.pixels[i];
    float pixcel = (int)(0.299*red(pix) + 0.587*green(pix) + 0.114*blue(pix));
    if(pixcel > level0) level = 190;
    else if(pixcel > level1) level = 180;
    else if(pixcel > level2) level = 170;
    else if(pixcel > level3) level = 160; 
    else if(pixcel > level4) level = 140;
    else if(pixcel > level5) level = 120;
    else if(pixcel > level6) level = 100; 
    else if(pixcel > level7) level = 90;
    else if(pixcel > level8) level = 80;
    else if(pixcel > level9) level = 70; 
    else if(pixcel > level10) level = 60;
    else if(pixcel > level11) level = 50;
    else if(pixcel > level12) level = 40;
    else if(pixcel > level13) level = 20;
    else level = 0;
    img2.pixels[i] = color(level);
  }
  image(img2,0, 0); // 表示
  save("ryoshika.jpg");
}

void draw(){
}
