#include <micro_ros_arduino.h>
#include <stdio.h>
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include "FastAccelStepper.h"
#include <std_msgs/msg/float32.h>
#include <IBusBM.h>


//Task definition for remote controller
TaskHandle_t FlyskyTask;

// Controller arm
bool arm_check = false;
IBusBM IBus;


//Subscribers for left and right motor.
rcl_subscription_t r_subscriber;
rcl_subscription_t l_subscriber;

//Message types for subscription. The unit is Radian per Second.
std_msgs__msg__Float32 l_msg;
std_msgs__msg__Float32 r_msg;

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
#define enablePinLeftStepper 27
#define stepPinLeftStepper 17

// Motor Connections for right stepper
#define dirPinRightStepper 27
#define enablePinRightStepper 26
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

  *demand_l_speed= demand_x - (demand_z*0.17);
  *demand_r_speed= demand_x + (demand_z*0.17);

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

void setup() {
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
  delay(500); 
  //Configure step pinss
  leftStepper = engine.stepperConnectToPin(stepPinLeftStepper);
  rightStepper = engine.stepperConnectToPin(stepPinRightStepper);

  //Initialize direction pin, enable pin and set acceleration
  if (leftStepper) {
    leftStepper->setDirectionPin(dirPinLeftStepper);
    leftStepper->setEnablePin(enablePinLeftStepper);
    leftStepper->setAutoEnable(true);
    leftStepper->setAcceleration(16000);
  }

  if(rightStepper){
    rightStepper->setDirectionPin(dirPinRightStepper);
    rightStepper->setEnablePin(enablePinRightStepper);
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
  //Init executor
  RCCHECK(rclc_executor_init(&executor, &support.context, 2, &allocator));
  //Init subscriptions  
  RCCHECK(rclc_executor_add_subscription(&executor, &l_subscriber, &l_msg, &subscription_callback_left_motor, ON_NEW_DATA));
  RCCHECK(rclc_executor_add_subscription(&executor, &r_subscriber, &r_msg, &subscription_callback_right_motor, ON_NEW_DATA));
  
}

void loop() {
  //micro-ros spin
  rclc_executor_spin(&executor);
  
  }
