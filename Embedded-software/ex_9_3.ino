// ex_9_3
// DS1302 RTC 모듈을 이용하여 시간 정보 읽기

#include <DS1302.h>

const int CEPin = 5;
const int IOPin = 6;
const int CLKPin = 7;

DS1302 rtc(CEPin, IOPin, CLKPin);

String dayAsString(const Time::Day day) {
  switch (day) {
    case Time::kSunday: return "Sunday";
    case Time::kMonday: return "Monday";
    case Time::kTuesday: return "Tuesday";
    case Time::kWednesday: return "Wednesday";
    case Time::kThursday: return "Thursday";
    case Time::kFriday: return "Friday";
    case Time::kSaturday: return "kSaturday";
  }
  return " (unknown day)";
}

void setup() {
  Serial.begin(9600);
  rtc.writeProtect(false);
  rtc.halt(false);

  Time t(2015, 8, 15, 00, 00, 00, Time::kSaturday);

  rtc.time(t);
}

void loop() {
  Time t = rtc.time();

  const String day =  dayAsString(t.day);

  Serial.print(day.c_str());
  Serial.print(" ");
  Serial.print(t.yr);
  Serial.print("-");
  Serial.print(t.mon);
  Serial.print("-");
  Serial.print(t.date);
  Serial.print(" ");
  Serial.print(t.hr);
  Serial.print(":");
  Serial.print(t.min);
  Serial.print(":");
  Serial.print(t.sec);

  delay(1000);
}
