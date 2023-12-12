#include <LiquidCrystal_I2C.h>
#include <SimpleTimer.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int led = 7;
const int alarm = 8;
int sensorValue = 0;
int button = 2;

SimpleTimer timer;
int pState = LOW;
boolean booked = false;
void setup()
{
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  pinMode(button, INPUT);
  
  lcd.init();
  lcd.backlight();
}

void loop()
{
  sensorValue = analogRead(A0);
  int hours = map(sensorValue, 0, 1023, 0, 12);
  
  Serial.print("sensorValue : ");
  Serial.println(sensorValue);
  
  delay(100);
  
  lcd.setCursor(0, 0);
  lcd.print("Alarm : ");
  lcd.print(hours);
  lcd.print("hours   ");
  
  
  int state = digitalRead(button);
  if(pState == LOW && state == HIGH){
    if(booked == false){
    booked = true;
    digitalWrite(led, LOW);
    timer.setTimeout(hours * 1000, beep);
      
    for (int i = hours; i >= 0; i--) {
      lcd.setCursor(0, 1);
      lcd.print("Remain : ");
      lcd.print(i);
      lcd.print("hours   ");
      delay(1000);
    }
    }
  }
  pState = state;
  timer.run(); 
}

void beep(){
  booked = false;
  digitalWrite(led, HIGH);
  tone(8, 1000, 20);
  delay(100);
  tone(8, 1000, 20);
  delay(100);
  tone(8, 1000, 20);

}
