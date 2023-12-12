#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int buttonPin = 7;

int greenPin = 3;
int bluePin = 4;
int redPin = 5;

String messages[] = {
  "Stay strong, smile",
  "Cheer up!",
  "Never give up!",
  "Aging is not 'lost",
  "You're amazing!",
  "Believe in yourself",
  "Enjoy your moment",
  "The best is yet",
  "Keep going strong",
  "Live with gratitude",
  "Age is opportunity",
  "Stay young at heart",
  "Cherish every day",
  "I love you!"
};

void setup()
{
  Serial.begin(9600);

  pinMode(buttonPin, INPUT);

  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(redPin, OUTPUT);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("start");
}

void loop()
{
  int readValue = digitalRead(buttonPin);

  if (readValue == HIGH)
  {
    displayRandomMessage();
  }
}

void displayRandomMessage()
{
  // 랜덤하게 배열에서 하나의 문구를 선택
  int randomIndex = random(0, sizeof(messages) / sizeof(messages[0]));
  String message = messages[randomIndex];

  digitalWrite(greenPin, random(2));
  digitalWrite(bluePin, random(2));
  digitalWrite(redPin, random(2));

  lcd.setCursor(0, 0);
  lcd.print(message.substring(0, 16));
  lcd.setCursor(0, 1);
  lcd.print(message.substring(16));
  
  Serial.println("Random Message: " + message);
  
  delay(3000);
  lcd.clear();
}
