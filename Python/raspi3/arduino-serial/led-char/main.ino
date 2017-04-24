

void setup(){
  pinMode(13, OUTPUT);
  // シリアルポートを9600 bps[ビット/秒]で初期化
  Serial.begin(9600);
}

void loop(){
  
  int inputchar;
  // シリアルポートより1文字読み込む
  inputchar = Serial.read();
 
  if(inputchar != -1 ){
    // 読み込んだデータが -1 以外の場合　以下の処理を行う 
    switch(inputchar){
      case 's':
        // 読み込みデータが　o の場合
        digitalWrite(13, HIGH);
        break;
      case 'q': 
        // 読み込みデータが　p の場合
        digitalWrite(13, LOW);
        break;
    }
  }
  else {
    // 読み込むデータが無い場合は何もしない
  }
}

