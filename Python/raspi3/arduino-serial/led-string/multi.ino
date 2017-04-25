char data[20];   // 文字列格納用
int i = 0;  // 文字数のカウンタ
String cmd1, cmd2, cmd3;
#define PIN1 11
#define PIN2 12
#define PIN3 13

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
    // 文字数が20以上 or 終端文字なら終了
    if (i > 20 || data[i] == '\0'){   
      cmd1 = strtok(data, ",");
      cmd2 = strtok(NULL, ",");
      cmd3 = strtok(NULL, ",");
      i = 0;
    }
    else i++;
  }
  return String(data);
}

void loop() {
  String cmd = serialRead();
  if(cmd1 == "on") digitalWrite(PIN1, HIGH);
  if(cmd1 == "off") digitalWrite(PIN1, LOW);
  if(cmd2 == "on") digitalWrite(PIN2, HIGH);
  if(cmd2 == "off") digitalWrite(PIN2, LOW);
  if(cmd3 == "on") digitalWrite(PIN3, HIGH);
  if(cmd3 == "off") digitalWrite(PIN3, LOW);
}
