"""Nav2 navigation lab bringup (requires Nav2 + slam/map)."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description() -> LaunchDescription:
    use_sim_time = LaunchConfiguration("use_sim_time")
    map_yaml = LaunchConfiguration("map")
    params_file = LaunchConfiguration("params_file")

    default_map = PathJoinSubstitution(
        [FindPackageShare("physibot_bringup"), "maps", "demo_map.yaml"]
    )
    default_params = PathJoinSubstitution(
        [FindPackageShare("physibot_bringup"), "config", "nav2_params.yaml"]
    )

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

    # Official Nav2 bringup with course params + demo map
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [FindPackageShare("nav2_bringup"), "launch", "bringup_launch.py"]
            )
        ),
        launch_arguments={
            "use_sim_time": use_sim_time,
            "map": map_yaml,
            "params_file": params_file,
            "autostart": "true",
        }.items(),
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument("use_sim_time", default_value="true"),
            DeclareLaunchArgument("map", default_value=default_map),
            DeclareLaunchArgument("params_file", default_value=default_params),
            LogInfo(msg=["PhysiBot Nav2 lab — params=", params_file]),
            sim,
            nav2,
        ]
    )
