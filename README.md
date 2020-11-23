# yak_ros2

[![GitHub Actions status](https://github.com/ros-industrial/yak_ros2/workflows/CI/badge.svg?branch=master)](https://github.com/ros-industrial/yak_ros2/actions)
[![GitHub issues open](https://img.shields.io/github/issues/ros-industrial/yak_ros2.svg?)](https://github.com/ros-industrial/yak_ros2/issues)
[![license - Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![support level: consortium / vendor](https://img.shields.io/badge/support%20level-consortium%20/%20vendor-brightgreen.svg)](http://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform)

Example ROS 2 frontend node for the Yak TSDF package

## Usage

The yak_ros2 node provides 3 services and is a subscriber to a topic, which can be used to interact with it.


#### Topics

1. `/input_depth_image`: Listener for published depth images.


#### Services

1. `/generate_mesh`: Used to generate the output mesh to the provided path.
2. `/yak_node/describe_parameters`
3. `/yak_node/get_parameter_types`
4. `/yak_node/get_parameters`
5. `/yak_node/list_parameters`
6. `/yak_node/set_parameters`
7. `/yak_node/set_parameters_atomically`
    read and set the TSDF Volume Parameters.