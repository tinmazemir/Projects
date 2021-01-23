
void define_button(int buttonPin)//Buton tanimlama(HerhangiBirDigital) **
{
  pinMode(buttonPin, INPUT_PULLUP);
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


void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
