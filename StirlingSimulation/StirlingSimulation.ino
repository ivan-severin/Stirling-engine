float dt=0.0;


void setup() {
  Serial.begin(38400);

}

void loop() {

  Serial.print(get_x());
  Serial.print("  ");
  Serial.println(get_y());
  dt+=0.8;
  delay(5);
}



float get_x(){
  float arc=0.002*random(10);
  float pi=3.1415;
  float R=512;

  return R*(cos(pi*dt*0.01 ) + arc);

}
float get_y(){
  float arc=0.002*random(10);
  float pi=3.1415;
  float R=512.0;
  return R*(0.3+sin(pi*dt*0.01) + arc);

}
