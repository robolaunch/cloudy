#include <micro_ros_arduino.h>
#include <stdio.h>
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include "FastAccelStepper.h"
#include <std_msgs/msg/float32.h>
#include <std_msgs/msg/int8.h>
#include <std_msgs/msg/int32.h>
#include <IBusBM.h>
//for oled screen
#include "SPI.h"              
#include "Wire.h"              
#include "Adafruit_SSD1306.h" 
#include <Fonts/FreeSerif9pt7b.h>
int width = 128; 
int height = 64; 
int address = 0x3C; 
Adafruit_SSD1306 screen(width, height, &Wire);  

//include sensors libraries
#include <Adafruit_INA219.h>
#include <Arduino_APDS9960.h>
Adafruit_INA219 ina219;

//Task definition for remote controller
TaskHandle_t FlyskyTask;
TaskHandle_t ScreenTask;

// Controller arm
bool arm_check = false;
IBusBM IBus;

//define neopixel led library and arguments
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif
#define PIN 26
Adafruit_NeoPixel pixels(32, PIN, NEO_GRB + NEO_KHZ800);

//Create Subscribers and publishers.
rcl_subscription_t r_subscriber;
rcl_subscription_t l_subscriber;
rcl_subscription_t led_subscriber;
rcl_publisher_t voltage_pub;
rcl_publisher_t bottom_sensor;
rcl_publisher_t distance_left_pub;
rcl_publisher_t distance_right_pub;

//Message types for subscription.
std_msgs__msg__Float32 l_msg;
std_msgs__msg__Float32 r_msg;
std_msgs__msg__Int8 led_msg;
std_msgs__msg__Float32 msg_voltage;
std_msgs__msg__Int32 msg_bottom;
std_msgs__msg__Int32 msg_left;
std_msgs__msg__Int32 msg_right;

//Create timer for only publishers
rcl_timer_t timer_voltage;
rcl_timer_t timer_bottom_sensor;
rcl_timer_t timer_distance_left;
rcl_timer_t timer_distance_right;

//micro-ros 
rclc_executor_t executor;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;


//Error handling for micro-ros
#define RCCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){error_loop();}}
#define RCSOFTCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){}}

// Motor Connections for left stepper
#define dirPinLeftStepper 14
//#define enablePinLeftStepper 12
#define stepPinLeftStepper 17

// Motor Connections for right stepper
#define dirPinRightStepper 27
//#define enablePinRightStepper 12
#define stepPinRightStepper 25

//This changes according to total step size for 1 turn of the stepper.
//Current configuration: 3200 step for 1 complete turn. 1 turn is 2*PI radians.
//radiantToStep: 3200/(2*PI)
#define radianToStep 509.2 

//Initialization for step motor library
FastAccelStepperEngine engine = FastAccelStepperEngine();
FastAccelStepper *leftStepper = NULL; 
FastAccelStepper *rightStepper = NULL; 

//For error handling
void error_loop(){
  while(1){
    delay(100);
  }
}

void TCA9548A(uint8_t bus){
  Wire.beginTransmission(0x70);  // TCA9548A address
  Wire.write(1 << bus);          // send byte to select bus
  Wire.endTransmission();
}

//Callback function for left motor
void subscription_callback_left_motor(const void * msgin)
{  
  if(!arm_check){
  //Unpack incoming message
  const std_msgs__msg__Float32 * msg = (const std_msgs__msg__Float32 *)msgin;
  
  //Calculate the speed 
  uint32_t speed = (uint32_t)(fabs(msg->data)*radianToStep);
  
  //Update the desired speed
  leftStepper->setSpeedInHz(speed);
  
  //Apply the change
  if(msg->data == 0){
    leftStepper->stopMove(); //Stop
  }
  else if(msg->data < 0){
    leftStepper->runBackward(); //For negative values run backwards
  }
  else{
    leftStepper->runForward(); //For positive values run forwards
  }}
  
  

}

