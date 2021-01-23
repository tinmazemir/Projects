
void define_encoder(int encoder0PinA, int encoder0PinB)
{
  pinMode (encoder0PinA, INPUT);
  pinMode (encoder0PinB, INPUT);
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


void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
