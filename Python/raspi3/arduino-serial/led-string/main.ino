#include <String.h>

String inputStr = String(20);

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  inputStr = "";
}

void serialRead() {
  while (Serial.available() > 0) {
    char inputChar = Serial.read();
    if (inputChar == '\n') break;
    if (inputStr.length() > 20) break;
    inputStr.concat(String(inputChar));
  }
}
void loop() {
  serialRead();
  if (inputStr.startsWith("on")) digitalWrite(13, HIGH);
  else if (inputStr.startsWith("off")) digitalWrite(13, LOW);
  inputStr = "";
}
