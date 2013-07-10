#include "Arduino.h"
#include "LightSwitch.h"

LightSwitch::LightSwitch(int iPin, int oPin)
{
    pinMode(oPin, OUTPUT);
    _outPin = oPin;
    _incended = false;
    pinMode(iPin, INPUT);
    _swPin = iPin;
    _digState = false;
}
bool LightSwitch::incended()
{
    return _incended;
}
void LightSwitch::flip()
{
    _digState = !_digState;
    resolve();
}
bool LightSwitch::resolve()
{
    _swState = digitalRead(_swPin);
    if((_swState == HIGH && _digState == true) || (_swState == LOW && _digState == false))
    {
        _incended = false;
        digitalWrite(_outPin, LOW);
        return false;
    }
    else
    {
        _incended = true;
        digitalWrite(_outPin, HIGH);
        return true;
    }
}
bool LightSwitch::changed()
{
    bool temp = _incended;
    _incended = resolve();
    return temp != _incended;
}