//Callback function for right motor.
void subscription_callback_right_motor(const void * msgin)
{  
  if(!arm_check){
  //Unpack incoming message
  const std_msgs__msg__Float32 * msg = (const std_msgs__msg__Float32 *)msgin;

  //Calculate the speed 
  uint32_t speed = (uint32_t)(fabs(msg->data)*radianToStep);

  //Update the desired speed
  rightStepper->setSpeedInHz(speed);

  //Apply the change
  if(msg->data == 0){
    rightStepper->stopMove(); //Stop
  }
  else if(msg->data<0){
    rightStepper->runBackward(); //For negative values run backwards
  }
  else{
    rightStepper->runForward(); //For positive values run forwards
  }
  }
  

} 
//Callback function for neopixel led.
int j;
void headlight() {
  for (int i = 7; i >= 0; i--) {
    pixels.setPixelColor(i, pixels.Color(200, 0, 100));
    j = 15 - i;
    pixels.setPixelColor(j, pixels.Color(200, 0, 100));
    j = 23 - i;
    pixels.setPixelColor(j, pixels.Color(200, 200, 200));
    j = i + 24;
    pixels.setPixelColor(j, pixels.Color(200, 200, 200));
    pixels.show();
  }
}
void emergency() {
  pixels.clear();  // Set all pixel colors to 'off'
  for (int i = 7; i >= 0; i--) {
    pixels.setPixelColor(i, pixels.Color(255, 69, 0));
    j = 15 - i;
    pixels.setPixelColor(j, pixels.Color(255, 69, 0));
    j = 23 - i;
    pixels.setPixelColor(j, pixels.Color(255, 69, 0));
    j = i + 24;
    pixels.setPixelColor(j, pixels.Color(255, 69, 0));
    pixels.show();
  }
  for (int i = 7; i >= 0; i--) {
    pixels.setPixelColor(i, pixels.Color(0, 0, 0));
    j = 15 - i;
    pixels.setPixelColor(j, pixels.Color(0, 0, 0));
    j = 23 - i;
    pixels.setPixelColor(j, pixels.Color(0, 0, 0));
    j = i + 24;
    pixels.setPixelColor(j, pixels.Color(0, 0, 0));
    pixels.show();
  }
}
void right_signal() {
  pixels.clear();  // Set all pixel colors to 'off'
  for (int i = 7; i >= 0; i--) {
    pixels.setPixelColor(i, pixels.Color(255, 69, 0));
    ;

    j = i + 24;
    pixels.setPixelColor(j, pixels.Color(255, 69, 0));
    pixels.show();
  }
  for (int i = 7; i >= 0; i--) {
    pixels.setPixelColor(i, pixels.Color(0, 0, 0));

    j = i + 24;
    pixels.setPixelColor(j, pixels.Color(0, 0, 0));
    pixels.show();
  }
}
void left_signal() {
  pixels.clear();  // Set all pixel colors to 'off'
  for (int i = 7; i >= 0; i--) {
    j = 15 - i;
    pixels.setPixelColor(j, pixels.Color(255, 69, 0));
    j = 23 - i;
    pixels.setPixelColor(j, pixels.Color(255, 69, 0));
    pixels.show();
  }
  for (int i = 7; i >= 0; i--) {
    j = 15 - i;
    pixels.setPixelColor(j, pixels.Color(0, 0, 0));
    j = 23 - i;
    pixels.setPixelColor(j, pixels.Color(0, 0, 0));
    pixels.show();
  }
}

void subscription_callback_led(const void * msgin)
{  
const std_msgs__msg__Int8 *msg = (const std_msgs__msg__Int8 *)msgin;
  int demand_led = msg->data;
  switch (demand_led){
    case 1:
      headlight();
      break;
    case 2:
      emergency();
      break;

    case 3:
      left_signal();
      break;

    case 4:
      right_signal();
      break;
  }
} 

void voltage_callback(rcl_timer_t* timer_voltage, int64_t last_call_time) {
  RCLC_UNUSED(last_call_time);
  if (timer_voltage != NULL) {
    TCA9548A(5);
    float busvoltage = 0;
    busvoltage = ina219.getBusVoltage_V();
    msg_voltage.data = busvoltage;
    RCSOFTCHECK(rcl_publish(&voltage_pub, &msg_voltage, NULL));
  }
}

void bottom_sensor_callback(rcl_timer_t* timer_bottom_sensor, int64_t last_call_time) {
  RCLC_UNUSED(last_call_time);
  if (timer_bottom_sensor != NULL) {
    TCA9548A(4);
    if (APDS.proximityAvailable()) {
      int proximity = APDS.readProximity();

      msg_bottom.data = proximity;
      RCSOFTCHECK(rcl_publish(&bottom_sensor, &msg_bottom, NULL));
    }
  }
}

void left_distance_callback(rcl_timer_t* timer_distance_left, int64_t last_call_time) {
  RCLC_UNUSED(last_call_time);
  if (timer_distance_left != NULL) {
    TCA9548A(3);
    if (APDS.proximityAvailable()) {
      int proximity = APDS.readProximity();

      msg_left.data = proximity;
      RCSOFTCHECK(rcl_publish(&distance_left_pub, &msg_left, NULL));
    }
  }
}

