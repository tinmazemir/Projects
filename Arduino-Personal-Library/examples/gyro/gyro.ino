#define GYRO 1

#if GYRO
  MPU6050 accelgyro;
  int16_t ax, ay, az;
  int16_t gx, gy, gz;
#endif


void start_gyro()//Gyro baslatma **
{
  Wire.begin();
  accelgyro.initialize();
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

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:

}
