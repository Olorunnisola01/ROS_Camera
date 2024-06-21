import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo
import cv2
from cv_bridge import CvBridge

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.publisher_ = self.create_publisher(Image, 'image_raw', 10)
        self.camera_info_publisher_ = self.create_publisher(CameraInfo, 'camera_info', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Use Video4Linux2 backend

        if not self.cap.isOpened():
            self.get_logger().error('Could not open video device')

        self.camera_info = CameraInfo()
        self.camera_info.header.frame_id = 'camera_frame'
        self.camera_info.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.camera_info.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # You can add more calibration parameters here if you have them

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'camera_frame'
            self.publisher_.publish(msg)
            
            self.camera_info.header.stamp = msg.header.stamp
            self.camera_info_publisher_.publish(self.camera_info)

def main(args=None):
    rclpy.init(args=args)
    camera_node = CameraNode()
    rclpy.spin(camera_node)
    camera_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
