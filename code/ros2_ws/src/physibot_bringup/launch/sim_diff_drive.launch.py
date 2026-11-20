"""Sim diff-drive bringup: description + odometry (+ optional stub laser)."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description() -> LaunchDescription:
    use_sim_time = LaunchConfiguration("use_sim_time")
    publish_laser = LaunchConfiguration("publish_laser")
    wheel_separation = LaunchConfiguration("wheel_separation")
    wheel_radius = LaunchConfiguration("wheel_radius")
    odom_noise_std = LaunchConfiguration("odom_noise_std")

    description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [FindPackageShare("physibot_bringup"), "launch", "description.launch.py"]
            )
        ),
        launch_arguments={"use_sim_time": use_sim_time}.items(),
    )

    odom = Node(
        package="physibot_sim",
        executable="diff_drive_odom",
        name="diff_drive_odom",
        output="screen",
        parameters=[
            {
                "use_sim_time": use_sim_time,
                "wheel_separation": wheel_separation,
                "wheel_radius": wheel_radius,
                "odom_noise_std": odom_noise_std,
            }
        ],
    )

    laser = Node(
        package="physibot_sim",
        executable="stub_laser",
        name="stub_laser",
        output="screen",
        condition=IfCondition(publish_laser),
        parameters=[{"use_sim_time": use_sim_time}],
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument("use_sim_time", default_value="true"),
            DeclareLaunchArgument("publish_laser", default_value="true"),
            DeclareLaunchArgument("wheel_separation", default_value="0.175"),
            DeclareLaunchArgument("wheel_radius", default_value="0.04"),
            DeclareLaunchArgument("odom_noise_std", default_value="0.0"),
            description,
            odom,
            laser,
        ]
    )
