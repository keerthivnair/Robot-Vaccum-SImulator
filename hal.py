import numpy as np
import math
from config import *
import random


class HAL:
    def __init__(self, map_array):
        self.x = 20.0  # Initial x-position
        self.y = 20.0  # Initial y-position
        self.yaw = 0.0  # Initial yaw (in radians)
        self.map_array = map_array  # Map (2D numpy array)
        self.v = 0.0  # Linear velocity
        self.w = 0.0  # Angular velocity

    def setV(self, v):
        self.v = v

    def setW(self, w):
        self.w = w

    def update(self, dt = TIME_STEP):
        self.yaw += self.w * dt
        self.x += self.v * math.cos(self.yaw) * dt
        self.y += self.v * math.sin(self.yaw) * dt

    def getPose3d(self):
        return {
            'x': self.x,
            'y': self.y,
            'yaw': self.yaw,
        }

    def getBumperData(self):
        row = int(round(self.y))
        col = int(round(self.x))
        if 0 <= row < self.map_array.shape[0] and 0 <= col < self.map_array.shape[1]:
            crash = self.map_array[row, col] == 1
        else:
            crash = True  # Outside map means crash
        return {
            'state': crash,
            'bumper': random.choice([0, 1, 2]) if crash else -1,
        }

    def getLaserData(self):
        values = []
        for i in range(NUM_LASER_RAYS):
            angle_deg = i - 90  # from -90 to +90
            angle_rad = math.radians(angle_deg) + self.yaw
            dist = self._raycast(angle_rad)
            values.append(dist)
        return {'values': values}

    def _raycast(self, angle):
        # each step distance from current increases with d
        for d in range(1, LASER_RANGE + 1):
            xi = int(round(self.x + d * math.cos(angle)))
            yi = int(round(self.y + d * math.sin(angle)))

            if not (0 <= yi < self.map_array.shape[0] and 0 <= xi < self.map_array.shape[1]):
                break  # Outside bounds

            if self.map_array[yi, xi] == 1:
                return d  #  obstacle

        return LASER_RANGE  # No obstacle within range
