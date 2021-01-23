#include <QTRSensors.h>
#define QTRSENS 1
#if QTRSENS
  #define NUMBER_OF_SENSORS 8
  #define EMITTER_PIN 2
  QTRSensorsRC qtrrc((unsigned char[]) {2,3,4,5,6,7},6, 2500); //Qtr(Cizgi Sensoru) tanimlama **
  unsigned int sensorValues[8];
#endif

void calibrate_qtr()//Kalibre etme ***
{
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
  for (int i = 0; i < 400; i++)
  {
    qtrrc.calibrate();
  }
  digitalWrite(13, LOW);
}


unsigned int qtr_read()//Sensorden gelen veriyi okuma ***
{
  unsigned int position = qtrrc.readLine(sensorValues);
  return position;

}

void setup() 
{
}

void loop() 
{
}
