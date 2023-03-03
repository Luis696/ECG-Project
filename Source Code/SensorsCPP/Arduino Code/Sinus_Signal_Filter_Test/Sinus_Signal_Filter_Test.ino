
float t;
int signal_frequency = 10;
int sample_frequency = 200;
int number_samples = 200;
int sampling_interval;
int sampling_interval_noise_50;
int sampling_interval_noise_1;
float signal[200];
float sinus;
byte * s = (byte *)&sinus;

void setup() {
  Serial.begin(115200);
  Serial.flush();
  for(int n = 0; n<number_samples; n++)
  {
    t = (float) n/sample_frequency; 
    signal[n] = sin(2*3.14*t);
  }
  sampling_interval = 1000000 / (signal_frequency*number_samples);
  sampling_interval_noise_50 = 1000000 / (1*number_samples); // 50 Hz Rauschen
  sampling_interval_noise_1 = 1000000/ (1 * number_samples); // 1 Hz Rauschen
}

void loop() {
  for(int j = 0; j<number_samples; j++)
  {
    //sinus = signal[j];
    //Serial.write(s,4);
    //delayMicroseconds(sampling_interval);
    sinus = 3*signal[j];
    Serial.write(s,4);
    delayMicroseconds(sampling_interval);
    // sinus = 3*signal[j];
    // Serial.write(s,4);
    // delayMicroseconds(sampling_interval_noise_1);
  }

}
