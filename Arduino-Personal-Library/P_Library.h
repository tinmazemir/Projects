#include <QTRSensors.h>
#include <I2Cdev.h>
#include <MPU6050.h>
#include <Wire.h>


#define QTRSENS 1
#define GYRO 1

int EN_A;     //Birinci motor pwm pini
int IN1;       //Birinci motor kontrol pini
int IN2;       //Birinci motor kontrol pini
int IN3;       //Ikinci motor kontrol pini
int IN4;       //Ikinci motor kontrol pini
int EN_B;     //Ikinci motor pwm pini
int lastError = 0;


#if QTRSENS
  #define NUMBER_OF_SENSORS 8
  #define EMITTER_PIN 2
  QTRSensorsRC qtrrc((unsigned char[]) {2,3,4,5,6,7},6, 2500); //Qtr(Cizgi Sensoru) tanimlama **
  unsigned int sensorValues[8];
#endif

#if GYRO
  MPU6050 accelgyro;
  int16_t ax, ay, az;
  int16_t gx, gy, gz;
#endif

//******************************************************************************
//                            Setupta kullanilacak
//******************************************************************************

void define_motordriver(int en_a, int in1, int in2, int in3, int in4, int en_b)// Motor surucu pin tanimlama, en_a ve en_b pwm pini olmali ***
{
  EN_A = en_a;
  IN1 = in1;
  IN2 = in2;
  IN3 = in3;
  IN4 = in4;
  EN_B = en_b;
  pinMode(EN_A, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(EN_B, OUTPUT);
}

void define_mz80(int pin)//Mz80 data pini tanimlama(Kahverengi-5V, Siyah-Data, Mavi-Gnd/Kirmizi-5V, Sari-Data, Yesil-Gnd) ***
{
  pinMode(pin, INPUT);
}

void define_ultrasonic(int trigPin, int echoPin)//Ultrasonik pin tanimlama(Vcc-5V, Trig-HerhangiBirDigital, Echo-HerhangiBirDigital, Gnd-Gnd) ***
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void define_button(int buttonPin)//Buton tanimlama(HerhangiBirDigital) **
{
  pinMode(buttonPin, INPUT_PULLUP);
}

void define_encoder(int encoder0PinA, int encoder0PinB)
{
  pinMode (encoder0PinA, INPUT);
  pinMode (encoder0PinB, INPUT);
}

void start_gyro()//Gyro baslatma **
{
  Wire.begin();
  accelgyro.initialize();
}

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


//******************************************************************************
//                            Loopta kullanilacak
//******************************************************************************

void drive(int motor, int speed)//Motor numarasi ve hiz vererek surme, motor-1,2 ***
{
  if(speed > 255)
  {
    speed = 255;
  }
  else if(speed < -255)
  {
    speed = -255;
  }

  if(motor == 1)
  {
    if(speed > 0)
    {
      digitalWrite(IN1 , HIGH);
      digitalWrite(IN2 , LOW);
      analogWrite(EN_A, speed);
    }
    else if(speed < 0)
    {
      digitalWrite(IN1 , LOW);
      digitalWrite(IN2 , HIGH);
      analogWrite(EN_A, -speed);
    }
    else
    {
      digitalWrite(IN1 , LOW);
      digitalWrite(IN2 , LOW);
      analogWrite(EN_A, speed);
    }
  }
  else if(motor == 2)
  {
    if(speed > 0)
    {
      digitalWrite(IN3 , HIGH);
      digitalWrite(IN4 , LOW);
      analogWrite(EN_B, speed);
    }
    else if(speed < 0)
    {
      digitalWrite(IN3 , LOW);
      digitalWrite(IN4 , HIGH);
      analogWrite(EN_B, -speed);
    }
    else
    {
      digitalWrite(IN3 , LOW);
      digitalWrite(IN4 , LOW);
      analogWrite(EN_B, speed);
    }
  }
}

void forward(int speed)//Ileri gitme ***
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(EN_A, speed);
  analogWrite(EN_B, speed);
}