void right_distance_callback(rcl_timer_t* timer_distance_right, int64_t last_call_time) {
  RCLC_UNUSED(last_call_time);
  if (timer_distance_right != NULL) {
    TCA9548A(2);
    if (APDS.proximityAvailable()) {
      int proximity = APDS.readProximity();

      msg_right.data = proximity;
      RCSOFTCHECK(rcl_publish(&distance_right_pub, &msg_right, NULL));
    }
  }
}

void write_text(float percent, String status) {
  screen.clearDisplay();
  screen.setTextSize(1);  // Yazı boyutu
  screen.setTextColor(SSD1306_WHITE);
  screen.setFont(&FreeSerif9pt7b);
  screen.setCursor(20, 15); 
  screen.print("robolaunch");
  screen.setFont();
  screen.setCursor(10, 30);
  screen.print("Battery  :  V ");
  screen.println(percent);
  screen.setCursor(10, 40);
  screen.print("Status   :  ");
  screen.println(status);
  screen.display();
}
void applyMotorSpeeds(FastAccelStepper * leftStepper,FastAccelStepper * rightStepper, float demand_l_speed, float demand_r_speed){

  leftStepper->setSpeedInHz((uint32_t) (fabs(demand_l_speed) * radianToStep));
  rightStepper->setSpeedInHz((uint32_t) (fabs(demand_r_speed) * radianToStep));


  //Apply the change to left motor
  if(demand_l_speed == 0){
    leftStepper->stopMove(); //Stop
  }
  else if(demand_l_speed < 0){
    leftStepper->runBackward(); //For negative values run backwards
  }
  else{
    leftStepper->runForward(); //For positive values run forwards
  }

  //Apply the change to right motor
  if(demand_r_speed == 0){
    rightStepper->stopMove(); //Stop
  }
  else if(demand_r_speed < 0){
    rightStepper->runBackward(); //For negative values run backwards
  }
  else{
    rightStepper->runForward(); //For positive values run forwards
  }


}

