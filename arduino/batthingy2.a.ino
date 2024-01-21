#include <Servo.h>
#define PIN_TRIG 12
#define PIN_ECHO 11
long duration, cm;
int servoAngle = 90;
Servo myservo1;

void setup() {
  Serial.begin(9600);
  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
  myservo1.attach(13);
  myservo1.write(servoAngle);
}
void loop() {
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(5);
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG,LOW);
  duration = pulseIn(PIN_ECHO,HIGH);
  cm=(duration / 2) / 29.1;
  myservo1.write(servoAngle);
  if(servoAngle<=160){
  servoAngle +=10;
  }else if(servoAngle>=160){
    servoAngle -=10;}
  Serial.print("Расстояние до объекта:");
  Serial.print(cm);
  Serial.println(" см.");
  delay(250);
}
