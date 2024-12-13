#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from water_control.srv import WaterControl

class WaterControlNode(Node):
    def __init__(self):
        super().__init__('water_control_node')
        
        self.create_service(
            WaterControl,
            'robot_stop',
            self.handle_robot_stop
        )
        self.create_service(
            WaterControl,
            'start_water',
            self.handle_start_water
        )
        self.create_service(
            WaterControl,
            'check_water_status',
            self.handle_check_status
        )
        self.create_service(
            WaterControl,
            'finish_water',
            self.handle_finish_water
        )

    def handle_robot_stop(self, request, response):
        response.success = True
        response.message = "Robot stopped"
        return response

    def handle_start_water(self, request, response):
        response.success = True
        response.message = "Water started"
        return response

    def handle_check_status(self, request, response):
        response.success = True
        response.message = "Water running completed"
        return response

    def handle_finish_water(self, request, response):
        response.success = True
        response.message = "Process finished"
        return response

def main():
    rclpy.init()
    node = WaterControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()