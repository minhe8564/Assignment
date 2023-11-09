// ex_9_1
// 피에조 버저를 이용한 소리 출력

int buzzerPin = 9;
int songLength = 16;

char notes[] = "cee egg dff abb";
int beats[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

int tempo = 200;

void setup() {
    pinMode(buzzerPin, OUTPUT);
}

void loop() {
  int duration;

  for(int i = 0; i < songLength; i++){
    duration = beats[i] * tempo;

    if(notes[i] == ' ') {
      dealy(duration);
    }
    else {
      tone(buzzerPin, frequency(notes[i]), duration);
      delay(duration);
    }

    delay(tempo / 10);
  }
}

int frequency(char note){

  int i;
  int notes = 8;

  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c' };
  int frequencies[] = {262, 294, 330, 349, 392, 440, 494, 523};

  for(i = 0; i < notes; i++){
    if (names[i] == note){
      return(frequencies[i]);
    };
  };

  return(0);
}
