const byte number[10] ={
  B00111111, //0
  B00000110, //1
  B01011011, //2
  B01001111, //3
  B01100110, //4
  B01101101, //5
  B01111101, //6
  B00000111, //7
  B01111111, //8
  B01101111, //9
};

void setup() {
  for(int i = 2; i <=0; i++){
    pinMode(i, OUTPUT);
  };
  digitalWrite(9, LOW);
}

void loop() {
  for(int k = 0; k <= 9; k++){
    fndDisplay(k);
    delay(1000);
  };
}

//LED 점등
void fndDisplay(int displayValue){
  boolean bitValue;

  for(int i = 2; i <=9; i++){
    digitalWrite(i, LOW);
  };
  for(int i = 0; i <=7; i++){
    bitValue = bitRead(number[displayValue], i);
    digitalWrite(i+2, bitValue);
  };
}
