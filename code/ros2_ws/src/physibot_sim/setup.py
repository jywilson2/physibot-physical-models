from setuptools import setup

package_name = "physibot_sim"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="PhysiBot contributors",
    maintainer_email="jywilson@ieee.org",
    description="PhysiBot simulation helpers (diff-drive odometry, stub laser).",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "diff_drive_odom = physibot_sim.diff_drive_odom_node:main",
            "stub_laser = physibot_sim.stub_laser_node:main",
        ],
    },
)
