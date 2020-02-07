# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RoboticaV2.0.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar) #Libreria de Ploteo 
import numpy as np
import random
import math
from mpl_toolkits.mplot3d import Axes3D #Complemento de la libreria de ploteo para 3d
import serial #Libreria de comunicación Serial
import maestro
from Adafruit_IO import Client, Data

ADAFRUIT_IO_USERNAME = "AlfaRog"
ADAFRUIT_IO_KEY = "3dfaa1c4618c41718ca6725367e40892"


aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#servo = maestro.Controller("/dev/ttyACM0") #Puerto COM para Linux
servo = maestro.Controller("COM4") #Puerto COM para Windows cambiar por el asignado 

class Ui_MainWindow(object):

################### Configuración de GUI ####################

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1211, 569)
        MainWindow.setMinimumSize(QtCore.QSize(881, 569))
        MainWindow.setMaximumSize(QtCore.QSize(2000, 2000))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 246, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 159, 157))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(119, 119, 118))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 341, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 130, 181, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 130, 181, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 121, 31))
        self.label_4.setObjectName("label_4")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(150, 190, 171, 33))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.T1.setFont(font)
        self.T1.setObjectName("T1")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 121, 31))
        self.label_5.setObjectName("label_5")
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(150, 250, 171, 33))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.T2.setFont(font)
        self.T2.setObjectName("T2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 131, 31))
        self.label_6.setObjectName("label_6")
        self.E1 = QtWidgets.QLineEdit(self.centralwidget)
        self.E1.setGeometry(QtCore.QRect(150, 310, 171, 33))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.E1.setFont(font)
        self.E1.setObjectName("E1")
        self.BCD = QtWidgets.QPushButton(self.centralwidget)
        self.BCD.setGeometry(QtCore.QRect(130, 380, 191, 41))
        self.BCD.setObjectName("BCD")
        self.BCI = QtWidgets.QPushButton(self.centralwidget)
        self.BCI.setGeometry(QtCore.QRect(580, 380, 191, 41))
        self.BCI.setObjectName("BCI")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 190, 21, 31))
        self.label_7.setObjectName("label_7")
        self.X = QtWidgets.QLineEdit(self.centralwidget)
        self.X.setGeometry(QtCore.QRect(590, 190, 171, 33))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.X.setFont(font)
        self.X.setObjectName("X")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 250, 21, 31))
        self.label_8.setObjectName("label_8")
        self.Z = QtWidgets.QLineEdit(self.centralwidget)
        self.Z.setGeometry(QtCore.QRect(590, 310, 171, 33))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Z.setFont(font)
        self.Z.setObjectName("Z")
        self.Y = QtWidgets.QLineEdit(self.centralwidget)
        self.Y.setGeometry(QtCore.QRect(590, 250, 171, 33))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Y.setFont(font)
        self.Y.setObjectName("Y")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(570, 310, 21, 31))
        self.label_9.setObjectName("label_9")
        self.Home = QtWidgets.QPushButton(self.centralwidget)
        self.Home.setGeometry(QtCore.QRect(360, 420, 171, 61))
        self.Home.setObjectName("Home")
        self.Cerrar = QtWidgets.QPushButton(self.centralwidget)
        self.Cerrar.setGeometry(QtCore.QRect(900, 470, 171, 41))
        self.Cerrar.setObjectName("Cerrar")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(340, 160, 201, 231))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("imagen.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(810, 120, 371, 271))
        self.MplWidget.setObjectName("MplWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1211, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

####################### Fin de la configuracion del GUI ########################################

####################### Linkeo de botones a funciones ##########################################

        self.BCD.clicked.connect(self.update_graph)
        self.BCI.clicked.connect(self.InversaFuncion)
        self.Home.clicked.connect(self.Home_Set)
        self.Cerrar.clicked.connect(self.Cierre)

################################ Fin del Linkeo #########################################################


######################## Matrices de Rotacion y Traslacion ##############################################

    def RotacionX(self,T):
        H = T*np.pi/180
        X = np.array([[1, 0, 0, 0], [0, math.cos(H), -1*math.sin(H), 0],[0, math.sin(H), math.cos(H), 0], [0, 0, 0, 1]])
        return X

    def RotacionY(self,T):
        H = T*np.pi/180
        Y = np.array([[math.cos(H), 0, math.sin(H), 0], [0, 1, 0, 0], [-1*math.sin(H), 0, math.cos(H), 0], [0 ,0, 0, 1]])
        return Y

    def RotacionZ(self,T):
        H = T*np.pi/180
        Z = np.array([[math.cos(H), -1*math.sin(H), 0, 0], [math.sin(H), math.cos(H), 0, 0], [0, 0, 1, 0],[0 , 0, 0, 1]])
        return Z

    def Traslacion(self,x,y,z):
        Tr = np.array([[1, 0, 0, x],[0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])
        return(Tr)
############################### Fin de las matrices #######################################################

############################# Inicio de las funciones #####################################################

    def update_graph(self, MainWindow):
        g1 = float(self.T1.text())
        g2 = float(self.T2.text())
        E1 = float(self.E1.text())
        g1 = 180 - g1
        g2 = 180 - g2
        if g1 >= 180:
            g1 = 180
        if g1 <= 0:
            g1 = 0
        self.T1.setText(str(180-g1))
        if g2 >= 180:
            g2 = 180
        if g2 <= 0:
            g2 = 0
        self.T2.setText(str(180-g2))
        if E1 >= 4.0:
            E1 = 4
        if E1 <= 0:
            E1 = 0
        self.E1.setText(str(E1))

        r1 = int(g1 * 33.33) + 3000
        r2 = int(g2 * 33.33) + 3000
        servo.setAccel(0,15)
        servo.setAccel(1,15)
        servo.setSpeed(0,60)
        servo.setSpeed(1,60)
        servo.setTarget(0,r1)
        servo.setTarget(1,r2)  
        t3 = aio.feeds('dist')
        t3send = aio.send_data(t3.key, (E1*10))

        MS1 = np.matmul(self.RotacionZ(180-g1),self.Traslacion(0,0,10))#Eslabon 1
        MS2 = np.matmul(MS1, self.RotacionX(180-g2))
        MS3 = np.matmul(MS2, self.Traslacion(0,0,7.4)) #Eslabon 2
        MS4 = np.matmul(MS3, self.Traslacion(0,0,E1))#Eslabon de desplazamiento Dezplazamiento mayor = 3.58

#### --------------------- Asignación de los plots al programa auxiliar mplwidget ----------------------- ###

        self.MplWidget.canvas.axes.plot([0, MS2[0,3]], [0,MS2[1,3]], [0, MS2[2,3]], color=(.4, .5, .6))
        self.MplWidget.canvas.axes.plot([0, MS2[0,3]], [0,MS2[1,3]], [0, MS2[2,3]], 'og')

        self.MplWidget.canvas.axes.plot([MS2[0,3], MS3[0,3]], [MS2[1,3], MS3[1,3]], [MS2[2,3], MS3[2,3]], color=(.4, .5, .6))
        self.MplWidget.canvas.axes.plot([MS2[0,3], MS3[0,3]], [MS2[1,3], MS3[1,3]], [MS2[2,3], MS3[2,3]], 'og')

        self.MplWidget.canvas.axes.plot([MS3[0,3], MS4[0,3]], [MS3[1,3], MS4[1,3]], [MS3[2,3], MS4[2,3]], color=(.4, .5, .6))
        self.MplWidget.canvas.axes.plot([MS3[0,3], MS4[0,3]], [MS3[1,3], MS4[1,3]], [MS3[2,3], MS4[2,3]], 'og')


        self.MplWidget.canvas.axes.set_xlim3d(15, -15)
        self.MplWidget.canvas.axes.set_ylim3d(15, -15)
        self.MplWidget.canvas.axes.set_zlim3d(0,15)
        self.MplWidget.canvas.draw()
### ------------------------------------------------------------------------------------------------------ ###

        print(MS4[0,3])
        print(MS4[1,3])
        print(MS4[2,3]) 

    def InversaFuncion(self, MainWindow): 
        x = float(self.X.text())
        y = float(self.Y.text())
        z = float(self.Z.text())
        theta1 = math.degrees(math.atan(y/x))
        env1 = (-1 * math.cos(math.radians(theta1)) * x) - math.sin(math.radians(theta1)) * y
        env2 = z - 10 
        theta2 = math.degrees((math.atan(env1/env2)))
        d = ( (-1 * math.sin(math.radians(theta2)) * math.cos(math.radians(theta1) )* x) - math.sin(math.radians(theta2)) * math.sin(math.radians(theta1) ) * y + math.cos(math.radians(theta2)) * z - math.cos(math.radians(theta2)) * 10)
        dprim = d - 7.4

        if dprim >= 4:
            dprim = 4
        if dprim <= 0:
            dprim = 0
        if theta1 >= 180:
            theta1 = 180
        if theta1 <= 0:
            theta1 = 0
        if theta2 >= 180:
            theta2 = 180
        if theta2 <= 0:
            theta2 = 0


        print(180 - theta1)
        print(180 - theta2)
        print(dprim) 

        r1 = int((180- theta1) * 33.33) + 3000
        r2 = int((180- theta2) * 33.33) + 3000
        servo.setAccel(0,15)
        servo.setAccel(1,15)
        servo.setSpeed(0,60)
        servo.setSpeed(1,60)
        servo.setTarget(0,r1)
        servo.setTarget(1,r2)  
        t3 = aio.feeds('dist')
        t3send = aio.send_data(t3.key, (dprim*10))

        MS1 = np.matmul(self.RotacionZ(theta1),self.Traslacion(0,0,10))#Eslabon 1
        MS2 = np.matmul(MS1, self.RotacionX(theta2))
        MS3 = np.matmul(MS2, self.Traslacion(0,0,7.4)) #Eslabon 2
        MS4 = np.matmul(MS3, self.Traslacion(0,0,dprim))#Eslabon de desplazamiento Dezplazamiento mayor = 3.58

        self.MplWidget.canvas.axes.plot([0, MS2[0,3]], [0,MS2[1,3]], [0, MS2[2,3]], color=(.4, .5, .6))
        self.MplWidget.canvas.axes.plot([0, MS2[0,3]], [0,MS2[1,3]], [0, MS2[2,3]], 'og')

        self.MplWidget.canvas.axes.plot([MS2[0,3], MS3[0,3]], [MS2[1,3], MS3[1,3]], [MS2[2,3], MS3[2,3]], color=(.4, .5, .6))
        self.MplWidget.canvas.axes.plot([MS2[0,3], MS3[0,3]], [MS2[1,3], MS3[1,3]], [MS2[2,3], MS3[2,3]], 'og')

        self.MplWidget.canvas.axes.plot([MS3[0,3], MS4[0,3]], [MS3[1,3], MS4[1,3]], [MS3[2,3], MS4[2,3]], color=(.4, .5, .6))
        self.MplWidget.canvas.axes.plot([MS3[0,3], MS4[0,3]], [MS3[1,3], MS4[1,3]], [MS3[2,3], MS4[2,3]], 'og')


        self.MplWidget.canvas.axes.set_xlim3d(15, -15)
        self.MplWidget.canvas.axes.set_ylim3d(15, -15)
        self.MplWidget.canvas.axes.set_zlim3d(0,15)
        self.MplWidget.canvas.draw()


    def Home_Set(self,MainWindow):
        self.T1.setText('0')
        self.T2.setText('0')
        self.E1.setText('0')
        servo.setAccel(0,15)
        servo.setAccel(1,15)
        servo.setSpeed(0,60)
        servo.setSpeed(1,60)
        servo.setTarget(0,9000)
        servo.setTarget(1,9000)  
        MS1 = np.matmul(self.RotacionZ(0),self.Traslacion(0,0,10))#Eslabon 1
        MS2 = np.matmul(MS1, self.RotacionX(0))
        MS3 = np.matmul(MS2, self.Traslacion(0,0,7.4)) #Eslabon 2
        MS4 = np.matmul(MS3, self.Traslacion(0,0,0))#Eslabon de desplazamiento Dezplazamiento mayor = 3.58

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot([0, MS2[0,3]], [0,MS2[1,3]], [0, MS2[2,3]], color='red')
        self.MplWidget.canvas.axes.plot([0, MS2[0,3]], [0,MS2[1,3]], [0, MS2[2,3]], 'og')

        self.MplWidget.canvas.axes.plot([MS2[0,3], MS3[0,3]], [MS2[1,3], MS3[1,3]], [MS2[2,3], MS3[2,3]], color='red')
        self.MplWidget.canvas.axes.plot([MS2[0,3], MS3[0,3]], [MS2[1,3], MS3[1,3]], [MS2[2,3], MS3[2,3]], 'og')

        self.MplWidget.canvas.axes.plot([MS3[0,3], MS4[0,3]], [MS3[1,3], MS4[1,3]], [MS3[2,3], MS4[2,3]], color='red')
        self.MplWidget.canvas.axes.plot([MS3[0,3], MS4[0,3]], [MS3[1,3], MS4[1,3]], [MS3[2,3], MS4[2,3]], 'og')


        self.MplWidget.canvas.axes.set_xlim3d(15, -15)
        self.MplWidget.canvas.axes.set_ylim3d(15, -15)
        self.MplWidget.canvas.axes.set_zlim3d(0,15)
        self.MplWidget.canvas.draw()

    def Cierre(self,MainWindow):
        servo.close()
        sys.exit(0)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robotica "))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Proyecto Final </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cinematica Directa</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cinematica Inversa</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Angulo Theta 1:</span></p></body></html>"))
        self.T1.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Angulo Theta 2:</span></p></body></html>"))
        self.T2.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Desplazamiento:</span></p></body></html>"))
        self.E1.setText(_translate("MainWindow", "0"))
        self.BCD.setText(_translate("MainWindow", "Enviar Datos C.D."))
        self.BCI.setText(_translate("MainWindow", "Enviar Datos C.I."))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">X:</span></p></body></html>"))
        self.X.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Y:</span></p></body></html>"))
        self.Z.setText(_translate("MainWindow", "0"))
        self.Y.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Z:</span></p></body></html>"))
        self.Home.setText(_translate("MainWindow", "Enviar a Home"))
        self.Cerrar.setText(_translate("MainWindow", "Cerrar Programa"))

############# Importacion de la clase MplWidget del programa mplwidget para ploteo ###################################
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
