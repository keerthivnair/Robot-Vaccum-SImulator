import numpy as np
import cv2
from config import *

class GUI:
    def __init__(self, map_array):
        self.map = map_array
        self.visited = np.zeros_like(map_array, dtype=np.uint8)

    def render(self, robot_pose, laser_values=None):
        # Convert map to grayscale base (0=black for walls, 255=free space)
        base = (1 - self.map) * 255
        img = cv2.cvtColor(base.astype(np.uint8), cv2.COLOR_GRAY2BGR)

        # Robot position and orientation
        x = int(round(robot_pose["x"]))
        y = int(round(robot_pose["y"]))
        yaw = robot_pose["yaw"]

        # Marking visited cells
        if 0 <= y < self.visited.shape[0] and 0 <= x < self.visited.shape[1]:
            self.visited[y, x] = 1

        visited_mask = self.visited > 0
        img[visited_mask] = COLOR_VISITED

        # Draw robot
        cv2.circle(img, (x, y), ROBOT_RADIUS, COLOR_ROBOT, -1)

        # Draw robot's orientation line
        end_x = int(x + ROBOT_RADIUS * 2 * np.cos(yaw))
        end_y = int(y + ROBOT_RADIUS * 2 * np.sin(yaw))
        cv2.line(img, (x, y), (end_x, end_y), (0, 0, 0), 1)

        # Draw laser rays if available
        if laser_values:
            for i in range(NUM_LASER_RAYS):
                angle_deg = i - 90
                angle_rad = np.radians(angle_deg) + yaw
                dist = laser_values[i]
                lx = int(x + dist * np.cos(angle_rad))
                ly = int(y + dist * np.sin(angle_rad))
                if 0 <= ly < img.shape[0] and 0 <= lx < img.shape[1]:
                    cv2.line(img, (x, y), (lx, ly), COLOR_LASER, 1)

        # Show window
        cv2.namedWindow("Vacuum Robot Simulator", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Vacuum Robot Simulator", 800, 800) 

        cv2.imshow("Vacuum Robot Simulator", img)
        cv2.waitKey(1)
