const int ledA = 3;
const int ledB = 5;
int brightness = 0;
int increment = 1;

void setup() {
  // analogWrite 핀에는 별도의 설정이 불필요하다.

}

void loop() {
  analogWrite(ledA, brightness);
  analogWrite(ledB, 255-brightness);

  brightness = brightness + increment;
  if((brightness >= 255) || (brightness <= 0)) increment = -increment;
  delay(10);

}
