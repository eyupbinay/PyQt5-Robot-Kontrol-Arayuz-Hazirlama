#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_kontrol.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

maxDistance=0
RADIUS=4
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 348)
        MainWindow.setMinimumSize(QtCore.QSize(500, 348))
        MainWindow.setMaximumSize(QtCore.QSize(500, 348))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.etiket_lineer = QtWidgets.QLabel(self.centralwidget)
        self.etiket_lineer.setObjectName("etiket_lineer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.etiket_lineer)
        self.line_lineer = QtWidgets.QLineEdit(self.centralwidget)
        self.line_lineer.setReadOnly(True)
        self.line_lineer.setObjectName("line_lineer")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_lineer)
        self.etiket_acisal = QtWidgets.QLabel(self.centralwidget)
        self.etiket_acisal.setObjectName("etiket_acisal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.etiket_acisal)
        self.line_acisal = QtWidgets.QLineEdit(self.centralwidget)
        self.line_acisal.setReadOnly(True)
        self.line_acisal.setObjectName("line_acisal")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_acisal)
        self.gridLayout_2.addLayout(self.formLayout, 1, 1, 1, 1)
        self.etiket_kontrol = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_kontrol.setFont(font)
        self.etiket_kontrol.setObjectName("etiket_kontrol")
        self.gridLayout_2.addWidget(self.etiket_kontrol, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.buton_geri.setObjectName("buton_geri")
        self.gridLayout.addWidget(self.buton_geri, 2, 1, 1, 1)
        self.buton_ileri = QtWidgets.QPushButton(self.centralwidget)
        self.buton_ileri.setObjectName("buton_ileri")
        self.gridLayout.addWidget(self.buton_ileri, 0, 1, 1, 1)
        self.buton_dur = QtWidgets.QPushButton(self.centralwidget)
        self.buton_dur.setObjectName("buton_dur")
        self.gridLayout.addWidget(self.buton_dur, 1, 1, 1, 1)
        self.buton_sag = QtWidgets.QPushButton(self.centralwidget)
        self.buton_sag.setObjectName("buton_sag")
        self.gridLayout.addWidget(self.buton_sag, 1, 2, 1, 1)
        self.buton_sol = QtWidgets.QPushButton(self.centralwidget)
        self.buton_sol.setObjectName("buton_sol")
        self.gridLayout.addWidget(self.buton_sol, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.etiket_konum = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_konum.setFont(font)
        self.etiket_konum.setObjectName("etiket_konum")
        self.gridLayout_2.addWidget(self.etiket_konum, 4, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.etiket_x = QtWidgets.QLabel(self.centralwidget)
        self.etiket_x.setObjectName("etiket_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.etiket_x)
        self.etiket_y = QtWidgets.QLabel(self.centralwidget)
        self.etiket_y.setObjectName("etiket_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.etiket_y)
        self.line_x = QtWidgets.QLineEdit(self.centralwidget)
        self.line_x.setReadOnly(True)
        self.line_x.setObjectName("line_x")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_x)
        self.line_y = QtWidgets.QLineEdit(self.centralwidget)
        self.line_y.setMaximumSize(QtCore.QSize(476, 348))
        self.line_y.setReadOnly(True)
        self.line_y.setObjectName("line_y")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_y)
        self.gridLayout_2.addLayout(self.formLayout_2, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Kontrol Arayüzü"))
        self.label.setText(_translate("MainWindow", "Hiz Göstergesi"))
        self.etiket_lineer.setText(_translate("MainWindow", "Lineer Hiz(m/s):"))
        self.etiket_acisal.setText(_translate("MainWindow", "Acisal Hiz(rad/s):"))
        self.etiket_kontrol.setText(_translate("MainWindow", "Robot Kontrol"))
        self.buton_geri.setText(_translate("MainWindow", "Geri"))
        self.buton_ileri.setText(_translate("MainWindow", "İleri"))
        self.buton_dur.setText(_translate("MainWindow", "Dur"))
        self.buton_sag.setText(_translate("MainWindow", "Sağ"))
        self.buton_sol.setText(_translate("MainWindow", "Sol"))
        self.etiket_konum.setText(_translate("MainWindow", "Konum Göstergesi"))
        self.etiket_x.setText(_translate("MainWindow", "Konum X(m):"))
        self.etiket_y.setText(_translate("MainWindow", "Konum Y(m):"))
        
        
        rospy.init_node("robot_arayuz")
        self.pub=rospy.Publisher("cmd_vel",Twist,queue_size=10)
        self.hiz_mesaji=Twist()
        rospy.Subscriber("odom",Odometry,self.odomCallback)
        
        self.buton_dur.clicked.connect(self.robotDur)
        self.buton_ileri.clicked.connect(self.ileriGit)
        self.buton_geri.clicked.connect(self.geriGit)
        self.buton_sol.clicked.connect(self.solaDon)
        self.buton_sag.clicked.connect(self.sagaDon)
        
 
        self.line_acisal.setText(str(0.0))
        self.line_lineer.setText(str(0.0))
        self.line_x.setText(str(0.0))
        self.line_y.setText(str(0.0))
        
    def robotDur(self):
        self.hiz_mesaji.linear.x=0.0
        self.hiz_mesaji.angular.z=0.0
        self.pub.publish(self.hiz_mesaji)
        self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
        self.line_acisal.setText(str(self.hiz_mesaji.angular.z))
        
  


    def ileriGit(self):
        self.hiz_mesaji.linear.x=0.5
        self.hiz_mesaji.angular.z=0.0
        self.pub.publish(self.hiz_mesaji)
        self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
        self.line_acisal.setText(str(self.hiz_mesaji.angular.z))
        
    def odomCallback(self,mesaj):
        self.line_x.setText(str(round(mesaj.pose.pose.position.x,4)))
        self.line_y.setText(str(round(mesaj.pose.pose.position.y,4)))
        x1 = -1.69
        y1 = -6.14 
        x2 = round(mesaj.pose.pose.position.x,2)
        y2 = round(mesaj.pose.pose.position.y,2)
        distance = ((x1-x2)**2+(y1-y2)**2)**(1/2)
        if distance>maxDistance:
            maxDistance=distance
        if (distance <= RADIUS and maxDistance>5):
            self.hiz_mesaji.linear.x=0.0
            self.hiz_mesaji.angular.z=0.0
            self.pub.publish(self.hiz_mesaji)
            self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
            self.line_acisal.setText(str(self.hiz_mesaji.angular.z))
            
            

    def geriGit(self):
        self.hiz_mesaji.linear.x=-0.5
        self.hiz_mesaji.angular.z=0.0
        self.pub.publish(self.hiz_mesaji)
        self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
        self.line_acisal.setText(str(self.hiz_mesaji.angular.z))



    def solaDon(self):
        self.hiz_mesaji.linear.x=0.0
        self.hiz_mesaji.angular.z=0.5
        self.pub.publish(self.hiz_mesaji)
        self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
        self.line_acisal.setText(str(self.hiz_mesaji.angular.z))



    def sagaDon(self):
        self.hiz_mesaji.linear.x=0.0
        self.hiz_mesaji.angular.z=-0.5
        self.pub.publish(self.hiz_mesaji)
        self.line_lineer.setText(str(self.hiz_mesaji.linear.x))
        self.line_acisal.setText(str(self.hiz_mesaji.angular.z))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
