#include <Arduino.h>

int t = 0;
int j = 2;
float pi = 3.14159265359;
float sinus = 1;
float cosinus = 0;
float sinus2 = 0;
float cosinus2 = 0;
byte * s = (byte *)&sinus;
byte * c = (byte *)&cosinus;
byte * s2 = (byte *)&sinus2;
byte * c2 = (byte *)&cosinus2;
float Frequenz = 2*pi*1/50;

void setup() {
    Serial.begin(115200);
    Serial.flush();
}

void loop() {
    sinus = sin(Frequenz*t+90);
    cosinus = cos(Frequenz*t);
    sinus2 = sin(Frequenz*t);
    cosinus2 = cos(Frequenz*t+90);

    Serial.write(s,4);
    delay(10); // entspricht 100 Hz
    //Serial.write(c,4);
    //delay(2);
    //Serial.write(s2,4);
    //delay(2);
    //Serial.write(c2,4);
    //delay(2);

}