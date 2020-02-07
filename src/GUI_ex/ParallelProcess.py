# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LecturaRPI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Encendido = QtWidgets.QPushButton(self.centralwidget)
        self.Encendido.setGeometry(QtCore.QRect(40, 130, 161, 61))
        self.Encendido.setObjectName("Encendido")
        self.Apagado = QtWidgets.QPushButton(self.centralwidget)
        self.Apagado.setGeometry(QtCore.QRect(40, 210, 161, 61))
        self.Apagado.setObjectName("Apagado")
        self.Cerrar = QtWidgets.QPushButton(self.centralwidget)
        self.Cerrar.setGeometry(QtCore.QRect(470, 320, 181, 71))
        self.Cerrar.setObjectName("Cerrar")
        self.Temp = QtWidgets.QLineEdit(self.centralwidget)
        self.Temp.setGeometry(QtCore.QRect(460, 120, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.Temp.setFont(font)
        self.Temp.setObjectName("Temp")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 120, 141, 51))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Encendido.clicked.connect(self.fEncendido)
        self.Apagado.clicked.connect(self.fApagado)
        self.Cerrar.clicked.connect(self.fCerrado)

###################### Secuencia en paralelo configuración e inicio ###########################

        self.Temperatura()
        self.my_time = QtCore.QTimer()
        self.my_time.timeout.connect(self.Temperatura)
        self.my_time.start(1000) #Tiempo de refresh 


##################### Fin de configuración ####################################################

    def fEncendido(self, MainWindow):
        GPIO.output(12, GPIO.HIGH)

    def fApagado(self, MainWindow):
        GPIO.output(12, GPIO.LOW)

    def fCerrado(self, MainWindow):
        sys.exit(0)

##################### Funcion de refresh en paralelo ##########################################
    def Temperatura(self):
        tFile = open('/sys/class/thermal/thermal_zone0/temp')
        temp = float(tFile.read())
        tempC = temp/1000
        self.Temp.setText(str(tempC))
        
############################## Fin de Funcion en paralelo #####################################


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ejemplo 2"))
        self.Encendido.setText(_translate("MainWindow", "Encendido Led"))
        self.Apagado.setText(_translate("MainWindow", "Apagado Led"))
        self.Cerrar.setText(_translate("MainWindow", "Cerrar"))
        self.label_2.setText(_translate("MainWindow", "Temperatura Rasp"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

