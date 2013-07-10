#ifndef LightSwitch_h
#define LightSwitch_h

#include "Arduino.h"

class LightSwitch
{
    public:
        LightSwitch(int pin, int swPin);
        bool incended();
        void flip();
        bool resolve();
        bool changed();
    private:
        int _outPin;
        int _swPin;
        bool _incended;
        int _swState;
        bool _digState;
};

#endif
