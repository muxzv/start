#define A 8
#define B 7
#define C 6
#define D 5
#define E 4
#define F 3
#define G 2
#define BUTTON 12
byte v = 0;
void setup() {
  pinMode(A, OUTPUT); pinMode(B, OUTPUT);
  pinMode(C, OUTPUT); pinMode(D, OUTPUT);
  pinMode(E, OUTPUT); pinMode(F, OUTPUT);
  pinMode(G, OUTPUT); pinMode(BUTTON, INPUT);
}

void loop() {
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, LOW);

if (digitalRead(BUTTON) == HIGH){delay(500); v = 1; }

  while (v == 3){
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, LOW);
      digitalWrite(F, LOW);
      digitalWrite(G, HIGH);
      if (digitalRead(BUTTON) == HIGH) { delay(500); v = 0; }
    }
}
