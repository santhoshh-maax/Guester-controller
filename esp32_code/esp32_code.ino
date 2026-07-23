int led1 = 2;   // Command '1'
int led2 = 4;   // Command '2'
int led3 = 5;   // Command '3'

void setup() {
  Serial.begin(9600);

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);

  // Initial state — all OFF
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);

  Serial.println("ESP32 Ready (3 LED Mode)");
}

void loop() {

  if (Serial.available()) {

    char cmd = Serial.read();

    Serial.print("Received command: ");
    Serial.println(cmd);

    if (cmd == '1') {
      // LED1 ON
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
      digitalWrite(led3, LOW);

      Serial.println("LED1 ON");
    }

    else if (cmd == '2') {
      // LED2 ON
      digitalWrite(led1, LOW);
      digitalWrite(led2, HIGH);
      digitalWrite(led3, LOW);

      Serial.println("LED2 ON");
    }

    else if (cmd == '3') {
      // LED3 ON
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);
      digitalWrite(led3, HIGH);

      Serial.println("LED3 ON");
    }

    else {
      // All OFF
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);
      digitalWrite(led3, LOW);

      Serial.println("All LEDs OFF");
    }
  }
}