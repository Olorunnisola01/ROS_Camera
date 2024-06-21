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
- cv_bridge package


## Node Details

- **Node Name**: `camera_node`
- **Published Topics**:
  - `image_raw` (`sensor_msgs/Image`): Publishes the live video stream.
  - `camera_info` (`sensor_msgs/CameraInfo`): Publishes camera information including frame ID and image dimensions.

## Customization

You can customize the node by modifying the source code or the launch file. For instance, you can change the video device index, frame rate, and other camera properties by editing the corresponding parameters in the code.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


---

Feel free to modify the above template to better fit your specific requirements and preferences.
