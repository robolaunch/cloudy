# Sensors

##  INA219 Voltage And Current
<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://ae01.alicdn.com/kf/Hf8e46be8e1b044bba6ced52175c80ca0c/10-adet-INA219-GY-219-GY219-ak-m-g-kayna-sens-r-kesme-panosu-mod-l.jpg_Q90.jpg_.webp"/>
<a href="https://tr.aliexpress.com/item/4000983502344.html?spm=a2g0o.productlist.main.15.74684be78NNSOq&algo_pvid=5385c799-29fd-4e92-ab3a-8278056e2b2c&aem_p4p_detail=202303010026424541665638641810003817171&algo_exp_id=5385c799-29fd-4e92-ab3a-8278056e2b2c-7&pdp_ext_f=%7B%22sku_id%22%3A%2210000013192851076%22%7D&pdp_npi=3%40dis%21TRY%2133.86%2127.45%21%21%21%21%21%402100baf316776592024184587d06d2%2110000013192851076%21sea%21TR%21800775013&curPageLogUid=yz0chc5OdZDn&ad_pvid=202303010026424541665638641810003817171_8&ad_pvid=202303010026424541665638641810003817171_8">

INA219</a> sensor utilizes the I2C protocol to provide voltage and current readings. It has a maximum voltage measurement capability of 26V, which is sufficient for monitoring LiPo or Li-ion battery packs with up to 6S. Additionally, it can measure the robot's current consumption up to 3.2 amps.

```/voltage [Float8]``` Topic is publish Battery Voltage </br>
```/current [Float8]``` Topic is publish Instant Current

https://github.com/adafruit/Adafruit_INA219

```
#include <Wire.h>
#include <Adafruit_INA219.h>
Adafruit_INA219 ina219;
void setup(void) 
{
  Serial.begin(115200);
  while (!Serial) {
      delay(1);
  }    
  Serial.println("Hello!");
  if (! ina219.begin()) {
    Serial.println("Failed to find INA219 chip");
    while (1) { delay(10); }
  }
  Serial.println("Measuring voltage and current with INA219 ...");
}
void loop(void) 
{
  float shuntvoltage = 0;
  float busvoltage = 0;
  float current_mA = 0;
  float loadvoltage = 0;
  float power_mW = 0;

  shuntvoltage = ina219.getShuntVoltage_mV();
  busvoltage = ina219.getBusVoltage_V();
  current_mA = ina219.getCurrent_mA();
  power_mW = ina219.getPower_mW();
  loadvoltage = busvoltage + (shuntvoltage / 1000);
  Serial.print("Bus Voltage:   "); Serial.print(busvoltage); Serial.println(" V");
  Serial.print("Shunt Voltage: "); Serial.print(shuntvoltage); Serial.println(" mV");
  Serial.print("Load Voltage:  "); Serial.print(loadvoltage); Serial.println(" V");
  Serial.print("Current:       "); Serial.print(current_mA); Serial.println(" mA");
  Serial.print("Power:         "); Serial.print(power_mW); Serial.println(" mW");
  Serial.println("");
  delay(2000);
}

}
```
 
## APDS-8960 Distance Sensors 

<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://productimages.hepsiburada.net/s/24/375/10076208332850.jpg"/>
<a href="https://tr.aliexpress.com/item/1005003518769618.html?spm=a2g0o.productlist.main.15.27383618OKAScH&algo_pvid=be2f2ec7-98fa-46a3-8b44-ca692cce9eaa&aem_p4p_detail=202303010104574003209801479040003846531&algo_exp_id=be2f2ec7-98fa-46a3-8b44-ca692cce9eaa-7&pdp_ext_f=%7B%22sku_id%22%3A%2212000026150196181%22%7D&pdp_npi=3%40dis%21TRY%2137.67%2137.67%21%21%21%21%21%402100baf316776614974026237d06d2%2112000026150196181%21sea%21TR%21800775013&curPageLogUid=PKbIWPDJSLLR&ad_pvid=202303010104574003209801479040003846531_8&ad_pvid=202303010104574003209801479040003846531_8">

APDS-9960</a> sensor is an advanced sensor with several features. With its distance measurement feature, it allows the robot to detect objects in front of it. In addition, the robot has this sensor in its bumper to detect the ground. This safety feature allows the robot to navigate high surfaces safely without any risk of falling. The sensor also features hand gesture detection and allows the user to send commands to the robot with intuitive gestures. This feature makes it easy for anyone, regardless of technical expertise, to control the robot. Finally, the sensor includes an RGB color detection feature that provides information about the colors in the robot's environment. It has many practical applications such as adding this feature to the bottom sensor of the robot and recognizing the ground color.

 ```/right_collision_distance [Float8]``` Topic is publish distance between 4-8 inch
 ```/left_collision_distance [Float8]``` Topic is publish distance between 4-8 inch
  ```/ground_floor [Boolean]``` Topic is publish if detect ground floor True else False


##  AS5600 Motor Encoder
<img style="width:40%; margin-left:auto; margin-right:auto; display:block" src="https://ae01.alicdn.com/kf/H50439b1bc6a9428e9af7024ce3474465P/AS5600-manyetik-kodlay-c-manyetik-nd-ksiyon-a-s-l-m-sens-r-mod-l-12bit.jpg_Q90.jpg_.webp"/>
<a href="https://tr.aliexpress.com/item/4001145068547.html?spm=a2g0o.productlist.main.3.5ef93747hGhVQf&algo_pvid=e088815a-848d-4625-a702-3fa0a540f93d&aem_p4p_detail=202303010340167927039469412100004309933&algo_exp_id=e088815a-848d-4625-a702-3fa0a540f93d-1&pdp_ext_f=%7B%22sku_id%22%3A%2210000014887911007%22%7D&pdp_npi=3%40dis%21TRY%2124.04%2122.84%21%21%21%21%21%402100b88516776708168128835d06c2%2110000014887911007%21sea%21TR%21800775013&curPageLogUid=hrZCnCXrbPlG&ad_pvid=202303010340167927039469412100004309933_2&ad_pvid=202303010340167927039469412100004309933_2">

AS5600 Encoder</a> sensor works with i2c connection and can share position and speed information of wheels with 4096 pulse in 1 turn.Cloudy robot uses step count of stepper motors instead of encoder by default, but supports this sensor for improvements.

## MPU6050 IMU Sensor 

<img style="width:30%; margin-left:auto; margin-right:auto; display:block"  src="https://www.direnc.net/mpu6050-3-axis-gyro-ve-egim-sensoru-mems-ve-egim-sensorleri-china-29093-62-B.jpg"/>

Required Imu for Cloudy positioning system. Imu is directly connected to sbc computer with i2c protocol. It gives us approximate position and angle information by measuring the speed and acceleration of the robot. The mpu6050 imu consists of 6 DOFs and this number is sufficient for a land vehicle with diff drive. The EKF filter receives the imu data and the desired axes of the imun are selected. By default, only yaw axis data is retrieved from the imu.

Launch IMU:

```bash
cd ~/imu && \
. install/setup.bash && \
ros2 launch mpu6050driver mpu6050driver_launch.py
```


