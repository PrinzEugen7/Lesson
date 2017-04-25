char data[30];   // 文字列格納用
int i = 0;  // 文字数のカウンタ

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

// データ受信
String serialRead(){
  // データ受信したとき
  if (Serial.available()) {
    data[i] = Serial.read();
     // 文字数が30以上 or 終端文字
    if (i > 30 || data[i] == '\0') {
      i = 0;      // カウンタの初期化
      break;
    }
    else { i++; }
  }
  return String(data);
}

void loop() {
  String cmd = serialRead();
  if(cmd =="on") digitalWrite(13, HIGH);
  if(cmd =="off") digitalWrite(13, LOW);
}
