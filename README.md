Certainly! Here is the revised README file with the repository name included:

---

# ROS_Camera

This repository contains a ROS 2 node that captures images from a camera using OpenCV and publishes them as sensor messages. The node also publishes camera information, such as image dimensions and frame IDs, for use in other ROS 2 nodes and applications.

## Features

- Captures images from a video device using OpenCV.
- Publishes images to the `image_raw` topic as `sensor_msgs/Image` messages.
- Publishes camera information to the `camera_info` topic as `sensor_msgs/CameraInfo` messages.
- Configurable through a ROS 2 launch file.

## Dependencies

- ROS 2 Humble
- OpenCV
- `cv_bridge` package

## Installation

1. Clone this repository into your ROS 2 workspace:
    ```bash
    cd ~/ros2_ws/src
    git clone https://github.com/olorunnisola01/ROS_Camera.git
    ```

2. Install dependencies:
    ```bash
    sudo apt update
    sudo apt install ros-humble-cv-bridge
    sudo apt install ros-humble-image-transport
    sudo apt install libopencv-dev
    ```

3. Build the workspace:
    ```bash
    cd ~/ros2_ws
    colcon build
    ```

4. Source the workspace:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```

## Usage

To run the camera node:
```bash
ros2 run camera_node camera_node
```

You can also use a launch file to configure and run the node:
```bash
ros2 launch camera_node camera_node_launch.py
```

## Node Details

- **Node Name**: `camera_node`
- **Published Topics**:
  - `image_raw` (`sensor_msgs/Image`): Publishes the captured images.
  - `camera_info` (`sensor_msgs/CameraInfo`): Publishes camera information including frame ID and image dimensions.

## Customization

You can customize the node by modifying the source code or the launch file. For instance, you can change the video device index, frame rate, and other camera properties by editing the corresponding parameters in the code.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify the above template to better fit your specific requirements and preferences.