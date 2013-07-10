#define BAUDRATE 115200

#include <LightSwitch.h>
#include <DoorSwitch.h>

LightSwitch lightSwitch(2,13);
DoorSwitch door(7);
boolean doorLast;

void setup()
{
  Serial.begin(BAUDRATE);
  doorLast = door.isOpen();
}

void loop()
{
  if(doorLast != door.isOpen())
  {
    doorLast = door.isOpen();
    if(doorLast)
    {
      Serial.write("Door is Open");
      delay(100);
    }
    else
    {
      Serial.write("Door is Closed");
      delay(100);
    //doorLast != doorLast;
    }
  }
  if(lightSwitch.changed())
  {
    if(lightSwitch.incended())
    {
      Serial.write("Light On");
      delay(10);
    }
    else
    {
      Serial.write("Light Off");
      delay(10);
    }
  }
 if(Serial.available())
 {
  char temp = ' ';
  temp = Serial.read();
  delay(100);
  if(temp == 'k')
  {
    if(lightSwitch.incended())
    {
      Serial.write("Light On");
      delay(10);
    }
    else
    {
      Serial.write("Light Off");
      delay(10);
    }
  }
  else if(temp == 'l')
  {
    if(!lightSwitch.incended())
    {
      Serial.write("Light Already Off");
      delay(10);
    }
    else
    {
      lightSwitch.flip();
      Serial.write("Light Off");
      delay(10);
    }
  }
  else if(temp == 'L')
  {
    if(lightSwitch.incended())
    {
      Serial.write("Light Already On");
      delay(10);
    }
    else
    {
      lightSwitch.flip();
      Serial.write("Light On");
      delay(10);
    }
  }
  temp = ' ';
 }
}
