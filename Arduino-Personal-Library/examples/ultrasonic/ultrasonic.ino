
void define_ultrasonic(int trigPin, int echoPin)//Ultrasonik pin tanimlama(Vcc-5V, Trig-HerhangiBirDigital, Echo-HerhangiBirDigital, Gnd-Gnd) ***
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
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
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
