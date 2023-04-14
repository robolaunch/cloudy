# Flysky Ibus 

<img style="width:30%; margin-left:auto; margin-right:auto; display:block" src="https://raw.githubusercontent.com/robolaunch/cloudy/docs/docs/images/flysky_ia6b.jpg"/>


Ibus channel could have between 6-10 channels due to transmitter and receiver. 4 of these channels are joysticks and the rest are switches, buttons and sliders. Each of these channels returns a data between 1000 and 2000 and you can transfer them to the feature you want by putting them in the map function, by default it can perform teleoperation with joysticks and on and off the microros feature with a switch.

https://github.com/bmellink/IBusBM

 Below, the value between 1000-2000 coming from any of the channels is printed on the screen.

    #include <IBusBM.h>

    IBusBM IBus;    // IBus object

    void setup() {
    Serial.begin(115200);     // debug info

    IBus.begin(Serial2,1);    // iBUS object connected to serial2 RX2 pin and use timer 1

    Serial.println("Start IBus2PWM_ESP32");
    }


    void loop() {
    int val;
    val = IBus.readChannel(0); // get latest value for servo channel 1

        Serial.println(val); // display value in microseconds on PC
    
    delay(100);
    }