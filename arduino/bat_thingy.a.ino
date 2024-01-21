#define PIN_TRIG 12
#define PIN_ECHO 11
long duration, cm;

void setup() {
  Serial.begin(9600);
  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
}
void loop() {
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(5);
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG,LOW);
  duration = pulseIn(PIN_ECHO,HIGH);
  cm=(duration / 2) / 29.1;
  Serial.print("Расстояние до объекта:");
  Serial.print(cm);
  Serial.println(" см.");
  delay(250);
}
