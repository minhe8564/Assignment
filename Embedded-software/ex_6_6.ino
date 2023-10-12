// 소리 입력
// ex_6_6

char soundInputPin = 0;

char ledLevel[3] = {2, 3, 4};

void setup() {
   for(int i=0; i<=2 ; i++){
    pinMode(ledLevel[i],OUTPUT);
   }
}

void loop(){
  int soundInput = analogRead(soundInputPin);
  int soundLevel = map(soundInput,50,900,0,2);

  for(int i =0;i<=2;i++){
    digitalWrite(ledLevel[i],LOW);
  }
  for(int i =0; i<= soundLevel; i++){
    digitalWrite(ledLevel[i],HIGH);
  }
}            
