const int potentioMeterPin = 0;
const int ledPin = 13;

void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  int adcValue;
  int duty;

  adcValue = analogRead(potentioMeterPin);
  duty = map(adcValue, 0, 1023, 0, 100);

  digitalWrite(ledPin, LOW);
  delay(100-duty);

  Serial.print("ADC Value is ");
  Serial.print(adcValue);
  Serial.print(", Duty cycle is ");
  Serial.print(duty);
  Serial.println("%");
}
