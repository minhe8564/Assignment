const int inputPin = 2;

long startTime = 0;
long swCountTimer = 0;

void setup() {
  pinMode(inputPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(inputPin) == LOW){
    startTime = millis();
    while(digitalRead(inputPin) == LOW);
    swCountTimer = millis() - startTime;
    Serial.print(swCountTimer);
    Serial.println(" ms");
  };
}
