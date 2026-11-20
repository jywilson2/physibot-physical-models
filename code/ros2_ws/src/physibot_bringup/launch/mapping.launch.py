"""Mapping lab: sim + slam_toolbox (requires slam_toolbox in Nav2 image)."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description() -> LaunchDescription:
    use_sim_time = LaunchConfiguration("use_sim_time")

    sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [FindPackageShare("physibot_bringup"), "launch", "sim_diff_drive.launch.py"]
            )
        ),
        launch_arguments={
            "use_sim_time": use_sim_time,
            "publish_laser": "true",
        }.items(),
    )

    slam = Node(
        package="slam_toolbox",
        executable="async_slam_toolbox_node",
        name="slam_toolbox",
        output="screen",
        parameters=[
            PathJoinSubstitution(
                [FindPackageShare("physibot_bringup"), "config", "slam_toolbox_params.yaml"]
            ),
            {"use_sim_time": use_sim_time},
        ],
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument("use_sim_time", default_value="true"),
            LogInfo(
                msg=[
                    "PhysiBot mapping lab: stub laser is for smoke/teaching; ",
                    "adapt Gazebo/Isaac Limo assets for realistic SLAM.",
                ]
            ),
            sim,
            slam,
        ]
    )
