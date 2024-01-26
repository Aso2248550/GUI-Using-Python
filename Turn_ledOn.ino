char userIn;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN,OUTPUT);
}

void loop() {
 if(Serial.available()>0){
  userIn=Serial.read();
  if (userIn=='o'){
    digitalWrite(LED_BUILTIN,HIGH);
    Serial.println('on');
    delay(500);
  }
  if(userIn=='x'){
    digitalWrite(LED_BUILTIN,LOW);
    Serial.println('off');
    delay(500);
 }

}
}