## Motor Control

<img style="width:50%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/cnc_shield_esp32.jpg"/>

Step motors control with step pulses, and esp32 controller have built in pwm module, fastaccelstepper.h library use that pwm module. This library can download from arduino ide builtin libraries. 

Simple example to control the motor down below.


    #include "FastAccelStepper.h"

    //#define dirPinStepper    5
    //#define enablePinStepper 6
    //#define stepPinStepper   9 

    // As in StepperDemo for Motor 1 on ESP32
    #define dirPinStepper 18
    #define enablePinStepper 26
    #define stepPinStepper 17

    FastAccelStepperEngine engine = FastAccelStepperEngine();
    FastAccelStepper *stepper = NULL;

    void setup() {
    engine.init();
    stepper = engine.stepperConnectToPin(stepPinStepper);
    if (stepper) {
        stepper->setDirectionPin(dirPinStepper);
        stepper->setEnablePin(enablePinStepper);
        stepper->setAutoEnable(true);

        // If auto enable/disable need delays, just add (one or both):
        // stepper->setDelayToEnable(50);
        // stepper->setDelayToDisable(1000);

        stepper->setSpeedInUs(1000);  // the parameter is us/step !!!
        stepper->setAcceleration(100);
        stepper->move(1000);
    }
    }

    void loop() {}
