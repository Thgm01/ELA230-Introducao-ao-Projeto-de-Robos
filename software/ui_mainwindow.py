# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.side2_robot = QtWidgets.QLabel(self.centralwidget)
        self.side2_robot.setEnabled(True)
        self.side2_robot.setGeometry(QtCore.QRect(0, 0, 611, 421))
        self.side2_robot.setText("")
        self.side2_robot.setPixmap(QtGui.QPixmap("../docs/robot_files/images/side2.jpg"))
        self.side2_robot.setScaledContents(True)
        self.side2_robot.setObjectName("side2_robot")
        self.joint1_pos = QtWidgets.QTextEdit(self.centralwidget)
        self.joint1_pos.setGeometry(QtCore.QRect(550, 360, 61, 31))
        self.joint1_pos.setAcceptRichText(False)
        self.joint1_pos.setObjectName("joint1_pos")
        self.joint2_pos = QtWidgets.QTextEdit(self.centralwidget)
        self.joint2_pos.setGeometry(QtCore.QRect(330, 320, 61, 31))
        self.joint2_pos.setAcceptRichText(False)
        self.joint2_pos.setObjectName("joint2_pos")
        self.joint3_pos = QtWidgets.QTextEdit(self.centralwidget)
        self.joint3_pos.setGeometry(QtCore.QRect(370, 140, 61, 31))
        self.joint3_pos.setAcceptRichText(False)
        self.joint3_pos.setObjectName("joint3_pos")
        self.ee_pos = QtWidgets.QTextEdit(self.centralwidget)
        self.ee_pos.setGeometry(QtCore.QRect(190, 200, 61, 31))
        self.ee_pos.setAcceptRichText(False)
        self.ee_pos.setObjectName("ee_pos")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 230, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 340, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 300, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 170, 101, 20))
        self.label_4.setObjectName("label_4")
        self.set_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_all_button.setGeometry(QtCore.QRect(150, 440, 131, 25))
        self.set_all_button.setObjectName("set_all_button")
        self.set_j1_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_j1_button.setGeometry(QtCore.QRect(10, 470, 131, 25))
        self.set_j1_button.setObjectName("set_j1_button")
        self.set_j2_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_j2_button.setGeometry(QtCore.QRect(150, 470, 131, 25))
        self.set_j2_button.setObjectName("set_j2_button")
        self.set_j3_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_j3_button.setGeometry(QtCore.QRect(10, 500, 131, 25))
        self.set_j3_button.setObjectName("set_j3_button")
        self.set_ee_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_ee_button.setGeometry(QtCore.QRect(150, 500, 131, 25))
        self.set_ee_button.setObjectName("set_ee_button")
        self.set_hp_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_hp_button.setGeometry(QtCore.QRect(10, 440, 131, 25))
        self.set_hp_button.setObjectName("set_hp_button")
        self.new_mov_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_mov_button.setGeometry(QtCore.QRect(310, 440, 141, 25))
        self.new_mov_button.setObjectName("new_mov_button")
        self.save_pos_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_pos_button.setGeometry(QtCore.QRect(390, 500, 141, 25))
        self.save_pos_button.setObjectName("save_pos_button")
        self.exclude_mov_button = QtWidgets.QPushButton(self.centralwidget)
        self.exclude_mov_button.setGeometry(QtCore.QRect(460, 440, 141, 25))
        self.exclude_mov_button.setObjectName("exclude_mov_button")
        self.previous_pos_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_pos_button.setGeometry(QtCore.QRect(310, 470, 141, 25))
        self.previous_pos_button.setObjectName("previous_pos_button")
        self.next_pos_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_pos_button.setGeometry(QtCore.QRect(460, 470, 141, 25))
        self.next_pos_button.setObjectName("next_pos_button")
        self.move_label = QtWidgets.QLabel(self.centralwidget)
        self.move_label.setGeometry(QtCore.QRect(260, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.move_label.setFont(font)
        self.move_label.setTextFormat(QtCore.Qt.AutoText)
        self.move_label.setAlignment(QtCore.Qt.AlignCenter)
        self.move_label.setObjectName("move_label")
        self.play_move_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_move_button.setGeometry(QtCore.QRect(150, 550, 141, 25))
        self.play_move_button.setObjectName("play_move_button")
        self.stop_move_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_move_button.setGeometry(QtCore.QRect(300, 550, 141, 25))
        self.stop_move_button.setObjectName("stop_move_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "End Effector"))
        self.label_2.setText(_translate("MainWindow", "Joint 1"))
        self.label_3.setText(_translate("MainWindow", "Joint 2"))
        self.label_4.setText(_translate("MainWindow", "Joint 3"))
        self.set_all_button.setText(_translate("MainWindow", "Set All Joints"))
        self.set_j1_button.setText(_translate("MainWindow", "Set Joint 1"))
        self.set_j2_button.setText(_translate("MainWindow", "Set Joint 2"))
        self.set_j3_button.setText(_translate("MainWindow", "Set Joint 3"))
        self.set_ee_button.setText(_translate("MainWindow", "Set End Effector"))
        self.set_hp_button.setText(_translate("MainWindow", "Home Position"))
        self.new_mov_button.setText(_translate("MainWindow", "New Movement"))
        self.save_pos_button.setText(_translate("MainWindow", "Save Position"))
        self.exclude_mov_button.setText(_translate("MainWindow", "Exclude Movement"))
        self.previous_pos_button.setText(_translate("MainWindow", "Previous Position"))
        self.next_pos_button.setText(_translate("MainWindow", "Next Position"))
        self.move_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.play_move_button.setText(_translate("MainWindow", "Play"))
        self.stop_move_button.setText(_translate("MainWindow", "Stop"))
