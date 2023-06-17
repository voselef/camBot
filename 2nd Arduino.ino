// Second Arduino's code. Please look at the circuit schema at README.md
void setup(){
  Serial.begin(115200); // Started serial connetion with Discord Bot
  pinMode(12,OUTPUT);
  pinMode(11,INPUT);
  digitalWrite(12,0);
}
void loop(){
  if(digitalRead(11) == HIGH){
    digitalWrite(12,0);
  }
  if(Serial.available() > 0){
    String comerMsg = Serial.readString();
    if(comerMsg == "p"){
      digitalWrite(12,1);
    }
  }
}
