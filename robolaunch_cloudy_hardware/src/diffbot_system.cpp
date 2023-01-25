#include "robolaunch_cloudy_hardware/diffbot_system.hpp"

#include <chrono>
#include <cmath>
#include <limits>
#include <memory>
#include <vector>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "hardware_interface/types/hardware_interface_type_values.hpp"

//#include <rclcpp_components/register_node_macro.hpp>

namespace robolaunch_cloudy_hardware
{
  HardwareCommandPub::HardwareCommandPub() : Node("hardware_command_publisher")
{
  publisher_l = this->create_publisher<std_msgs::msg::Float32>("left_motor_speed", 1);
  publisher_r = this->create_publisher<std_msgs::msg::Float32>("right_motor_speed", 1);
}

void HardwareCommandPub::publishData(float left_motor_speed, float right_motor_speed)
{
  std_msgs::msg::Float32 msg;

  msg.data = left_motor_speed;
  publisher_l->publish(msg);
  
  msg.data = right_motor_speed;
  publisher_r->publish(msg);

}

CallbackReturn DiffBotSystemHardware::on_init(
  const hardware_interface::HardwareInfo & info)
{
  base_x_ = 0.0;
  base_y_ = 0.0;
  base_theta_ = 0.0;
  hw_cmd_pub_ = std::make_shared<HardwareCommandPub>();

  if (hardware_interface::SystemInterface::on_init(info) != CallbackReturn::SUCCESS)
{
  return CallbackReturn::ERROR;
}

  hw_start_sec_ = stod(info_.hardware_parameters["example_param_hw_start_duration_sec"]);
  hw_stop_sec_ = stod(info_.hardware_parameters["example_param_hw_stop_duration_sec"]);
  hw_positions_.resize(info_.joints.size(), std::numeric_limits<double>::quiet_NaN());
  hw_velocities_.resize(info_.joints.size(), std::numeric_limits<double>::quiet_NaN());
  hw_commands_.resize(info_.joints.size(), std::numeric_limits<double>::quiet_NaN());

  for (const hardware_interface::ComponentInfo & joint : info_.joints)
  {
    // DiffBotSystem has exactly two states and one command interface on each joint
    if (joint.command_interfaces.size() != 1)
    {
      RCLCPP_FATAL(
        rclcpp::get_logger("DiffBotSystemHardware"),
        "Joint '%s' has %lu command interfaces found. 1 expected.", joint.name.c_str(),
        joint.command_interfaces.size());
      return CallbackReturn::ERROR;
    }

    if (joint.command_interfaces[0].name != hardware_interface::HW_IF_VELOCITY)
    {
      RCLCPP_FATAL(
        rclcpp::get_logger("DiffBotSystemHardware"),
        "Joint '%s' have %s command interfaces found. '%s' expected.", joint.name.c_str(),
        joint.command_interfaces[0].name.c_str(), hardware_interface::HW_IF_VELOCITY);
      return CallbackReturn::ERROR;
    }

    if (joint.state_interfaces.size() != 2)
    {
      RCLCPP_FATAL(
        rclcpp::get_logger("DiffBotSystemHardware"),
        "Joint '%s' has %lu state interface. 2 expected.", joint.name.c_str(),
        joint.state_interfaces.size());
      return CallbackReturn::ERROR;
    }

    if (joint.state_interfaces[0].name != hardware_interface::HW_IF_POSITION)
    {
      RCLCPP_FATAL(
        rclcpp::get_logger("DiffBotSystemHardware"),
        "Joint '%s' have '%s' as first state interface. '%s'expected.",
        joint.name.c_str(), joint.state_interfaces[0].name.c_str(),
        hardware_interface::HW_IF_POSITION);
      return CallbackReturn::ERROR;
    }

    if (joint.state_interfaces[1].name != hardware_interface::HW_IF_VELOCITY)
    {
      RCLCPP_FATAL(
        rclcpp::get_logger("DiffBotSystemHardware"),
        "Joint '%s' have '%s' as second state interface. '%s' expected.", joint.name.c_str(),
        joint.state_interfaces[1].name.c_str(), hardware_interface::HW_IF_VELOCITY);
      return CallbackReturn::ERROR;
    }
  }

return CallbackReturn::SUCCESS;
}

std::vector<hardware_interface::StateInterface> DiffBotSystemHardware::export_state_interfaces()
{
  std::vector<hardware_interface::StateInterface> state_interfaces;
  for (auto i = 0u; i < info_.joints.size(); i++)
  {
    state_interfaces.emplace_back(hardware_interface::StateInterface(
      info_.joints[i].name, hardware_interface::HW_IF_POSITION, &hw_positions_[i]));
    state_interfaces.emplace_back(hardware_interface::StateInterface(
      info_.joints[i].name, hardware_interface::HW_IF_VELOCITY, &hw_velocities_[i]));
  }

  return state_interfaces;
}

std::vector<hardware_interface::CommandInterface> DiffBotSystemHardware::export_command_interfaces()
{
  std::vector<hardware_interface::CommandInterface> command_interfaces;
  for (auto i = 0u; i < info_.joints.size(); i++)
  {
    command_interfaces.emplace_back(hardware_interface::CommandInterface(
      info_.joints[i].name, hardware_interface::HW_IF_VELOCITY, &hw_commands_[i]));
  }

  return command_interfaces;
}

CallbackReturn DiffBotSystemHardware::on_activate(const rclcpp_lifecycle::State &)
{
  RCLCPP_INFO(rclcpp::get_logger("DiffBotSystemHardware"), "Starting ...please wait...");

  for (auto i = 0; i <= hw_start_sec_; i++)
  {
    rclcpp::sleep_for(std::chrono::seconds(1));
    RCLCPP_INFO(
      rclcpp::get_logger("DiffBotSystemHardware"), "%.1f seconds left...", hw_start_sec_ - i);
  }

  // set some default values
  for (auto i = 0u; i < hw_positions_.size(); i++)
  {
    if (std::isnan(hw_positions_[i]))
    {
      hw_positions_[i] = 0;
      hw_velocities_[i] = 0;
      hw_commands_[i] = 0;
    }
  }


  RCLCPP_INFO(rclcpp::get_logger("DiffBotSystemHardware"), "System Successfully started!");

  return CallbackReturn::SUCCESS;
}

CallbackReturn DiffBotSystemHardware::on_deactivate(const rclcpp_lifecycle::State &)
{
  RCLCPP_INFO(rclcpp::get_logger("DiffBotSystemHardware"), "Stopping ...please wait...");

  for (auto i = 0; i <= hw_stop_sec_; i++)
  {
    rclcpp::sleep_for(std::chrono::seconds(1));
    RCLCPP_INFO(
      rclcpp::get_logger("DiffBotSystemHardware"), "%.1f seconds left...", hw_stop_sec_ - i);
  }


  RCLCPP_INFO(rclcpp::get_logger("DiffBotSystemHardware"), "System successfully stopped!");

  return CallbackReturn::SUCCESS;
}

hardware_interface::return_type DiffBotSystemHardware::read(const rclcpp::Time& time, const rclcpp::Duration& duration)
{
  RCLCPP_INFO(rclcpp::get_logger("DiffBotSystemHardware"), "Reading...");

  double radius = 0.0315;  // radius of the wheels
  double dist_w = 0.215;   // distance between the wheels
  double dt = duration.seconds();      // Control period
  
  
  for (uint i = 0; i < hw_commands_.size(); i++)
  {
    // Simulate DiffBot wheels's movement as a first-order system
    // Update the joint status: this is a revolute joint without any limit.
    // Simply integrates
    hw_positions_[i] = hw_positions_[i] + dt * hw_commands_[i] ;
    hw_velocities_[i] = hw_commands_[i];
    
    RCLCPP_INFO(
      rclcpp::get_logger("DiffBotSystemHardware"),
      "Got position state %.5f and velocity state %.5f for '%s'!", hw_positions_[i],
      hw_velocities_[i], info_.joints[i].name.c_str());
  }

  // Update the free-flyer, i.e. the base notation using the classical
  // wheel differentiable kinematics
  double base_dx = 0.5 * radius * (hw_commands_[0] + hw_commands_[1]) * cos(base_theta_);
  double base_dy = 0.5 * radius * (hw_commands_[0] + hw_commands_[1]) * sin(base_theta_);
  double base_dtheta = radius * (hw_commands_[0] - hw_commands_[1]) / dist_w;
  base_x_ += base_dx * dt;
  base_y_ += base_dy * dt;
  base_theta_ += base_dtheta * dt;

  RCLCPP_INFO(
    rclcpp::get_logger("DiffBotSystemHardware"), "Joints successfully read! (%.5f,%.5f,%.5f)",
    base_x_, base_y_, base_theta_);

  return hardware_interface::return_type::OK;
}

hardware_interface::return_type robolaunch_cloudy_hardware::DiffBotSystemHardware::write(const rclcpp::Time&, const rclcpp::Duration&)
{
  RCLCPP_INFO(rclcpp::get_logger("DiffBotSystemHardware"), "Writing...");
    //publish to topic

  for (auto i = 0u; i < hw_commands_.size(); i++)
  {
    // Simulate sending commands to the hardware
    RCLCPP_INFO(
      rclcpp::get_logger("DiffBotSystemHardware"), "Got command %.5f for '%s'!", hw_commands_[i],
      info_.joints[i].name.c_str());
  }
  hw_cmd_pub_->publishData(hw_commands_[0],hw_commands_[1]);
  RCLCPP_INFO(rclcpp::get_logger("DiffBotSystemHardware"), "Joints successfully written!");
  return hardware_interface::return_type::OK;
}

}  // namespace robolaunch_cloudy_hardware

#include "pluginlib/class_list_macros.hpp"
PLUGINLIB_EXPORT_CLASS(
  robolaunch_cloudy_hardware::DiffBotSystemHardware, hardware_interface::SystemInterface)