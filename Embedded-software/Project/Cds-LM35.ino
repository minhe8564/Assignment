int illuminance = 0;
int temperature = 0;

int CdSPin = A0;
int LM35Pin = A1;
int yellowPin = 3;
int redPin = 4;
int bluePin = 5;

void setup()
{
  Serial.begin(9600);

  pinMode(CdSPin, INPUT);
  pinMode(LM35Pin, INPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop()
{
  illuminance = analogRead(CdSPin);

  if (illuminance <= 200) {
    digitalWrite(yellowPin, HIGH);
  } else {
    digitalWrite(yellowPin, LOW);  
  }

  Serial.print("Current illuminance: ");
  Serial.println(illuminance);

  temperature = -40 + 0.488155 * (analogRead(LM35Pin) - 20);
  if (temperature > 50){
    Serial.print("Temperature is too high! Current temperature: ");
    Serial.print(temperature);
    Serial.println(" C.");
    digitalWrite(redPin, HIGH);
  }
  else{
    digitalWrite(redPin, LOW);
  }
  
  if (temperature < 0){
    Serial.print("Temperature is too low! Current temperature: ");
    Serial.print(temperature);
    Serial.println(" C.");
    digitalWrite(bluePin, HIGH);
  }
  else{
    digitalWrite(bluePin, LOW);
  }
  
  delay(3000);
}
