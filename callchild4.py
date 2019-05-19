import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from child4 import Ui_Form4
from lxml import etree
import sys


class WinForm(QMainWindow, Ui_Form4):
    def __init__(self, parent=None):
        super(WinForm, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showinfo)


    def showinfo(self):
        info = self.spider()
        str = ''
        for item in info:
            str += item[0] + '\t' + item[1] + '\t' + item[2] + '\t' + item[3] + '\n'
        self.textEdit.setText(str)


    def spider(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        url = 'https://www.tianqi.com/air/'
        response = requests.get(url, headers=headers)
        selector = etree.HTML(response.text)
        all_li = selector.xpath('//*[@class="main-unit"]/div[2]/ul/li')

        title1 = all_li[0].xpath('span[1]/text()')[0]
        title2 = all_li[0].xpath('span[2]/text()')[0]
        title3 = all_li[0].xpath('span[3]/i/text()')[0]
        title4 = all_li[0].xpath('span[4]/text()')[0]

        title = [title1, title2, title3, title4]

        info = []
        info.append(title)
        all_li.remove(all_li[0])  # 将第一个li标签删除掉，后面的统一处理
        for li in all_li:
            mingzi = li.xpath("span[1]/text()")[0]
            city = li.xpath("span[2]/a/text()")[0]
            index = li.xpath("span[3]/text()")[0]
            degree = li.xpath("span[4]/em/text()")[0]
            temp = [mingzi, city, index, degree]

            info.append(temp)
        return info
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
