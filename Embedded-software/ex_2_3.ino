// LED 출력을 할 핀 번호 설정
const int ledPin = 13;
// 점멸횟수 변수 설정
int blinkNumber = 0;

void setup() {
  // put your setup code here, to run once:
  // 9600bps로 시리얼 통신 설정
  Serial.begin(9600);
  // 13번 핀을 출력으로 설정
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // 시리얼 통신으로 입력 받은 데이터가 있는지를 검사하여
  // 데이터가 있을 경우에 if문 안의 명령어를 실행
  if(Serial.available()){
    char val = Serial.read();
    if(isDigit(val)){
      blinkNumber = (val - '0');
    }
  }

  for(char i=0; i < blinkNumber; i++){
    digitalWrite(ledPin, HIGH);
    delay(200);
    digitalWrite(ledPin, LOW);
    delay(200);
  }
  blinkNumber = 0;
}
