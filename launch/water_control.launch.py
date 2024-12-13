from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    water_control_node = Node(
        package='water_control',
        executable='water_control_node',
        name='water_control_node',
        output='screen'
    )

    rosbridge_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('rosbridge_server'),
                        'launch',
                        'rosbridge_websocket_launch.py')
        ),
        launch_arguments={
            'port': '9090',
            'address': '0.0.0.0'
        }.items()
    )

    return LaunchDescription([
        water_control_node,
        rosbridge_launch
    ])