void back(int speed)//Geri gitme ***
{
  digitalWrite(IN1 , LOW);
  digitalWrite(IN2 , HIGH);
  digitalWrite(IN3 , LOW);
  digitalWrite(IN4 , HIGH);
  analogWrite(EN_A, speed);
  analogWrite(EN_B, speed);
}

void right(int speed)//Kendi etrafinda saga donme ***
{
  digitalWrite(IN1 , HIGH);
  digitalWrite(IN2 , LOW);
  digitalWrite(IN3 , LOW);
  digitalWrite(IN4 , HIGH);
  analogWrite(EN_A, speed);
  analogWrite(EN_B, speed);
}

void left(int speed)//Kendi etrafinda sola donme ***
{
  digitalWrite(IN1 , LOW);
  digitalWrite(IN2 , HIGH);
  digitalWrite(IN3 , HIGH);
  digitalWrite(IN4 , LOW);
  analogWrite(EN_A, speed);
  analogWrite(EN_B, speed);
}

int pid(int position, float Kp, float Kd, int target)
{
  int error = position - target;
  int motorSpeed = Kp * error + Kd * (error - lastError);
  lastError = error;
  return motorSpeed;
}

unsigned int qtr_read()//Sensorden gelen veriyi okuma ***
{
  unsigned int position = qtrrc.readLine(sensorValues);
  return position;

}

int gyro_read(int return_val)// Gyrodan gelen veriyi okuma(1-Ax, 2-Ay, 3-Az, 4-Gx, 5-Gy, 6-Gz) **
{
  accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  switch(return_val)
  {
    case 1:
      return ax;
    case 2:
      return ay;
    case 3:
      return az;
    case 4:
      return gx;
    case 5:
      return gy;
    case 6:
      return gz;
  }
}

int mz80_read(int pwmPin) // mz80 pwm pin alir engel varsa "is_obstacle" 1 doner yoksa 0 doner ***
{
   int is_obstacle;
   int val = digitalRead(pwmPin);
   if(val == 1)
   {
      is_obstacle = 0;
      return is_obstacle;
   }
   else if(val == 0)
   {
      is_obstacle = 1;
      return is_obstacle;
   }

}

int  button_read(int buttonPin,unsigned int debounceDelay = 5) // debounceDelay kac milisaniye sonra buttonu aktif olacagini belirler(standart 50 girilir)
{
   unsigned int start = millis();
   int value = digitalRead(buttonPin);
   if(value == HIGH)
   {
    if(millis()-start < debounceDelay)
    {
       return 0;
    }
   }
   else
   {
    start = millis();
   }
   return 1;
}

int ultrasonic_read(int trigPin, int echoPin, int averageNumber = 10, int passTimer = 2, int acTimer = 10) // setupta tanimlanan trigPin ile echoPin i tekrar giriniz  ***
{
   float average = 0;                                                                          //passTimer ve acTimer sureleri default cok acil gerekirse degistirin
   long duration;                                                                              // averageNumber()default 10) ise kac degerin ortalamasinin alinacagi
   long distance;
   digitalWrite(trigPin, LOW); /* sensör pasif hale getirildi */
   delayMicroseconds(passTimer);
   digitalWrite(trigPin, HIGH); /* Sensore ses dalgasının üretmesi için emir verildi */
   delayMicroseconds(acTimer);
   digitalWrite(trigPin, LOW);  /* Yeni dalgaların üretilmemesi için trig pini LOW konumuna getirildi */
   duration = pulseIn(echoPin, HIGH); /* ses dalgasının geri dönmesi için geçen sure ölçülüyor */
   distance = duration/58.2;
   for(int i = 0; i <= averageNumber; i++)
   {
      average = distance + average;
   }
   return average/averageNumber;
}

int encoder(int encoder0PinA, int encoder0PinB)// aciklama yaz
{
   int encoder0Pos;
   int encoder0PinALast = LOW;
   int n = LOW;
   n = digitalRead(encoder0PinA);
   if ((encoder0PinALast == LOW) && (n == HIGH))
   {
      if (digitalRead(encoder0PinB) == LOW)
      {
         encoder0Pos--;
      }
      else
      {
         encoder0Pos++;
      }
    return encoder0Pos;
   }
   encoder0PinALast = n;
}
