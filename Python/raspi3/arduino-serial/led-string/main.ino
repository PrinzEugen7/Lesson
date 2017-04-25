char data[10];   // 文字列格納用
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
    // 1文字ずつ読み込み
    data[i] = Serial.read();
    // 文字数が10以上 or 終端文字なら終了
    if (i > 10 || data[i] == '\0') i = 0;
    else { i++; }
  }
  return String(data);
}

void loop() {
  String cmd = serialRead();
  if(cmd =="on") digitalWrite(13, HIGH);
  if(cmd =="off") digitalWrite(13, LOW);
}
