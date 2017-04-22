int trig = 8; // 出力ピン
int echo = 9; // 入力ピン

void setup() {
  Serial.begin(9600);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
}

void loop() {
  // 超音波の出力終了
  digitalWrite(trig,LOW);
  delayMicroseconds(1);
  // 超音波を出力
  digitalWrite(trig,HIGH);
  delayMicroseconds(11);
  // 超音波を出力終了
  digitalWrite(trig,LOW);
  // 出力した超音波が返って来る時間を計測
  int t = pulseIn(echo,HIGH);
  // 計測した時間と音速(気温を考慮)から反射物までの距離を計算
  float temp = 22.4;    // 気温
  float v = (331.5+0.6*temp)/10000; // 音速
  float distance = v*(t/2); // 距離
  // 計算結果をシリアル通信で出力
  Serial.print(distance);
  Serial.println(" cm");
  delay(500);
}
