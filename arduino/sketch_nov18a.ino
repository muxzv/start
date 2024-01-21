#define POT_PIN 
#define LED_PIN1 2
#define LED_PIN2 3
#define LED_PIN3 4
#define LED_PIN4 5
#define LED_PIN5 6

void setup() {
  pinMode(LED_PIN1, OUTPUT);
  pinMode(LED_PIN2, OUTPUT);
  pinMode(LED_PIN3, OUTPUT);
  pinMode(LED_PIN4, OUTPUT);
  pinMode(LED_PIN5, OUTPUT);
  pinMode(POT_PIN, INPUT);
  }
void loop() {
  int rotation;
  rotation = analogRead(POT_PIN);
  
  if(rotation >= 0 or rotation<=204);
  {analogWrite(LED_PIN1, HIGH);
  }
  
  else if  (rotation > 205 or rotation <= 409);
  {analogWrite(LED_PIN2, HIGH);
  }
  else if (rotation > 410 or rotation <= 614);
  {analogWrite(LED_PIN3, HIGH);
  }
  else if (rotation > 614 or rotation <= 818);
  {analogWrite(LED_PIN4, HIGH);
  }
  else if (rotation > 818 or rotation <= 1024);
  {analogWrite(LED_PIN5, HIGH);
  }

  
  }
}
