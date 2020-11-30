from launch import LaunchDescription
import launch_ros.actions

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription([
        # Core node for GPU-accelerated 3D reconstruction
        launch_ros.actions.Node(
            name='yak_ros2_node', package='yak_ros2', executable='yak_ros2_node', output='screen',
            remappings=[('input_depth_image', '/camera1/depth/image_rect_raw')],
            parameters=[{
                         'tsdf_frame_id': 'iiwa_base',
                         'camera_intrinsic_params':
                           {
                             'fx': 550.0,
                             'fy': 550.0,
                             'cx': 320.0,
                             'cy': 240.0,
                           },
                         'cols': 640,
                         'rows': 480,
                         'volume_resolution': 0.001,
                         'volume_x': 640,
                         'volume_y': 640,
                         'volume_z': 192,
                         }]
            ),
    ])
    return ld