//Calculates speeds for each motor using diffdrive kinematics
void calculateMotorSpeeds(int steering, int driving, float* demand_l_speed, float* demand_r_speed){
  int demand_x = map(steering,2000,1000,-23,23);    
  int demand_z = map(driving,1000,2000,-20,20);

  *demand_l_speed= demand_x - (demand_z*0.255);
  *demand_r_speed= demand_x + (demand_z*0.255);

}
void FlySkyCode( void * pvParameters ){
  while(true){
    
  int arm=IBus.readChannel(7);
  if(arm>1500){
    digitalWrite(2, HIGH);  // turn the LED on (HIGH is the voltage level)
    //Control wheel
    arm_check = true;
    
    int steering = IBus.readChannel(1); // get latest value for servo channel 1
    int driving = IBus.readChannel(3); // get latest value for servo channel 3

    float demand_l_speed = 0.0;
    float demand_r_speed = 0.0;

    float* demand_l_speed_p = &demand_l_speed;
    float* demand_r_speed_p = &demand_r_speed;

    calculateMotorSpeeds(steering, driving, demand_l_speed_p, demand_r_speed_p);
    applyMotorSpeeds(leftStepper,rightStepper,*demand_l_speed_p,*demand_r_speed_p);

    
    delay(100);

  }
  else{
    digitalWrite(2, LOW);   // turn the LED off by making the voltage LOW
    arm_check = false;
    delay(1000);
    
  }
  
  }
}
void screenCode( void * pvParameters){
  int i = 0;
  const TickType_t xDelay = 500;
  float busvoltage = 0;
  while(true){
    TCA9548A(5);
    vTaskDelay( xDelay );
    busvoltage = ina219.getBusVoltage_V();
    i++;
    TCA9548A(1);
    write_text(busvoltage,"Ready");

  }
}
bool led_first_open = false;
void setup() {
  
  //Mulitplexer Sensors Setup

  TCA9548A(5);
  ina219.begin();

  TCA9548A(4);
  APDS.begin();

  TCA9548A(3);
  APDS.begin();

  TCA9548A(2);
  APDS.begin();

  TCA9548A(1);
  screen.begin(SSD1306_SWITCHCAPVCC, address); 

//Open the led when plug battery
  if (led_first_open==false){
  headlight();
  led_first_open= true;
  }

  //neopixel led initialize
  #if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
  #endif

  pixels.begin();
  //Initialize step motor engine
  engine.init();
  pinMode(2, OUTPUT);
  IBus.begin(Serial2, 0);
  
  xTaskCreatePinnedToCore(
                    FlySkyCode,   /* Task function. */
                    "FlySky",     /* name of task. */
                    10000,       /* Stack size of task */
                    NULL,        /* parameter of the task */
                    1,           /* priority of the task */
                    &FlyskyTask,      /* Task handle to keep track of created task */
                    0);          /* pin task to core 0 */
  xTaskCreatePinnedToCore(
                    screenCode,   /* Task function. */
                    "Screen",     /* name of task. */
                    10000,       /* Stack size of task */
                    NULL,        /* parameter of the task */
                    2,           /* priority of the task */
                    &ScreenTask,      /* Task handle to keep track of created task */
                    0);  
  delay(500); 
  //Configure step pinss
  leftStepper = engine.stepperConnectToPin(stepPinLeftStepper);
  rightStepper = engine.stepperConnectToPin(stepPinRightStepper);

  //Initialize direction pin, enable pin and set acceleration
  if (leftStepper) {
    leftStepper->setDirectionPin(dirPinLeftStepper);
    //leftStepper->setEnablePin(enablePinLeftStepper);
    leftStepper->setAutoEnable(true);
    leftStepper->setAcceleration(16000);
  }

  if(rightStepper){
    rightStepper->setDirectionPin(dirPinRightStepper);
    //rightStepper->setEnablePin(enablePinRightStepper);
    rightStepper->setAutoEnable(true);
    rightStepper->setAcceleration(16000);
  }

  set_microros_transports();
  delay(2000);
  allocator = rcl_get_default_allocator();

  //Create init_options
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  //Create node
  RCCHECK(rclc_node_init_default(&node, "micro_ros_arduino_node", "", &support));
  
  //Create subscribers
  RCCHECK(rclc_subscription_init_default(
    &l_subscriber,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32),
    "left_motor_speed"));
  RCCHECK(rclc_subscription_init_default(
    &r_subscriber,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32),
    "right_motor_speed")); 
  RCCHECK(rclc_subscription_init_default(
    &led_subscriber,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Int8),
    "neopixel_led")); 

  //Create Publishers
  RCCHECK(rclc_publisher_init_default(
    &voltage_pub,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Float32),
    "voltage"));

  RCCHECK(rclc_publisher_init_default(
    &bottom_sensor,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Int32),
    "bottom_sensor"));

  RCCHECK(rclc_publisher_init_default(
    &distance_left_pub,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Int32),
    "left_sensor_distance"));

  RCCHECK(rclc_publisher_init_default(
    &distance_right_pub,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Int32),
    "right_sensor_distance"));

  // Create Timer for Only Publisher*********************************
  RCCHECK(rclc_timer_init_default(
    &timer_voltage,
    &support,
    RCL_MS_TO_NS(1000),
    voltage_callback));

  RCCHECK(rclc_timer_init_default(
    &timer_bottom_sensor,
    &support,
    RCL_MS_TO_NS(100),
    bottom_sensor_callback));

  RCCHECK(rclc_timer_init_default(
    &timer_distance_left,
    &support,
    RCL_MS_TO_NS(100),
    left_distance_callback));

  RCCHECK(rclc_timer_init_default(
    &timer_distance_right,
    &support,
    RCL_MS_TO_NS(100),
    right_distance_callback));

  //Init executor
  RCCHECK(rclc_executor_init(&executor, &support.context, 7, &allocator));
  //Init subscriptions  
  RCCHECK(rclc_executor_add_subscription(&executor, &l_subscriber, &l_msg, &subscription_callback_left_motor, ON_NEW_DATA));
  RCCHECK(rclc_executor_add_subscription(&executor, &r_subscriber, &r_msg, &subscription_callback_right_motor, ON_NEW_DATA));
  RCCHECK(rclc_executor_add_subscription(&executor, &led_subscriber, &led_msg, &subscription_callback_led, ON_NEW_DATA));
  RCCHECK(rclc_executor_add_timer(&executor, &timer_voltage));
  RCCHECK(rclc_executor_add_timer(&executor, &timer_bottom_sensor));
  RCCHECK(rclc_executor_add_timer(&executor, &timer_distance_left));
  RCCHECK(rclc_executor_add_timer(&executor, &timer_distance_right));

}

void loop() {
  //micro-ros spin
  rclc_executor_spin(&executor);
  
  }