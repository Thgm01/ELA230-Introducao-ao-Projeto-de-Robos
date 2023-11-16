from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

UPPER_LIMIT_PWM = 2000
LOWER_LIMIT_PWM = 10000

class Robot:
    def __init__(self):
        self.pca = PCA9685(busio.I2C(SCL, SDA))
        self.pca.reference_clock_speed = 26624000
        self.pca.frequency = 60
        self.joints_number = 4
        
        self.home_angles = [90,90,90,90]
        self.limits = ((0, 180), (40,125), (0, 180), (0, 180))
        self.atual_angles = [90,90,90,90]

    def validade(self, joint_number, angle_degrees):
        upper_limit = self.limits[joint_number-1][1]
        lower_limit = self.limits[joint_number-1][0]

        if joint_number == 3:
            lower_limit = abs(self.atual_angles[1]-155)
            upper_limit = 150

            if angle_degrees < lower_limit:
                return lower_limit
            elif angle_degrees > upper_limit:
                return upper_limit
            
            return angle_degrees
            
        else:
            if angle_degrees < lower_limit:
                print('1')
                return lower_limit
            elif angle_degrees > upper_limit:
                print('2')
                return upper_limit

            print('3')

            return angle_degrees
        
        
    def degrees_to_pwm(self, angle_degrees):
        angle_pwm = int((UPPER_LIMIT_PWM - LOWER_LIMIT_PWM)/(180 - 0)*angle_degrees + LOWER_LIMIT_PWM)
        return angle_pwm


    def set_single_joint_angle(self, joint_number, angle_degrees):
        angle_degrees = self.validade(joint_number, angle_degrees)
        angle_pwm = self.degrees_to_pwm(angle_degrees)
        self.pca.channels[joint_number-1].duty_cycle = angle_pwm
        self.atual_angles[joint_number-1] = angle_degrees
        print(f'Set Joint {joint_number}: {angle_degrees}\t | All angles: {self.atual_angles}')

    def set_all_joints_angle(self, list_angle_degrees):
        for j in range(0, self.joints_number):
            self.set_single_joint_angle(j+1, list_angle_degrees[j])


    def stop_robot(self):
        self.pca.deinit()

    def home_position(self):
        self.set_all_joints_angle(self.home_angles)

    def trajectory(self, angles_list):
        for angles in angles_list:
            self.set_all_joints_angle(angles)


