int cmd = 0;

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
}

void loop() {
  if (Serial.available() > 0) {
      //cmd = Serial.read();
      digitalWrite(LED,HIGH);
  }
  delay(10);
}
