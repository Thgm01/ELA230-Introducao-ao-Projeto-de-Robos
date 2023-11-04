# from board import SCL, SDA
# import busio

# from adafruit_motor import servo
# from adafruit_pca9685 import PCA9685

UPPER_LIMIT_PWM = 2000
LOWER_LIMIT_PWM = 10000

UPPER_LIMIT_DG = 180
LOWER_LIMIT_DG = 0

class Robot:
    def __init__(self):
        # self.pca = PCA9685(busio.I2C(SCL, SDA))
        # self.pca.reference_clock_speed = 26624000
        # self.pca.frequency = 60
        self.joints_number = 4
        
        self.home_angles = [90,90,90,90]
        self.atual_angles = self.home_angles


    def degrees_to_pwm(self, angle_degrees):
        angle_pwm = int((UPPER_LIMIT_PWM - LOWER_LIMIT_PWM)/(UPPER_LIMIT_DG - LOWER_LIMIT_DG)*angle_degrees + LOWER_LIMIT_PWM)
        return angle_pwm


    def set_single_joint_angle(self, joint_number, angle_degrees):
        # angle_pwm = self.degrees_to_pwm(angle_degrees)
        # self.pca.channels[joint_number-1].duty_cycle = angle_pwm
        self.atual_angles[joint_number-1] = angle_degrees
        print(f'Set Joint {joint_number}: {angle_degrees}\t | All angles: {self.atual_angles}')

    def set_all_joints_angle(self, list_angle_degrees):
        for j in range(0, self.joints_number):
            self.set_single_joint_angle(j+1, list_angle_degrees[j])


    def stop_robot(self):
        self.pca.deinit()

    def home_position(self):
        self.set_all_joints_angle(self.home_angles)
