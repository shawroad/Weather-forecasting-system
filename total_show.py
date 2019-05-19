from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from total import Ui_Form
import sys
import os


class WinForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(WinForm, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.zaixian)
        self.pushButton_2.clicked.connect(self.lixian)

    def zaixian(self):
        os.system('python callweather.py')

    def lixian(self):
        os.system('python 001-offline查询天气.py')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.setObjectName("MainWindow")  # 为主窗口设置对象名 为了在下面设置背景颜色
    win.setStyleSheet("#MainWindow{border-image:url(./img/total.jpg);}")
    win.show()
    sys.exit(app.exec_())
