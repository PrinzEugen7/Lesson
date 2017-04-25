int cmd = 0;

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
}

void loop() {
  if (Serial.available() > 0) {
    cmd = Serial.read();
    // 入力値がoなら点灯, それ以外は消灯
    if(cmd=='o') digitalWrite(13, HIGH);
    else digitalWrite(13, LOW);
  }
  delay(10);
}
