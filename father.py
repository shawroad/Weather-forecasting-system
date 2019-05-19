# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'father.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 820, 620))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.searchWeather = QtWidgets.QAction(MainWindow)
        self.searchWeather.setObjectName("searchWeather")
        self.WorldWeather = QtWidgets.QAction(MainWindow)
        self.WorldWeather.setObjectName("WorldWeather")
        self.sanWeather = QtWidgets.QAction(MainWindow)
        self.sanWeather.setObjectName("sanWeather")
        self.kongqisort = QtWidgets.QAction(MainWindow)
        self.kongqisort.setObjectName("kongqisort")
        self.kongqibiaozhun = QtWidgets.QAction(MainWindow)
        self.kongqibiaozhun.setObjectName("kongqibiaozhun")

        self.menu.addAction(self.searchWeather)
        self.menu.addAction(self.WorldWeather)
        self.menu.addAction(self.sanWeather)
        self.menu_2.addAction(self.kongqisort)
        self.menu_2.addAction(self.kongqibiaozhun)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "切换查询方式"))
        self.menu_2.setTitle(_translate("MainWindow", "空气质量查询"))
        self.searchWeather.setText(_translate("MainWindow", "天气预报查询"))
        self.searchWeather.setToolTip(_translate("MainWindow", "天气预报查询"))
        self.searchWeather.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.WorldWeather.setText(_translate("MainWindow", "全国气温查询"))
        self.WorldWeather.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.sanWeather.setText(_translate("MainWindow", "查询三天天气"))
        self.sanWeather.setToolTip(_translate("MainWindow", "查询三天天气"))
        self.sanWeather.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.kongqisort.setText(_translate("MainWindow", "空气质量排名"))
        self.kongqisort.setToolTip(_translate("MainWindow", "空气质量排名"))
        self.kongqisort.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.kongqibiaozhun.setText(_translate("MainWindow", "空气质量标准"))
        self.kongqibiaozhun.setToolTip(_translate("MainWindow", "空气质量标准"))
        self.kongqibiaozhun.setShortcut(_translate("MainWindow", "Ctrl+G"))

