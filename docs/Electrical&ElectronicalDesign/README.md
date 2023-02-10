# Getting Started
Cloudy uses the esp32 micro controller on the embedded hardware side.

Cloudy robot has a Hardware Stack containing the main electronics and computer, all the parts here are cooled by a powerful fan. The Hardware Stack is easily separated from the body of the cloudy, which allows you to easily replace them and use them outside of the robot.<br/>
<img style="width:170px; height:170px;" src="https://ae01.alicdn.com/kf/H4de861835bb241de85a0f85ce23112f9a/ESP32-Wemos-D1-Mini-Arduino-UNO-i-in-R3-D1-R32-WIFI-kablosuz-bluetooth-geli-tirme.jpg_Q90.jpg_.webp"/>
  <figcaption>Esp32 Wemos D1 Uno</figcaption>
<br/>
The first layer of the Hardware Stack contains an esp32 microcontroller. This board is known as uno esp32 and is compatible with most arduino uno shields.<br/><br/><br/>
<img style="width:170px; height:170px; float:left;" src="https://st.myideasoft.com/idea/cd/40/myassets/products/058/cnc-shield.jpg?revision=1484509194"/>
<img style="width:170px; height:170px;" src="https://image.robotistan.com/vnh3asp30-step-motor-surucusu-38119-98-O.jpg"/>  
<figcaption>CNC Shield - Monster Moto Shield</figcaption><br/>
The second layer contains shield for the motor drivers. Depending on your motor type (step, dc, brushless) you can choose different shield to the compatible driver board.this layer ensures the stable operation of the motor drivers.<br/><br/><br/>
<img style="width:170px; height:170px; float:left;" src="https://m.media-amazon.com/images/I/41cn6diLE0L.jpg"/>
<img style="width:170px; height:170px;" src="https://live.staticflickr.com/65535/52217221682_6e7508c486_o.png"/>
<img style="width:170px; height:170px;" src="https://www.robotsepeti.com/nvidia-jetson-nano-2gb-developer-kit-wifi-nvidia-nvidia-13114-68-B.png"/>
<img style="width:180px; height:120px;" src="https://www.intel.com.tr/content/dam/www/central-libraries/us/en/images/nuc11-product.png.rendition.intel.web.576.324.png"/>
  <figcaption>Raspberry Pi 4 - Orange Pi 5 - Jetson Nano - Intel Nuc</figcaption><br/>
On the top layer, there is a single board computer. Cloudy supports raspberry pi, orange pi 5, jetson nano and Intel Nuc computers. You can easily access the USBs on it and use add-ons such as stereo camera and lidar.
<br/>
<br/>
In addition, the body of the Cloudy is equipped with many sensors. These sensors work with i2c protocol and are connected with i2c multiplexer so you can connect multiple same sensors.Cloudy includes 3 distance sensors, 2 for collision avoidance in the bumper, and 1 for protection from falling from a height. Also there are neopixel LEDs on all four sides, these LEDs are used for robot visibility and status indication. You can learn the battery voltage and status with the tiny oled screen at the top.
<br/>
<br/><br/>
<br/>
<img style="width:170px; height:170px; float:left;" src="https://st.myideasoft.com/idea/cd/40/myassets/products/827/ws2812-8li-serit-rgb-led-modulu-rgb-stick-modul-drone-1-1.JPG?revision=1582459848"/>
<img style="width:170px; height:170px;" src="https://www.direnc.net/vl6180-optik-sensor-modulu-arduino-uyumlu-lazer-ve-lazerli-sensorler-estardyn-40330-14-B.jpg"/>
<img style="width:170px; height:170px;" src="https://www.robotistan.com/13-inch-i2c-oled-ekran-ssd1106-25686-80-O.jpg"/>
<img style="width:170px; height:170px;" src="https://robiz.net/image/cache/data/sensors/gyro/mpu6050/mpu6050_01-500x500.jpg"/>
<br/><br/><br/>