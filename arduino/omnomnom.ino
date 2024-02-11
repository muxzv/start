#define trigPin 9
#define echoPin 8
#define led 10
#define servopin 7

#define chewing 4
#define blizost 10

#define mouthClose 90
#define mouthOpen 30
#define mouthAjar 70

#include <Servo.h>
Servo Sergo;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  Sergo.attach(servopin);
  sleep();
}

void loop() {
  int duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration / 58;
  Serial.print(distance);
  Serial.println("cm");

  if (distance < blizost){
    om_nom_nom();
    digitalWrite(led, HIGH);
  }
  delay(100);
}

void om_nom_nom(){
  digitalWrite(led, HIGH);
  Sergo.attach(servopin);
  delay(200);

  Sergo.write(mouthOpen);
  delay(700);
  
  for (int x = 0; x < chewing; x++){
    Sergo.write(mouthAjar);
    delay(250);
    Sergo.write(mouthOpen);
    delay(250);
    Serial.println("nyam");
  }
  sleep();
}

void sleep(){
  Sergo.write(mouthClose);
  delay(250);

  Sergo.detach();
  digitalWrite(led, LOW);
}
