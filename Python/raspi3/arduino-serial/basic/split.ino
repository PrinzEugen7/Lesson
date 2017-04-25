String cmds[3] = {"\0"}; // 分割された文字列を格納する配列 

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
 
void setup() {
  // 文字列
  String cmd = "on,off,on";
  // 分割数 = 分割処理(文字列, 区切り文字, 配列) 
  int index = split(cmd, ',', cmds);
  // 結果表示
  Serial.begin(9600);
  for(int i = 0; i < index; i++){
    Serial.println(cmds[i]);
  }
}
 
void loop() {

}
