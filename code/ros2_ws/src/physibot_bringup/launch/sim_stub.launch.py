"""Minimal PhysiBot sim stub launch — replace with adapted Limo/Gazebo bringup later."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description() -> LaunchDescription:
    use_sim_time = LaunchConfiguration("use_sim_time")
    desc_share = get_package_share_directory("physibot_description")
    urdf_path = os.path.join(desc_share, "urdf", "physibot_stub.urdf.xacro")

    return LaunchDescription(
        [
            DeclareLaunchArgument("use_sim_time", default_value="true"),
            LogInfo(
                msg=[
                    "PhysiBot sim stub: adapt AgileX Limo + Nav2 examples next. ",
                    "URDF=",
                    urdf_path,
                ]
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[
                    {
                        "use_sim_time": use_sim_time,
                        # Placeholder: xacro processing added when description matures
                        "robot_description": "<robot name=\"physibot_stub\"><link name=\"base_link\"/></robot>",
                    }
                ],
            ),
        ]
    )
