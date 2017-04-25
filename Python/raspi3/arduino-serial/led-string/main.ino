char input[30];   // 文字列格納用
int i = 0;  // 文字数のカウンタ
         
void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}
         
void loop() {
  
  // データ受信したとき
  if (Serial.available()) {
    input[i] = Serial.read();
     // 文字数が30以上 or 末尾文字
    if (i > 30 || input[i] == '.') {
      // 末尾に終端文字の挿入
      input[i] = '\0';
      // 受信文字列を送信
      if (String(input)=="on"){
        digitalWrite(13, HIGH);
      }
      else if (String(input)=="off"){
        digitalWrite(13,LOW);
      }
      // カウンタの初期化
      i = 0;
    }
    else { i++; }
  }
}
