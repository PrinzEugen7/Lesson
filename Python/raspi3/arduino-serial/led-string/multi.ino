String cmds[3] = {"\0"}; // 分割された文字列を格納する配列 
char data[20];   // 文字列格納用
int i = 0;  // 文字数のカウンタ
int index;
#define PIN1 11
#define PIN2 12
#define PIN3 13

// 文字列分割
int split(String data, char delimiter, String *dst){
    int index = 0;
    int arraySize = (sizeof(data)/sizeof((data)[0]));  
    int datalength = data.length();
    for (int i = 0; i < datalength; i++) {
        char tmp = data.charAt(i);
        if ( tmp == delimiter ) {
            index++;
            if ( index > (arraySize - 1)) return -1;
        }
        else dst[index] += tmp;
    }
    return (index + 1);
}

// データ受信
String serialRead(){
  // データ受信したとき
  if (Serial.available()) {
    // 1文字ずつ読み込み
    data[i] = Serial.read();
    // 文字数が10以上 or 終端文字なら終了
    if (i > 20 || data[i] == '\0'){
      // 配列リセット
      for(int j=0;j<index;j++) cmds[j] = "";
      // カンマ区切りで分割
      index = split(data, ',', cmds);
      i = 0;
    }
    else { i++; }

  }
  return String(data);
}

void setup() {
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  String cmd = serialRead();
  // 受信したデータに応じてLEDを点灯・消灯
  if(cmds[0] == "on") digitalWrite(PIN1, HIGH);
  if(cmds[0] == "off") digitalWrite(PIN1, LOW);
  if(cmds[1] == "on") digitalWrite(PIN2, HIGH);
  if(cmds[1] == "off") digitalWrite(PIN2, LOW);
  if(cmds[2] == "on") digitalWrite(PIN3, HIGH);
  if(cmds[2] == "off") digitalWrite(PIN3, LOW);
}
