int ch1 = A0;
int ch2 = A1;
float dt=0.0;

const int num_smpl = 200;
float x = 0.0;
float y = 0.0;
float dx = 0.0;
float dy = 0.0;
float d = 0.0;

float dat_t[num_smpl];
float dat_x[num_smpl];
float dat_y[num_smpl];
float E = 0.01*sqrt(2)*1023;  

char receivedChar;
boolean readData=false;


unsigned long time_start; // Start of capturing, ms
unsigned long time_end; // End of capturing, ms




void setup(){
  Serial.begin(38400);
  //Serial.print("Start\n");

}
void loop(){ 
  //test();  
  readData = true;
  while (readData){

    for(int i=0; i<num_smpl; i++){

      dat_x[i] = 0;
      dat_y[i] = 0;

    }
    dat_x[0] = analogRead(ch1);
    dat_y[0] = analogRead(ch2);
//    Serial.print(dat_x[0]);
//    Serial.print('\t');
//    Serial.println(dat_y[0]);

    for(int i=1; i<num_smpl; i++){
      do{
        x= analogRead(ch1);
        y = analogRead(ch2);;

        dx = dat_x[i-1] - x;
        dy = dat_y[i-1] - y;


        d = sqrt( sq(dx) + sq(dy));
//        Serial.print(i);
//        Serial.print('\t');
//        
//        Serial.print(dat_x[i-1]);
//        Serial.print('\t');
//        Serial.print(dat_y[i-1]);
//        Serial.print('\t');
//        
//        Serial.print(E);
//        ;
//
//        Serial.print('\t');      
//        Serial.println(d);
        dat_x[i] = x;
        dat_y[i] = y;
        dt+=0.01;
        //delayMicroseconds(200);
        //delay(500);
      }
      while( d < E );
      
dt+=0.01;
    }

    delay(100);


    for(int i=0; i<num_smpl; i++){
      Serial.print(millis());
     Serial.print(' '); 
      Serial.print(dat_x[i]);
      Serial.print(' ');
      Serial.println(dat_y[i]);
    }



    //test();
    //Serial.println('Next Sample');


  }


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

boolean test(){
  if (Serial.available() > 0) {
    receivedChar = Serial.read();
    switch(receivedChar){
    case 'r':
      readData = true;
      Serial.println("Start reading");
      return true;
      break;
    case 's':
      readData = false;
      Serial.println("Stop reading");
      return false;
      break;
    }

  }
}




















