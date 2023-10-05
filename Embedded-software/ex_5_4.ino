const int numRows = 4;
const int numCols = 4;

char keys[numRows][numCols] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

int rowPins[] = {2, 3, 4, 5};
int colPins[] = {6, 7, 8, 9};

void setup() {
  // 열을 입력 풀업 모드로 설정
  for(int i = 0; i < numRows; i++){
    pinMode(rowPins[i], INPUT_PULLUP);
  }

  // 행을 출력 모드로 설정, 초기값 HIGH
  for(int i = 0; i < numCols; i++){
    pinMode(colPins[i], OUTPUT);
    digitalWrite(colPins[i], HIGH);
  }
  Serial.begin(9600);
}

void loop() {
  // key 변수에 키패드 입력 값을 읽어서 저장
  char key = keypadRead();

  if(key != 0){
    Serial.print("You push ");
    Serial.print(key);
    Serial.print(" Key");
  };
}

char keypadRead(){

  char key = 0;

  for(int i = 0; i < numCols; i++){
    // 행 중에 하나를 LOW로 설정
    digitalWrite(colPins[i], LOW);
    
    // 열을 하나씩 바꿔가면서 값 읽기
    for(int j = 0; j < numRows; j++){
      // 열 입력이 LOW 일 때 키 입력 발생
      if(digitalRead(rowPins[i]) == LOW){
        delay(10);
        // 키 놓을 때까지 기다림
        while(digitalRead(rowPins[j]) == LOW);
        key = keys[j][i];
      };
    }
    // 행을 다시 HIGH로 설정
    digitalWrite(colPins[i], HIGH);
  }
  return key;
}
