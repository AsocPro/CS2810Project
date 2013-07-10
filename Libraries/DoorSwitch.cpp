#include "Arduino.h"
#include "DoorSwitch.h"

DoorSwitch::DoorSwitch(int pin)
{
    pinMode(pin, INPUT);
    _pin = pin;
}
bool DoorSwitch::isOpen()
{
    _isOpen = digitalRead(_pin);
    if(_isOpen == HIGH)
    {
        return true;
    }
    else
    {
        return false;
    }
}
