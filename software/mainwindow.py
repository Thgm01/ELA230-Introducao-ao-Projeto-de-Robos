import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from ui_mainwndow import Ui_MainWindow
from robot import Robot

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.set_hp_button.clicked.connect(self.set_hp_button_clicked)
        self.ui.set_all_button.clicked.connect(self.set_all_button_clicked)

        self.ui.set_j1_button.clicked.connect(self.set_j1_button_clicked)
        

        self.robot = Robot()


    def show(self):
        self.main_win.show()

    def set_hp_button_clicked(self):
        print('set_hp_clicado')
        self.robot.home_position()
        print(self.robot.atual_angles)

    def set_all_button_clicked(self):
        pass

    def set_j1_button_clicked(self):
        pass




    




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
