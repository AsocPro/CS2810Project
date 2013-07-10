#ifndef DoorSwitch_h
#define DoorSwitch_h

#include "Arduino.h"

class DoorSwitch
{
    public:
        DoorSwitch(int pin);
        bool isOpen();
    private:
        int _isOpen;
        int _pin;
};

#endif
