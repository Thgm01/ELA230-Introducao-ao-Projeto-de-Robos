import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from ui_mainwindow import Ui_MainWindow
from robot import Robot

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.set_hp_button.clicked.connect(self.set_hp_button_clicked)
        self.ui.set_all_button.clicked.connect(self.set_all_button_clicked)

        self.ui.set_j1_button.clicked.connect(self.set_j1_button_clicked)
        self.ui.set_j2_button.clicked.connect(self.set_j2_button_clicked)
        self.ui.set_j3_button.clicked.connect(self.set_j3_button_clicked)
        self.ui.set_ee_button.clicked.connect(self.set_ee_button_clicked)

        self.robot = Robot()


    def show(self):
        self.main_win.show()

    def set_hp_button_clicked(self):
        self.robot.home_position()
        self.ui_atualize_joints_angles()

    def set_all_button_clicked(self):
        self.set_j1_button_clicked()
        self.set_j2_button_clicked()
        self.set_j3_button_clicked()
        self.set_ee_button_clicked()
        
        pass

    def set_j1_button_clicked(self):

        joint1_angle = self.robot.atual_angles[0]

        if self.ui.joint1_pos.toPlainText().isnumeric():
            joint1_angle = int(self.ui.joint1_pos.toPlainText())

        self.robot.set_single_joint_angle(1, joint1_angle)
        self.ui.joint1_pos.setText(str(self.robot.atual_angles[0]))

    def set_j2_button_clicked(self):

        joint2_angle = self.robot.atual_angles[1]

        if self.ui.joint2_pos.toPlainText().isnumeric():
            joint2_angle = int(self.ui.joint2_pos.toPlainText())

        self.robot.set_single_joint_angle(2, joint2_angle)
        self.ui.joint2_pos.setText(str(self.robot.atual_angles[1]))

    def set_j3_button_clicked(self):

        joint3_angle = self.robot.atual_angles[2]

        if self.ui.joint3_pos.toPlainText().isnumeric():
            joint3_angle = int(self.ui.joint3_pos.toPlainText())

        self.robot.set_single_joint_angle(3, joint3_angle)
        self.ui.joint3_pos.setText(str(self.robot.atual_angles[2]))

    def set_ee_button_clicked(self):

        ee_angle = self.robot.atual_angles[3]

        if self.ui.ee_pos.toPlainText().isnumeric():
            ee_angle = int(self.ui.ee_pos.toPlainText())

        self.robot.set_single_joint_angle(4, ee_angle)
        self.ui.ee_pos.setText(str(self.robot.atual_angles[3]))

    def ui_atualize_joints_angles(self):
        self.ui.joint1_pos.setText(str(self.robot.atual_angles[0]))
        self.ui.joint2_pos.setText(str(self.robot.atual_angles[1]))
        self.ui.joint3_pos.setText(str(self.robot.atual_angles[2]))
        self.ui.ee_pos.setText(str(self.robot.atual_angles[3]))
        





    




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
