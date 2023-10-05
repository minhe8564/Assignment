#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int CdsPin = 0;

void setup() {
    lcd.init();
    lcd.backlight();

    lcd.print("ex 6.2");
    lcd.setCursor(0,1);
    lcd.print("Cds Cell Test");
    delay(3000);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("ADC: ");
    lcd.setCursor(0, 1);
    lcd.print("Illuminance: ");
    lcd.setCursor(15, 1);
    lcd.print("%");
}

void loop(){
  int adcValue;
  int illuminance;

  adcValue = analogRead(CdsPin);
  illuminance = map(adcValue, 0, 1023, 100, 0);

  lcd.setCursor(9, 0);
  lcd.print("     ");
  lcd.setCursor(9, 0);
  lcd.print(adcValue);

  lcd.setCursor(13, 1);
  lcd.print("     ");
  lcd.setCursor(12, 1);
  lcd.print(illuminance);

  delay(1000);
}
