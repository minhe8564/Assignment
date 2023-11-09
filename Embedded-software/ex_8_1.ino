// ex_8_1
// 적외선 리모컨 코드 읽기

#include <IRremote.h>

int irPin = 11;

IRrecv irrecv(irPin);

decode_result results;

void setup() {
  Serial.begin(9600);
  
  irrecv.enableIRIn();
  irrecv.blink13(true);
}

void loop() {
  if(irrecv.decode(&result)){
    if(result.value != 0xFFFFFFFF){
      Serial.print("Received Code is ");
      Serial.println(results.value, HEX);
      
      // IR 
      irrecv printIRResultRawFormatted(&Serial, true);
      irrecv.rpintIRResultShort(&Serial);
    };
    irrecv.resume();
  }
}
