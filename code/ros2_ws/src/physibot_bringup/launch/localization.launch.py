"""Localization lab: sim + map_server + AMCL (requires Nav2 packages)."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description() -> LaunchDescription:
    use_sim_time = LaunchConfiguration("use_sim_time")
    map_yaml = LaunchConfiguration("map")

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

    map_server = Node(
        package="nav2_map_server",
        executable="map_server",
        name="map_server",
        output="screen",
        parameters=[
            {
                "use_sim_time": use_sim_time,
                "yaml_filename": map_yaml,
            }
        ],
    )

    amcl = Node(
        package="nav2_amcl",
        executable="amcl",
        name="amcl",
        output="screen",
        parameters=[
            PathJoinSubstitution(
                [FindPackageShare("physibot_bringup"), "config", "amcl_params.yaml"]
            ),
            {"use_sim_time": use_sim_time},
        ],
    )

    lifecycle = Node(
        package="nav2_lifecycle_manager",
        executable="lifecycle_manager",
        name="lifecycle_manager_localization",
        output="screen",
        parameters=[
            {
                "use_sim_time": use_sim_time,
                "autostart": True,
                "node_names": ["map_server", "amcl"],
            }
        ],
    )

    default_map = PathJoinSubstitution(
        [FindPackageShare("physibot_bringup"), "maps", "demo_map.yaml"]
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument("use_sim_time", default_value="true"),
            DeclareLaunchArgument("map", default_value=default_map),
            LogInfo(msg=["PhysiBot localization lab — map=", map_yaml]),
            sim,
            map_server,
            amcl,
            lifecycle,
        ]
    )
