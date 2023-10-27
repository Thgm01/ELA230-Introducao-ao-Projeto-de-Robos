# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(548, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.side2_robot = QtWidgets.QLabel(self.centralwidget)
        self.side2_robot.setEnabled(True)
        self.side2_robot.setGeometry(QtCore.QRect(0, 0, 531, 381))
        self.side2_robot.setText("")
        self.side2_robot.setPixmap(QtGui.QPixmap("../docs/robot_files/images/side2.jpg"))
        self.side2_robot.setScaledContents(True)
        self.side2_robot.setObjectName("side2_robot")
        self.joit1_pos = QtWidgets.QTextEdit(self.centralwidget)
        self.joit1_pos.setGeometry(QtCore.QRect(470, 320, 61, 31))
        self.joit1_pos.setObjectName("joit1_pos")
        self.joit2_pos = QtWidgets.QTextEdit(self.centralwidget)
        self.joit2_pos.setGeometry(QtCore.QRect(280, 280, 61, 31))
        self.joit2_pos.setObjectName("joit2_pos")
        self.joit3_pos = QtWidgets.QTextEdit(self.centralwidget)
        self.joit3_pos.setGeometry(QtCore.QRect(330, 120, 61, 31))
        self.joit3_pos.setObjectName("joit3_pos")
        self.joit4_pos = QtWidgets.QTextEdit(self.centralwidget)
        self.joit4_pos.setGeometry(QtCore.QRect(170, 180, 61, 31))
        self.joit4_pos.setObjectName("joit4_pos")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 210, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 300, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 260, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 150, 101, 20))
        self.label_4.setObjectName("label_4")
        self.set_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_all_button.setGeometry(QtCore.QRect(260, 390, 131, 25))
        self.set_all_button.setObjectName("set_all_button")
        self.set_j1_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_j1_button.setGeometry(QtCore.QRect(120, 420, 131, 25))
        self.set_j1_button.setObjectName("set_j1_button")
        self.set_j2_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_j2_button.setGeometry(QtCore.QRect(260, 420, 131, 25))
        self.set_j2_button.setObjectName("set_j2_button")
        self.set_j3_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_j3_button.setGeometry(QtCore.QRect(120, 450, 131, 25))
        self.set_j3_button.setObjectName("set_j3_button")
        self.set_ee_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_ee_button.setGeometry(QtCore.QRect(260, 450, 131, 25))
        self.set_ee_button.setObjectName("set_ee_button")
        self.set_hp_button = QtWidgets.QPushButton(self.centralwidget)
        self.set_hp_button.setGeometry(QtCore.QRect(120, 390, 131, 25))
        self.set_hp_button.setObjectName("set_hp_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 548, 22))
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
