import subprocess
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # turtlesim node'u başlat
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'ros2', 'run', 'turtlesim', 'turtlesim_node'],
            name='turtlesim_node',
            output='screen'
        ),
        # shapes node'u başlatmak için subprocess kullanıyoruz
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'python3', '/home/yahya/ros2_ws/src/shapes/shapes/shapes.py'],
            name='shapes_node',
            output='screen'
        ),
        # py_srvcli server node'unu Python ile başlatmak için subprocess kullanıyoruz
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'python3', '/home/yahya/ros2_ws/src/py_srvcli/py_srvcli/server.py'],
            name='service_node',
            output='screen'
        ),
        # py_srvcli client node'unu Python ile başlatmak için subprocess kullanıyoruz
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'python3', '/home/yahya/ros2_ws/src/py_srvcli/py_srvcli/client.py'],
            name='client_node',
            output='screen'
        ),
        # my_pub_sub publisher node'unu Python ile başlatmak için subprocess kullanıyoruz
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'python3', '/home/yahya/ros2_ws/src/my_pub_sub/my_pub_sub/publisher_node.py'],
            name='publisher_node',
            output='screen'
        ),
        # my_pub_sub subscriber node'unu Python ile başlatmak için subprocess kullanıyoruz
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'python3', '/home/yahya/ros2_ws/src/my_pub_sub/my_pub_sub/subscriber_node.py'],
            name='subscriber_node',
            output='screen'
        ),
    ])
