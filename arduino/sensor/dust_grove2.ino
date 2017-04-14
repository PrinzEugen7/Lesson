int pin = 8;
unsigned long t0;
unsigned long ts = 30000; // 30000ms
unsigned long lowOc = 0;
double ratio = 0;
double concent = 0;

void setup() {
  Serial.begin(9600);
  pinMode(8,INPUT);
  t0 = millis();
}

// 単位をμg/m^3に変換
double pcs2ugm3 (double pcs)
{
  double pi = 3.14159;
  // 全粒子密度(1.65E12μg/ m3)
  double density = 1.65 * pow (10, 12);
  // PM2.5粒子の半径(0.44μm)
  double r25 = 0.44 * pow (10, -6);
  double vol25 = (4/3) * pi * pow (r25, 3);
  double mass25 = density * vol25; // μg
  double K = 3531.5; // per m^3 
  // μg/m^3に変換して返す
  return pcs * K * mass25;
}

void loop() {
  // LOWの占有率
  lowOc += pulseIn(pin, LOW);

  // サンプリング
  if ((millis() - t0) > ts){
    // LOWの割合
    ratio = lowOc/(ts*10.0);
    // ほこりの濃度を算出
    concent = 1.1 * pow(ratio,3) - 3.8 * pow(ratio,2) + 520 * ratio + 0.62;
    Serial.println(String( pcs2ugm3(concent) ) + "[ug/ m3]");
    lowOc = 0;
    t0 = millis();
  }
}

