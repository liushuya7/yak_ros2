cmake_minimum_required(VERSION 3.5.0)
project(yak_ros2_msgs)

find_package(ament_cmake REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(yak_ros2_msgs
  "msg/KinFuParams.msg"
  "srv/GenerateMesh.srv"
  "srv/UpdateKinFuParams.srv"
  DEPENDENCIES
  builtin_interfaces
  geometry_msgs
  std_msgs
  )

ament_export_dependencies(rosidl_default_runtime)
ament_package()
