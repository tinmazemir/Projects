void define_mz80(int pin)//Mz80 data pini tanimlama(Kahverengi-5V, Siyah-Data, Mavi-Gnd/Kirmizi-5V, Sari-Data, Yesil-Gnd) ***
{
  pinMode(pin, INPUT);
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


void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
