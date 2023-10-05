const int ledPin = 13;
const int inputPin = 2;

void setup() {
    pinMode(ledPin, OUTPUT);
    pinMode(inputPin, INPUT_PULLUP);
}
 void loop() {
  int swInput = digitalRead(inputPin);

  if (swInput == LOW) digitalWrite(ledPin, HIGH);
  else digitalWrite(ledPin, LOW);
 }
