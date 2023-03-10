#ifndef robolaunch_cloudy_hardware__DIFFBOT_SYSTEM_HPP_
#define robolaunch_cloudy_hardware__DIFFBOT_SYSTEM_HPP_

#include <memory>
#include <string>
#include <vector>

#include "robolaunch_cloudy_hardware/visibility_control.h"

#include "rclcpp_lifecycle/node_interfaces/lifecycle_node_interface.hpp"
#include "rclcpp_lifecycle/state.hpp"
#include "rclcpp/rclcpp.hpp"
#include "rclcpp/time.hpp"
#include "rclcpp/macros.hpp"


#include "hardware_interface/types/hardware_interface_return_values.hpp"
#include "hardware_interface/system_interface.hpp"
#include "hardware_interface/handle.hpp"

#include "std_msgs/msg/float32.hpp"


namespace robolaunch_cloudy_hardware
{
  using CallbackReturn = rclcpp_lifecycle::node_interfaces::LifecycleNodeInterface::CallbackReturn;

  class HardwareCommandPub : public rclcpp::Node  //the node definition for the publisher to talk to micro-ROS agent
{
  public:
    HardwareCommandPub();
    void publishData(float left_motor_speed, float right_motor_speed);

  private:
    rclcpp::Publisher<std_msgs::msg::Float32>::SharedPtr publisher_l;
    rclcpp::Publisher<std_msgs::msg::Float32>::SharedPtr publisher_r;
};


class DiffBotSystemHardware
: public hardware_interface::SystemInterface
{
public:
  RCLCPP_SHARED_PTR_DEFINITIONS(DiffBotSystemHardware);

  robolaunch_cloudy_hardware_PUBLIC
  CallbackReturn on_init(const hardware_interface::HardwareInfo & info) override;

  robolaunch_cloudy_hardware_PUBLIC
  std::vector<hardware_interface::StateInterface> export_state_interfaces() override;

  robolaunch_cloudy_hardware_PUBLIC
  std::vector<hardware_interface::CommandInterface> export_command_interfaces() override;

  robolaunch_cloudy_hardware_PUBLIC
  CallbackReturn on_activate(const rclcpp_lifecycle::State & ) override;

  robolaunch_cloudy_hardware_PUBLIC
  CallbackReturn on_deactivate(const rclcpp_lifecycle::State & ) override;

  robolaunch_cloudy_hardware_PUBLIC
  hardware_interface::return_type read(const rclcpp::Time& time, const rclcpp::Duration& period) override;

  robolaunch_cloudy_hardware_PUBLIC
  hardware_interface::return_type write(const rclcpp::Time& time, const rclcpp::Duration& period) override;

  std::shared_ptr<HardwareCommandPub> hw_cmd_pub_;
private:
  // Parameters for the DiffBot simulation
  double hw_start_sec_;
  double hw_stop_sec_;

  // Store the command for the simulated robot
  std::vector<double> hw_commands_;
  std::vector<double> hw_positions_;
  std::vector<double> hw_velocities_;

  // Store the wheeled robot position
  double base_x_, base_y_, base_theta_;
};

}  // namespace robolaunch_cloudy_hardware

#endif  // robolaunch_cloudy_hardware__DIFFBOT_SYSTEM_HPP_
