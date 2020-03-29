# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_solver.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(647, 732)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b11 = QtWidgets.QTextEdit(self.centralwidget)
        self.b11.setGeometry(QtCore.QRect(10, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b11.setFont(font)
        self.b11.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.b11.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.b11.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.b11.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.b11.setDocumentTitle("")
        self.b11.setLineWrapMode(QtWidgets.QTextEdit.FixedPixelWidth)
        self.b11.setLineWrapColumnOrWidth(-1)
        self.b11.setObjectName("b11")
        self.b12 = QtWidgets.QTextEdit(self.centralwidget)
        self.b12.setGeometry(QtCore.QRect(80, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b12.setFont(font)
        self.b12.setObjectName("b12")
        self.b13 = QtWidgets.QTextEdit(self.centralwidget)
        self.b13.setGeometry(QtCore.QRect(150, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b13.setFont(font)
        self.b13.setObjectName("b13")
        self.b15 = QtWidgets.QTextEdit(self.centralwidget)
        self.b15.setGeometry(QtCore.QRect(290, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b15.setFont(font)
        self.b15.setObjectName("b15")
        self.b14 = QtWidgets.QTextEdit(self.centralwidget)
        self.b14.setGeometry(QtCore.QRect(220, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b14.setFont(font)
        self.b14.setObjectName("b14")
        self.b16 = QtWidgets.QTextEdit(self.centralwidget)
        self.b16.setGeometry(QtCore.QRect(360, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b16.setFont(font)
        self.b16.setObjectName("b16")
        self.b18 = QtWidgets.QTextEdit(self.centralwidget)
        self.b18.setGeometry(QtCore.QRect(500, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b18.setFont(font)
        self.b18.setObjectName("b18")
        self.b17 = QtWidgets.QTextEdit(self.centralwidget)
        self.b17.setGeometry(QtCore.QRect(430, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b17.setFont(font)
        self.b17.setObjectName("b17")
        self.b19 = QtWidgets.QTextEdit(self.centralwidget)
        self.b19.setGeometry(QtCore.QRect(570, 10, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b19.setFont(font)
        self.b19.setObjectName("b19")
        self.b25 = QtWidgets.QTextEdit(self.centralwidget)
        self.b25.setGeometry(QtCore.QRect(290, 80, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b25.setFont(font)
        self.b25.setObjectName("b25")
        self.b28 = QtWidgets.QTextEdit(self.centralwidget)
        self.b28.setGeometry(QtCore.QRect(500, 80, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b28.setFont(font)
        self.b28.setObjectName("b28")
        self.b27 = QtWidgets.QTextEdit(self.centralwidget)
        self.b27.setGeometry(QtCore.QRect(430, 80, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b27.setFont(font)
        self.b27.setObjectName("b27")
        self.b26 = QtWidgets.QTextEdit(self.centralwidget)
        self.b26.setGeometry(QtCore.QRect(360, 80, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b26.setFont(font)
        self.b26.setObjectName("b26")
        self.b22 = QtWidgets.QTextEdit(self.centralwidget)
        self.b22.setGeometry(QtCore.QRect(80, 80, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b22.setFont(font)
        self.b22.setObjectName("b22")
        self.b21 = QtWidgets.QTextEdit(self.centralwidget)
        self.b21.setGeometry(QtCore.QRect(10, 80, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b21.setFont(font)
        self.b21.setObjectName("b21")
        self.b23 = QtWidgets.QTextEdit(self.centralwidget)
        self.b23.setGeometry(QtCore.QRect(150, 80, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b23.setFont(font)
        self.b23.setObjectName("b23")
        self.b24 = QtWidgets.QTextEdit(self.centralwidget)
        self.b24.setGeometry(QtCore.QRect(220, 80, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b24.setFont(font)
        self.b24.setObjectName("b24")
        self.b29 = QtWidgets.QTextEdit(self.centralwidget)
        self.b29.setGeometry(QtCore.QRect(570, 80, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b29.setFont(font)
        self.b29.setObjectName("b29")
        self.b44 = QtWidgets.QTextEdit(self.centralwidget)
        self.b44.setGeometry(QtCore.QRect(220, 220, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b44.setFont(font)
        self.b44.setObjectName("b44")
        self.b43 = QtWidgets.QTextEdit(self.centralwidget)
        self.b43.setGeometry(QtCore.QRect(150, 220, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b43.setFont(font)
        self.b43.setObjectName("b43")
        self.b39 = QtWidgets.QTextEdit(self.centralwidget)
        self.b39.setGeometry(QtCore.QRect(570, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b39.setFont(font)
        self.b39.setObjectName("b39")
        self.b33 = QtWidgets.QTextEdit(self.centralwidget)
        self.b33.setGeometry(QtCore.QRect(150, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b33.setFont(font)
        self.b33.setObjectName("b33")
        self.b48 = QtWidgets.QTextEdit(self.centralwidget)
        self.b48.setGeometry(QtCore.QRect(500, 220, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b48.setFont(font)
        self.b48.setObjectName("b48")
        self.b37 = QtWidgets.QTextEdit(self.centralwidget)
        self.b37.setGeometry(QtCore.QRect(430, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b37.setFont(font)
        self.b37.setObjectName("b37")
        self.b49 = QtWidgets.QTextEdit(self.centralwidget)
        self.b49.setGeometry(QtCore.QRect(570, 220, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b49.setFont(font)
        self.b49.setObjectName("b49")
        self.b38 = QtWidgets.QTextEdit(self.centralwidget)
        self.b38.setGeometry(QtCore.QRect(500, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b38.setFont(font)
        self.b38.setObjectName("b38")
        self.b47 = QtWidgets.QTextEdit(self.centralwidget)
        self.b47.setGeometry(QtCore.QRect(430, 220, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b47.setFont(font)
        self.b47.setObjectName("b47")
        self.b34 = QtWidgets.QTextEdit(self.centralwidget)
        self.b34.setGeometry(QtCore.QRect(220, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b34.setFont(font)
        self.b34.setObjectName("b34")
        self.b45 = QtWidgets.QTextEdit(self.centralwidget)
        self.b45.setGeometry(QtCore.QRect(290, 220, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b45.setFont(font)
        self.b45.setObjectName("b45")
        self.b36 = QtWidgets.QTextEdit(self.centralwidget)
        self.b36.setGeometry(QtCore.QRect(360, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b36.setFont(font)
        self.b36.setObjectName("b36")
        self.b32 = QtWidgets.QTextEdit(self.centralwidget)
        self.b32.setGeometry(QtCore.QRect(80, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b32.setFont(font)
        self.b32.setObjectName("b32")
        self.b42 = QtWidgets.QTextEdit(self.centralwidget)
        self.b42.setGeometry(QtCore.QRect(80, 220, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b42.setFont(font)
        self.b42.setObjectName("b42")
        self.b35 = QtWidgets.QTextEdit(self.centralwidget)
        self.b35.setGeometry(QtCore.QRect(290, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b35.setFont(font)
        self.b35.setObjectName("b35")
        self.b31 = QtWidgets.QTextEdit(self.centralwidget)
        self.b31.setGeometry(QtCore.QRect(10, 150, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b31.setFont(font)
        self.b31.setObjectName("b31")
        self.b41 = QtWidgets.QTextEdit(self.centralwidget)
        self.b41.setGeometry(QtCore.QRect(10, 220, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b41.setFont(font)
        self.b41.setObjectName("b41")
        self.b46 = QtWidgets.QTextEdit(self.centralwidget)
        self.b46.setGeometry(QtCore.QRect(360, 220, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b46.setFont(font)
        self.b46.setObjectName("b46")
        self.b64 = QtWidgets.QTextEdit(self.centralwidget)
        self.b64.setGeometry(QtCore.QRect(220, 360, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b64.setFont(font)
        self.b64.setObjectName("b64")
        self.b63 = QtWidgets.QTextEdit(self.centralwidget)
        self.b63.setGeometry(QtCore.QRect(150, 360, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b63.setFont(font)
        self.b63.setObjectName("b63")
        self.b76 = QtWidgets.QTextEdit(self.centralwidget)
        self.b76.setGeometry(QtCore.QRect(360, 430, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b76.setFont(font)
        self.b76.setObjectName("b76")
        self.b78 = QtWidgets.QTextEdit(self.centralwidget)
        self.b78.setGeometry(QtCore.QRect(500, 430, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b78.setFont(font)
        self.b78.setObjectName("b78")
        self.b79 = QtWidgets.QTextEdit(self.centralwidget)
        self.b79.setGeometry(QtCore.QRect(570, 430, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b79.setFont(font)
        self.b79.setObjectName("b79")
        self.b59 = QtWidgets.QTextEdit(self.centralwidget)
        self.b59.setGeometry(QtCore.QRect(570, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b59.setFont(font)
        self.b59.setObjectName("b59")
        self.b82 = QtWidgets.QTextEdit(self.centralwidget)
        self.b82.setGeometry(QtCore.QRect(80, 500, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b82.setFont(font)
        self.b82.setObjectName("b82")
        self.b83 = QtWidgets.QTextEdit(self.centralwidget)
        self.b83.setGeometry(QtCore.QRect(150, 500, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b83.setFont(font)
        self.b83.setObjectName("b83")
        self.b75 = QtWidgets.QTextEdit(self.centralwidget)
        self.b75.setGeometry(QtCore.QRect(290, 430, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b75.setFont(font)
        self.b75.setObjectName("b75")
        self.b53 = QtWidgets.QTextEdit(self.centralwidget)
        self.b53.setGeometry(QtCore.QRect(150, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b53.setFont(font)
        self.b53.setObjectName("b53")
        self.b68 = QtWidgets.QTextEdit(self.centralwidget)
        self.b68.setGeometry(QtCore.QRect(500, 360, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b68.setFont(font)
        self.b68.setObjectName("b68")
        self.b57 = QtWidgets.QTextEdit(self.centralwidget)
        self.b57.setGeometry(QtCore.QRect(430, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b57.setFont(font)
        self.b57.setObjectName("b57")
        self.b71 = QtWidgets.QTextEdit(self.centralwidget)
        self.b71.setGeometry(QtCore.QRect(10, 430, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b71.setFont(font)
        self.b71.setObjectName("b71")
        self.b69 = QtWidgets.QTextEdit(self.centralwidget)
        self.b69.setGeometry(QtCore.QRect(570, 360, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b69.setFont(font)
        self.b69.setObjectName("b69")
        self.b87 = QtWidgets.QTextEdit(self.centralwidget)
        self.b87.setGeometry(QtCore.QRect(430, 500, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b87.setFont(font)
        self.b87.setObjectName("b87")
        self.b58 = QtWidgets.QTextEdit(self.centralwidget)
        self.b58.setGeometry(QtCore.QRect(500, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b58.setFont(font)
        self.b58.setObjectName("b58")
        self.b84 = QtWidgets.QTextEdit(self.centralwidget)
        self.b84.setGeometry(QtCore.QRect(220, 500, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b84.setFont(font)
        self.b84.setObjectName("b84")
        self.b72 = QtWidgets.QTextEdit(self.centralwidget)
        self.b72.setGeometry(QtCore.QRect(80, 430, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b72.setFont(font)
        self.b72.setObjectName("b72")
        self.b81 = QtWidgets.QTextEdit(self.centralwidget)
        self.b81.setGeometry(QtCore.QRect(10, 500, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b81.setFont(font)
        self.b81.setObjectName("b81")
        self.b67 = QtWidgets.QTextEdit(self.centralwidget)
        self.b67.setGeometry(QtCore.QRect(430, 360, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b67.setFont(font)
        self.b67.setObjectName("b67")
        self.b74 = QtWidgets.QTextEdit(self.centralwidget)
        self.b74.setGeometry(QtCore.QRect(220, 430, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b74.setFont(font)
        self.b74.setObjectName("b74")
        self.b54 = QtWidgets.QTextEdit(self.centralwidget)
        self.b54.setGeometry(QtCore.QRect(220, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b54.setFont(font)
        self.b54.setObjectName("b54")
        self.b65 = QtWidgets.QTextEdit(self.centralwidget)
        self.b65.setGeometry(QtCore.QRect(290, 360, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b65.setFont(font)
        self.b65.setObjectName("b65")
        self.b89 = QtWidgets.QTextEdit(self.centralwidget)
        self.b89.setGeometry(QtCore.QRect(570, 500, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b89.setFont(font)
        self.b89.setObjectName("b89")
        self.b73 = QtWidgets.QTextEdit(self.centralwidget)
        self.b73.setGeometry(QtCore.QRect(150, 430, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b73.setFont(font)
        self.b73.setObjectName("b73")
        self.b56 = QtWidgets.QTextEdit(self.centralwidget)
        self.b56.setGeometry(QtCore.QRect(360, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b56.setFont(font)
        self.b56.setObjectName("b56")
        self.b52 = QtWidgets.QTextEdit(self.centralwidget)
        self.b52.setGeometry(QtCore.QRect(80, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b52.setFont(font)
        self.b52.setObjectName("b52")
        self.b77 = QtWidgets.QTextEdit(self.centralwidget)
        self.b77.setGeometry(QtCore.QRect(430, 430, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b77.setFont(font)
        self.b77.setObjectName("b77")
        self.b85 = QtWidgets.QTextEdit(self.centralwidget)
        self.b85.setGeometry(QtCore.QRect(290, 500, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b85.setFont(font)
        self.b85.setObjectName("b85")
        self.b86 = QtWidgets.QTextEdit(self.centralwidget)
        self.b86.setGeometry(QtCore.QRect(360, 500, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b86.setFont(font)
        self.b86.setLineWrapColumnOrWidth(-1)
        self.b86.setObjectName("b86")
        self.b62 = QtWidgets.QTextEdit(self.centralwidget)
        self.b62.setGeometry(QtCore.QRect(80, 360, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b62.setFont(font)
        self.b62.setObjectName("b62")
        self.b55 = QtWidgets.QTextEdit(self.centralwidget)
        self.b55.setGeometry(QtCore.QRect(290, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b55.setFont(font)
        self.b55.setObjectName("b55")
        self.b51 = QtWidgets.QTextEdit(self.centralwidget)
        self.b51.setGeometry(QtCore.QRect(10, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b51.setFont(font)
        self.b51.setObjectName("b51")
        self.b61 = QtWidgets.QTextEdit(self.centralwidget)
        self.b61.setGeometry(QtCore.QRect(10, 360, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b61.setFont(font)
        self.b61.setObjectName("b61")
        self.Solve = QtWidgets.QPushButton(self.centralwidget)
        self.Solve.setGeometry(QtCore.QRect(250, 630, 131, 51))
        self.Solve.setObjectName("Solve")
        self.b66 = QtWidgets.QTextEdit(self.centralwidget)
        self.b66.setGeometry(QtCore.QRect(360, 360, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b66.setFont(font)
        self.b66.setObjectName("b66")
        self.b88 = QtWidgets.QTextEdit(self.centralwidget)
        self.b88.setGeometry(QtCore.QRect(500, 500, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b88.setFont(font)
        self.b88.setObjectName("b88")
        self.b91 = QtWidgets.QTextEdit(self.centralwidget)
        self.b91.setGeometry(QtCore.QRect(10, 570, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b91.setFont(font)
        self.b91.setObjectName("b91")
        self.b97 = QtWidgets.QTextEdit(self.centralwidget)
        self.b97.setGeometry(QtCore.QRect(430, 570, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b97.setFont(font)
        self.b97.setObjectName("b97")
        self.b99 = QtWidgets.QTextEdit(self.centralwidget)
        self.b99.setGeometry(QtCore.QRect(570, 570, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b99.setFont(font)
        self.b99.setObjectName("b99")
        self.b96 = QtWidgets.QTextEdit(self.centralwidget)
        self.b96.setGeometry(QtCore.QRect(360, 570, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b96.setFont(font)
        self.b96.setObjectName("b96")
        self.b93 = QtWidgets.QTextEdit(self.centralwidget)
        self.b93.setGeometry(QtCore.QRect(150, 570, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b93.setFont(font)
        self.b93.setObjectName("b93")
        self.b94 = QtWidgets.QTextEdit(self.centralwidget)
        self.b94.setGeometry(QtCore.QRect(220, 570, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b94.setFont(font)
        self.b94.setObjectName("b94")
        self.b95 = QtWidgets.QTextEdit(self.centralwidget)
        self.b95.setGeometry(QtCore.QRect(290, 570, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b95.setFont(font)
        self.b95.setObjectName("b95")
        self.b98 = QtWidgets.QTextEdit(self.centralwidget)
        self.b98.setGeometry(QtCore.QRect(500, 570, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b98.setFont(font)
        self.b98.setObjectName("b98")
        self.b92 = QtWidgets.QTextEdit(self.centralwidget)
        self.b92.setGeometry(QtCore.QRect(80, 570, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.b92.setFont(font)
        self.b92.setObjectName("b92")
        self.line2 = QtWidgets.QFrame(self.centralwidget)
        self.line2.setGeometry(QtCore.QRect(410, 10, 16, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line2.sizePolicy().hasHeightForWidth())
        self.line2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(41)
        font.setBold(True)
        font.setWeight(75)
        self.line2.setFont(font)
        self.line2.setLineWidth(5)
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.line3 = QtWidgets.QFrame(self.centralwidget)
        self.line3.setGeometry(QtCore.QRect(0, 200, 621, 16))
        self.line3.setLineWidth(5)
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        self.line4 = QtWidgets.QFrame(self.centralwidget)
        self.line4.setGeometry(QtCore.QRect(10, 410, 621, 16))
        self.line4.setLineWidth(5)
        self.line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line4.setObjectName("line4")
        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(200, 10, 16, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line1.sizePolicy().hasHeightForWidth())
        self.line1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(41)
        font.setBold(True)
        font.setWeight(75)
        self.line1.setFont(font)
        self.line1.setLineWidth(5)
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Solve.clicked.connect(self.MatrixPrint)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b11.setPlaceholderText(_translate("MainWindow", "0"))
        self.b12.setPlaceholderText(_translate("MainWindow", "0"))
        self.b13.setPlaceholderText(_translate("MainWindow", "0"))
        self.b15.setPlaceholderText(_translate("MainWindow", "0"))
        self.b14.setPlaceholderText(_translate("MainWindow", "0"))
        self.b16.setPlaceholderText(_translate("MainWindow", "0"))
        self.b18.setPlaceholderText(_translate("MainWindow", "0"))
        self.b17.setPlaceholderText(_translate("MainWindow", "0"))
        self.b19.setPlaceholderText(_translate("MainWindow", "0"))
        self.b25.setPlaceholderText(_translate("MainWindow", "0"))
        self.b28.setPlaceholderText(_translate("MainWindow", "0"))
        self.b27.setPlaceholderText(_translate("MainWindow", "0"))
        self.b26.setPlaceholderText(_translate("MainWindow", "0"))
        self.b22.setPlaceholderText(_translate("MainWindow", "0"))
        self.b21.setPlaceholderText(_translate("MainWindow", "0"))
        self.b23.setPlaceholderText(_translate("MainWindow", "0"))
        self.b24.setPlaceholderText(_translate("MainWindow", "0"))
        self.b29.setPlaceholderText(_translate("MainWindow", "0"))
        self.b44.setPlaceholderText(_translate("MainWindow", "0"))
        self.b43.setPlaceholderText(_translate("MainWindow", "0"))
        self.b39.setPlaceholderText(_translate("MainWindow", "0"))
        self.b33.setPlaceholderText(_translate("MainWindow", "0"))
        self.b48.setPlaceholderText(_translate("MainWindow", "0"))
        self.b37.setPlaceholderText(_translate("MainWindow", "0"))
        self.b49.setPlaceholderText(_translate("MainWindow", "0"))
        self.b38.setPlaceholderText(_translate("MainWindow", "0"))
        self.b47.setPlaceholderText(_translate("MainWindow", "0"))
        self.b34.setPlaceholderText(_translate("MainWindow", "0"))
        self.b45.setPlaceholderText(_translate("MainWindow", "0"))
        self.b36.setPlaceholderText(_translate("MainWindow", "0"))
        self.b32.setPlaceholderText(_translate("MainWindow", "0"))
        self.b42.setPlaceholderText(_translate("MainWindow", "0"))
        self.b35.setPlaceholderText(_translate("MainWindow", "0"))
        self.b31.setPlaceholderText(_translate("MainWindow", "0"))
        self.b41.setPlaceholderText(_translate("MainWindow", "0"))
        self.b46.setPlaceholderText(_translate("MainWindow", "0"))
        self.b64.setPlaceholderText(_translate("MainWindow", "0"))
        self.b63.setPlaceholderText(_translate("MainWindow", "0"))
        self.b76.setPlaceholderText(_translate("MainWindow", "0"))
        self.b78.setPlaceholderText(_translate("MainWindow", "0"))
        self.b79.setPlaceholderText(_translate("MainWindow", "0"))
        self.b59.setPlaceholderText(_translate("MainWindow", "0"))
        self.b82.setPlaceholderText(_translate("MainWindow", "0"))
        self.b83.setPlaceholderText(_translate("MainWindow", "0"))
        self.b75.setPlaceholderText(_translate("MainWindow", "0"))
        self.b53.setPlaceholderText(_translate("MainWindow", "0"))
        self.b68.setPlaceholderText(_translate("MainWindow", "0"))
        self.b57.setPlaceholderText(_translate("MainWindow", "0"))
        self.b71.setPlaceholderText(_translate("MainWindow", "0"))
        self.b69.setPlaceholderText(_translate("MainWindow", "0"))
        self.b87.setPlaceholderText(_translate("MainWindow", "0"))
        self.b58.setPlaceholderText(_translate("MainWindow", "0"))
        self.b84.setPlaceholderText(_translate("MainWindow", "0"))
        self.b72.setPlaceholderText(_translate("MainWindow", "0"))
        self.b81.setPlaceholderText(_translate("MainWindow", "0"))
        self.b67.setPlaceholderText(_translate("MainWindow", "0"))
        self.b74.setPlaceholderText(_translate("MainWindow", "0"))
        self.b54.setPlaceholderText(_translate("MainWindow", "0"))
        self.b65.setPlaceholderText(_translate("MainWindow", "0"))
        self.b89.setPlaceholderText(_translate("MainWindow", "0"))
        self.b73.setPlaceholderText(_translate("MainWindow", "0"))
        self.b56.setPlaceholderText(_translate("MainWindow", "0"))
        self.b52.setPlaceholderText(_translate("MainWindow", "0"))
        self.b77.setPlaceholderText(_translate("MainWindow", "0"))
        self.b85.setPlaceholderText(_translate("MainWindow", "0"))
        self.b86.setPlaceholderText(_translate("MainWindow", "0"))
        self.b62.setPlaceholderText(_translate("MainWindow", "0"))
        self.b55.setPlaceholderText(_translate("MainWindow", "0"))
        self.b51.setPlaceholderText(_translate("MainWindow", "0"))
        self.b61.setPlaceholderText(_translate("MainWindow", "0"))
        self.Solve.setText(_translate("MainWindow", "Solve"))
        self.b66.setPlaceholderText(_translate("MainWindow", "0"))
        self.b88.setPlaceholderText(_translate("MainWindow", "0"))
        self.b91.setPlaceholderText(_translate("MainWindow", "0"))
        self.b97.setPlaceholderText(_translate("MainWindow", "0"))
        self.b99.setPlaceholderText(_translate("MainWindow", "0"))
        self.b96.setPlaceholderText(_translate("MainWindow", "0"))
        self.b93.setPlaceholderText(_translate("MainWindow", "0"))
        self.b94.setPlaceholderText(_translate("MainWindow", "0"))
        self.b95.setPlaceholderText(_translate("MainWindow", "0"))
        self.b98.setPlaceholderText(_translate("MainWindow", "0"))
        self.b92.setPlaceholderText(_translate("MainWindow", "0"))
        
        
        
    def MatrixPrint(self):
        if len(str(self.b11.toPlainText())) == 0:
            b11 = 0 
        else:
            b11 =int(self.b11.toPlainText()) 
            
        if len(str(self.b12.toPlainText())) == 0:
            b12 = 0 
        else:
            b12 =int(self.b12.toPlainText()) 
            
        if len(str(self.b13.toPlainText())) == 0:
            b13 = 0 
        else:
            b13 =int(self.b13.toPlainText())   
            
        if len(str(self.b14.toPlainText())) == 0:
            b14 = 0 
        else:
            b14 =int(self.b14.toPlainText()) 
            
        if len(str(self.b15.toPlainText())) == 0:
            b15 = 0 
        else:
            b15 =int(self.b15.toPlainText()) 
            
        if len(str(self.b16.toPlainText())) == 0:
            b16 = 0 
        else:
            b16 =int(self.b16.toPlainText()) 
            
        if len(str(self.b17.toPlainText())) == 0:
            b17 = 0 
        else:
            b17 =int(self.b17.toPlainText())   
            
        if len(str(self.b18.toPlainText())) == 0:
            b18 = 0 
        else:
            b18 =int(self.b18.toPlainText()) 
            
        if len(str(self.b19.toPlainText())) == 0:
            b19 = 0 
        else:
            b19 =int(self.b19.toPlainText())     
        
        # print(b11,b12,b13,b14,b15,b16,b17,b18,b19)    
       
        
       
        if len(str(self.b21.toPlainText())) == 0:
            b21 = 0 
        else:
            b21 =int(self.b21.toPlainText()) 
            
        if len(str(self.b22.toPlainText())) == 0:
            b22 = 0 
        else:
            b22 =int(self.b22.toPlainText()) 
            
        if len(str(self.b23.toPlainText())) == 0:
            b23 = 0 
        else:
            b23 =int(self.b23.toPlainText())   
            
        if len(str(self.b24.toPlainText())) == 0:
            b24 = 0 
        else:
            b24 =int(self.b24.toPlainText()) 
            
        if len(str(self.b25.toPlainText())) == 0:
            b25 = 0 
        else:
            b25 =int(self.b25.toPlainText()) 
            
        if len(str(self.b26.toPlainText())) == 0:
            b26 = 0 
        else:
            b26 =int(self.b26.toPlainText()) 
            
        if len(str(self.b27.toPlainText())) == 0:
            b27 = 0 
        else:
            b27 =int(self.b27.toPlainText())   
            
        if len(str(self.b28.toPlainText())) == 0:
            b28 = 0 
        else:
            b28 =int(self.b28.toPlainText()) 
            
        if len(str(self.b29.toPlainText())) == 0:
            b29 = 0 
        else:
            b29 =int(self.b29.toPlainText())     
        
        # print(b21,b22,b23,b24,b25,b26,b27,b28,b29)
        
        
        if len(str(self.b31.toPlainText())) == 0:
            b31 = 0 
        else:
            b31 =int(self.b31.toPlainText()) 
            
        if len(str(self.b32.toPlainText())) == 0:
            b32 = 0 
        else:
            b32 =int(self.b32.toPlainText()) 
            
        if len(str(self.b33.toPlainText())) == 0:
            b33 = 0 
        else:
            b33 =int(self.b33.toPlainText())   
            
        if len(str(self.b34.toPlainText())) == 0:
            b34 = 0 
        else:
            b34 =int(self.b34.toPlainText()) 
            
        if len(str(self.b35.toPlainText())) == 0:
            b35 = 0 
        else:
            b35 =int(self.b35.toPlainText()) 
            
        if len(str(self.b36.toPlainText())) == 0:
            b36 = 0 
        else:
            b36 =int(self.b36.toPlainText()) 
            
        if len(str(self.b37.toPlainText())) == 0:
            b37 = 0 
        else:
            b37 =int(self.b37.toPlainText())   
            
        if len(str(self.b38.toPlainText())) == 0:
            b38 = 0 
        else:
            b38 =int(self.b38.toPlainText()) 
            
        if len(str(self.b39.toPlainText())) == 0:
            b39 = 0 
        else:
            b39 =int(self.b39.toPlainText())     
        
        # print(b31,b32,b33,b34,b35,b36,b37,b38,b39)
        
        
        if len(str(self.b41.toPlainText())) == 0:
            b41 = 0 
        else:
            b41 =int(self.b41.toPlainText()) 
            
        if len(str(self.b42.toPlainText())) == 0:
            b42 = 0 
        else:
            b42 =int(self.b42.toPlainText()) 
            
        if len(str(self.b43.toPlainText())) == 0:
            b43 = 0 
        else:
            b43 =int(self.b43.toPlainText())   
            
        if len(str(self.b44.toPlainText())) == 0:
            b44 = 0 
        else:
            b44 =int(self.b44.toPlainText()) 
            
        if len(str(self.b45.toPlainText())) == 0:
            b45 = 0 
        else:
            b45 =int(self.b45.toPlainText()) 
            
        if len(str(self.b46.toPlainText())) == 0:
            b46 = 0 
        else:
            b46 =int(self.b46.toPlainText()) 
            
        if len(str(self.b47.toPlainText())) == 0:
            b47 = 0 
        else:
            b47 =int(self.b47.toPlainText())   
            
        if len(str(self.b48.toPlainText())) == 0:
            b48 = 0 
        else:
            b48 =int(self.b48.toPlainText()) 
            
        if len(str(self.b49.toPlainText())) == 0:
            b49 = 0 
        else:
            b49 =int(self.b49.toPlainText())     
        
        # print(b41,b42,b43,b44,b45,b46,b47,b48,b49) 
        
        
        if len(str(self.b51.toPlainText())) == 0:
            b51 = 0 
        else:
            b51 =int(self.b51.toPlainText()) 
            
        if len(str(self.b52.toPlainText())) == 0:
            b52 = 0 
        else:
            b52 =int(self.b52.toPlainText()) 
            
        if len(str(self.b53.toPlainText())) == 0:
            b53 = 0 
        else:
            b53 =int(self.b53.toPlainText())   
            
        if len(str(self.b54.toPlainText())) == 0:
            b54 = 0 
        else:
            b54 =int(self.b54.toPlainText()) 
            
        if len(str(self.b55.toPlainText())) == 0:
            b55 = 0 
        else:
            b55 =int(self.b55.toPlainText()) 
            
        if len(str(self.b56.toPlainText())) == 0:
            b56 = 0 
        else:
            b56 =int(self.b56.toPlainText()) 
            
        if len(str(self.b57.toPlainText())) == 0:
            b57 = 0 
        else:
            b57 =int(self.b57.toPlainText())   
            
        if len(str(self.b58.toPlainText())) == 0:
            b58 = 0 
        else:
            b58 =int(self.b58.toPlainText()) 
            
        if len(str(self.b59.toPlainText())) == 0:
            b59 = 0 
        else:
            b59 =int(self.b59.toPlainText())     
        
        # print(b51,b52,b53,b54,b55,b56,b57,b58,b59)
        
        
        if len(str(self.b61.toPlainText())) == 0:
            b61 = 0 
        else:
            b61 =int(self.b61.toPlainText()) 
            
        if len(str(self.b62.toPlainText())) == 0:
            b62 = 0 
        else:
            b62 =int(self.b62.toPlainText()) 
            
        if len(str(self.b63.toPlainText())) == 0:
            b63 = 0 
        else:
            b63 =int(self.b63.toPlainText())   
            
        if len(str(self.b64.toPlainText())) == 0:
            b64 = 0 
        else:
            b64 =int(self.b64.toPlainText()) 
            
        if len(str(self.b65.toPlainText())) == 0:
            b65 = 0 
        else:
            b65 =int(self.b65.toPlainText()) 
            
        if len(str(self.b66.toPlainText())) == 0:
            b66 = 0 
        else:
            b66 =int(self.b66.toPlainText()) 
            
        if len(str(self.b67.toPlainText())) == 0:
            b67 = 0 
        else:
            b67 =int(self.b67.toPlainText())   
            
        if len(str(self.b68.toPlainText())) == 0:
            b68 = 0 
        else:
            b68 =int(self.b68.toPlainText()) 
            
        if len(str(self.b69.toPlainText())) == 0:
            b69 = 0 
        else:
            b69 =int(self.b69.toPlainText())     
        
        # print(b61,b62,b63,b64,b65,b66,b67,b68,b69)
        
        
        if len(str(self.b71.toPlainText())) == 0:
            b71 = 0 
        else:
            b71 =int(self.b71.toPlainText()) 
            
        if len(str(self.b72.toPlainText())) == 0:
            b72 = 0 
        else:
            b72 =int(self.b72.toPlainText()) 
            
        if len(str(self.b73.toPlainText())) == 0:
            b73 = 0 
        else:
            b73 =int(self.b73.toPlainText())   
            
        if len(str(self.b74.toPlainText())) == 0:
            b74 = 0 
        else:
            b74 =int(self.b74.toPlainText()) 
            
        if len(str(self.b75.toPlainText())) == 0:
            b75 = 0 
        else:
            b75 =int(self.b75.toPlainText()) 
            
        if len(str(self.b76.toPlainText())) == 0:
            b76 = 0 
        else:
            b76 =int(self.b76.toPlainText()) 
            
        if len(str(self.b77.toPlainText())) == 0:
            b77 = 0 
        else:
            b77 =int(self.b77.toPlainText())   
            
        if len(str(self.b78.toPlainText())) == 0:
            b78 = 0 
        else:
            b78 =int(self.b78.toPlainText()) 
            
        if len(str(self.b79.toPlainText())) == 0:
            b79 = 0 
        else:
            b79 =int(self.b79.toPlainText())     
        
        # print(b71,b72,b73,b74,b75,b76,b77,b78,b79) 
        
        
        if len(str(self.b81.toPlainText())) == 0:
            b81 = 0 
        else:
            b81 =int(self.b81.toPlainText()) 
            
        if len(str(self.b82.toPlainText())) == 0:
            b82 = 0 
        else:
            b82 =int(self.b82.toPlainText()) 
            
        if len(str(self.b83.toPlainText())) == 0:
            b83 = 0 
        else:
            b83 =int(self.b83.toPlainText())   
            
        if len(str(self.b84.toPlainText())) == 0:
            b84 = 0 
        else:
            b84 =int(self.b84.toPlainText()) 
            
        if len(str(self.b85.toPlainText())) == 0:
            b85 = 0 
        else:
            b85 =int(self.b85.toPlainText()) 
            
        if len(str(self.b86.toPlainText())) == 0:
            b86 = 0 
        else:
            b86 =int(self.b86.toPlainText()) 
            
        if len(str(self.b87.toPlainText())) == 0:
            b87 = 0 
        else:
            b87 =int(self.b87.toPlainText())   
            
        if len(str(self.b88.toPlainText())) == 0:
            b88 = 0 
        else:
            b88 =int(self.b88.toPlainText()) 
            
        if len(str(self.b89.toPlainText())) == 0:
            b89 = 0 
        else:
            b89 =int(self.b89.toPlainText())     
        
        # print(b81,b82,b83,b84,b85,b86,b87,b88,b89) 
        
        
        
        if len(str(self.b91.toPlainText())) == 0:
            b91 = 0 
        else:
            b91 =int(self.b91.toPlainText()) 
            
        if len(str(self.b92.toPlainText())) == 0:
            b92 = 0 
        else:
            b92 =int(self.b92.toPlainText()) 
            
        if len(str(self.b93.toPlainText())) == 0:
            b93 = 0 
        else:
            b93 =int(self.b93.toPlainText())   
            
        if len(str(self.b94.toPlainText())) == 0:
            b94 = 0 
        else:
            b94 =int(self.b94.toPlainText()) 
            
        if len(str(self.b95.toPlainText())) == 0:
            b95 = 0 
        else:
            b95 =int(self.b95.toPlainText()) 
            
        if len(str(self.b96.toPlainText())) == 0:
            b96 = 0 
        else:
            b96 =int(self.b96.toPlainText()) 
            
        if len(str(self.b97.toPlainText())) == 0:
            b97 = 0 
        else:
            b97 =int(self.b97.toPlainText())   
            
        if len(str(self.b98.toPlainText())) == 0:
            b98 = 0 
        else:
            b98 =int(self.b98.toPlainText()) 
            
        if len(str(self.b99.toPlainText())) == 0:
            b99 = 0 
        else:
            b99 =int(self.b99.toPlainText())     
        
        # print(b91,b92,b93,b94,b95,b96,b97,b98,b99) 
        
        
        Sudoku = [[b11,b12,b13,b14,b15,b16,b17,b18,b19],
                  [b21,b22,b23,b24,b25,b26,b27,b28,b29],
                  [b31,b32,b33,b34,b35,b36,b37,b38,b39],
                  [b41,b42,b43,b44,b45,b46,b47,b48,b49],
                  [b51,b52,b53,b54,b55,b56,b57,b58,b59],
                  [b61,b62,b63,b64,b65,b66,b67,b68,b69],
                  [b71,b72,b73,b74,b75,b76,b77,b78,b79],
                  [b81,b82,b83,b84,b85,b86,b87,b88,b89],
                  [b91,b92,b93,b94,b95,b96,b97,b98,b99]]

        print(np.matrix(Sudoku))
        
         
        
        def possible(y,x,n):
            # global Sudoku
            for i in range(0,9):
                if Sudoku[y][i] == n:
                    return False
            for i in range(0,9):
                if Sudoku[i][x] == n:
                    return False   
            x0 = (x//3)*3
            y0 = (y//3)*3    
            for i in range(0,3):
                for j in range (0,3):
                    if Sudoku[y0+i][x0+j] == n:
                        return False          
            return True
        
        def solver(self):
            # global Sudoku
            for y in range(9):
                for x in range(9):
                    if Sudoku[y][x] == 0:
                        for n in range (1,10):
                            if possible(y,x,n):
                                Sudoku[y][x] = n
                                solver(self)
                                Sudoku[y][x] = 0
                        return
            print("The solution : \n")
            print(np.matrix(Sudoku))
            # print(Sudoku[1][1])
            
            self.b11.setText(str(Sudoku[0][0]))
            self.b12.setText(str(Sudoku[0][1]))
            self.b13.setText(str(Sudoku[0][2]))
            self.b14.setText(str(Sudoku[0][3]))
            self.b15.setText(str(Sudoku[0][4]))
            self.b16.setText(str(Sudoku[0][5]))
            self.b17.setText(str(Sudoku[0][6]))
            self.b18.setText(str(Sudoku[0][7]))
            self.b19.setText(str(Sudoku[0][8]))
            
            self.b21.setText(str(Sudoku[1][0]))
            self.b22.setText(str(Sudoku[1][1]))
            self.b23.setText(str(Sudoku[1][2]))
            self.b24.setText(str(Sudoku[1][3]))
            self.b25.setText(str(Sudoku[1][4]))
            self.b26.setText(str(Sudoku[1][5]))
            self.b27.setText(str(Sudoku[1][6]))
            self.b28.setText(str(Sudoku[1][7]))
            self.b29.setText(str(Sudoku[1][8]))
            
            self.b31.setText(str(Sudoku[2][0]))
            self.b32.setText(str(Sudoku[2][1]))
            self.b33.setText(str(Sudoku[2][2]))
            self.b34.setText(str(Sudoku[2][3]))
            self.b35.setText(str(Sudoku[2][4]))
            self.b36.setText(str(Sudoku[2][5]))
            self.b37.setText(str(Sudoku[2][6]))
            self.b38.setText(str(Sudoku[2][7]))
            self.b39.setText(str(Sudoku[2][8]))
            
            self.b41.setText(str(Sudoku[3][0]))
            self.b42.setText(str(Sudoku[3][1]))
            self.b43.setText(str(Sudoku[3][2]))
            self.b44.setText(str(Sudoku[3][3]))
            self.b45.setText(str(Sudoku[3][4]))
            self.b46.setText(str(Sudoku[3][5]))
            self.b47.setText(str(Sudoku[3][6]))
            self.b48.setText(str(Sudoku[3][7]))
            self.b49.setText(str(Sudoku[3][8]))
            
            self.b51.setText(str(Sudoku[4][0]))
            self.b52.setText(str(Sudoku[4][1]))
            self.b53.setText(str(Sudoku[4][2]))
            self.b54.setText(str(Sudoku[4][3]))
            self.b55.setText(str(Sudoku[4][4]))
            self.b56.setText(str(Sudoku[4][5]))
            self.b57.setText(str(Sudoku[4][6]))
            self.b58.setText(str(Sudoku[4][7]))
            self.b59.setText(str(Sudoku[4][8]))
            
            self.b61.setText(str(Sudoku[5][0]))
            self.b62.setText(str(Sudoku[5][1]))
            self.b63.setText(str(Sudoku[5][2]))
            self.b64.setText(str(Sudoku[5][3]))
            self.b65.setText(str(Sudoku[5][4]))
            self.b66.setText(str(Sudoku[5][5]))
            self.b67.setText(str(Sudoku[5][6]))
            self.b68.setText(str(Sudoku[5][7]))
            self.b69.setText(str(Sudoku[5][8]))
            
            self.b71.setText(str(Sudoku[6][0]))
            self.b72.setText(str(Sudoku[6][1]))
            self.b73.setText(str(Sudoku[6][2]))
            self.b74.setText(str(Sudoku[6][3]))
            self.b75.setText(str(Sudoku[6][4]))
            self.b76.setText(str(Sudoku[6][5]))
            self.b77.setText(str(Sudoku[6][6]))
            self.b78.setText(str(Sudoku[6][7]))
            self.b79.setText(str(Sudoku[6][8]))
            
            self.b81.setText(str(Sudoku[7][0]))
            self.b82.setText(str(Sudoku[7][1]))
            self.b83.setText(str(Sudoku[7][2]))
            self.b84.setText(str(Sudoku[7][3]))
            self.b85.setText(str(Sudoku[7][4]))
            self.b86.setText(str(Sudoku[7][5]))
            self.b87.setText(str(Sudoku[7][6]))
            self.b88.setText(str(Sudoku[7][7]))
            self.b89.setText(str(Sudoku[7][8]))
            
            self.b91.setText(str(Sudoku[8][0]))
            self.b92.setText(str(Sudoku[8][1]))
            self.b93.setText(str(Sudoku[8][2]))
            self.b94.setText(str(Sudoku[8][3]))
            self.b95.setText(str(Sudoku[8][4]))
            self.b96.setText(str(Sudoku[8][5]))
            self.b97.setText(str(Sudoku[8][6]))
            self.b98.setText(str(Sudoku[8][7]))
            self.b99.setText(str(Sudoku[8][8]))
            # input("Any other Soulutions?")
            
            return
        
        solver(self)
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

