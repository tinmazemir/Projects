int EN_A;     //Birinci motor pwm pini
int IN1;       //Birinci motor kontrol pini
int IN2;       //Birinci motor kontrol pini
int IN3;       //Ikinci motor kontrol pini
int IN4;       //Ikinci motor kontrol pini
int EN_B;     //Ikinci motor pwm pini
int lastError = 0;

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

void setup() 
{
}

void loop() 
{
}
