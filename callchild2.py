from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from child2 import Ui_Form2
import sys
import requests

class MainWindow(QMainWindow, Ui_Form2):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.queryBtn.clicked.connect(self.queryinfo)
        self.clearBtn.clicked.connect(self.clearinfo)
    def clearinfo(self):
        self.label_2.setText('请选择对应条件进行查询')

    def queryinfo(self):
        # self.spider()   # 先跑一边爬虫 将需要的图片爬下来
        title = self.comboBox.currentText()
        if title == '全国24小时最高温分布':
            filename = './img/1.jpg'
            img = QImage(filename)
            result = img.scaled(self.label_2.width(), self.label_2.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            # 在标签控件上显示图片
            self.label_2.setPixmap(QPixmap.fromImage(result))
        elif title == '全国24小时最低温分布':
            filename = './img/2.jpg'
            img = QImage(filename)
            result = img.scaled(self.label_2.width(), self.label_2.height(), Qt.IgnoreAspectRatio,
                                Qt.SmoothTransformation)
            # 在标签控件上显示图片
            self.label_2.setPixmap(QPixmap.fromImage(result))
        elif title == '全国24小时降水量分布':
            filename = './img/3.jpg'
            img = QImage(filename)
            result = img.scaled(self.label_2.width(), self.label_2.height(), Qt.IgnoreAspectRatio,
                                Qt.SmoothTransformation)
            # 在标签控件上显示图片
            self.label_2.setPixmap(QPixmap.fromImage(result))
        elif title == '全国24小时平均气温分布':
            filename = './img/4.jpg'
            img = QImage(filename)
            result = img.scaled(self.label_2.width(), self.label_2.height(), Qt.IgnoreAspectRatio,
                                Qt.SmoothTransformation)
            # 在标签控件上显示图片
            self.label_2.setPixmap(QPixmap.fromImage(result))

    def graph_save(response, name):
        with open("./img/{}.jpg".format(name), 'wb') as f:
            f.write(response.content)  # 把图片内容写入


    def spider(self):
        i = 0
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        url_high_wendu = 'http://pi.weather.com.cn/i/product/share/pic/l/PWCP_TWC_STFC_S99_ETM_TWC_L88_P9_20190320120000000.JPG'
        url_low_wendu = 'http://pi.weather.com.cn/i/product/share/pic/l/PWCP_TWC_STFC_S99_ETN_TWC_L88_P9_20190320120000000.JPG'
        url_jiangshuiliang = 'http://pi.weather.com.cn/i/product/share/pic/l/PWCP_TWC_WEAP_SFER_EEO_TWC_L88_P9_20190320050000000.JPG'
        url_mean_wendu = 'http://products.weather.com.cn/product/Index/index/procode/JC_WD_PJ.shtml'

        response1 = requests.get(url_high_wendu, headers=headers)
        name = '1'
        self.graph_save(response1, name)
        response2 = requests.get(url_low_wendu, headers=headers)
        name = '2'
        self.graph_save(response2, name)

        response3 = requests.get(url_jiangshuiliang, headers=headers)
        name = '3'
        self.graph_save(response3, name)

        response4 = requests.get(url_mean_wendu, headers=headers)
        name = '4'
        self.graph_save(response4, name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
