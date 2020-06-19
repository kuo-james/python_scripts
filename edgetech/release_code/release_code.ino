
int pin = 8;
int pulse = 22;
int period = 248;

void setup() {
  // put your setup code here, to run once:
  tone(pin, 9900, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);
  tone(pin, 9500, pulse);

  delay(5000+period+16);
  
  tone(pin, 9900, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);
  tone(pin, 9900, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);
  tone(pin, 9900, pulse);
  delay(period);
  tone(pin, 9500, pulse);
  delay(period);

}

void loop() {
  // put your main code here, to run repeatedly:

}
