import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from child1 import Ui_Form
import requests
from PyQt5.QtGui import QIcon
from xpinyin import Pinyin
from lxml import etree

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.clearBtn.clicked.connect(self.clearResult)
        self.ui.queryBtn.clicked.connect(self.queryWeather)

        # 设置程序的图标和名字
        self.setWindowTitle('天气预报的查询')
        self.setWindowIcon(QIcon('./img/sign.ico'))


    def queryWeather(self):
        print("天气查询。。。")
        # 获取当前选择的文本内容
        cityName = self.ui.weatherComboBox_2.currentText()
        # 将文本内容转换为拼音
        pinyin = self.hanzi2pinyin(cityName)

        content = self.spider(pinyin)

        self.ui.resultText_2.setText(content)

    def hanzi2pinyin(self, city):
        pin = Pinyin()
        temp_pin = pin.get_pinyin(city)
        pin = temp_pin.replace('-', '')
        return pin

    def spider(self, pin):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        url = 'http://www.tianqi2345.com/yubao/{}.htm'
        response = requests.get(url.format(pin), headers=headers)
        selector = etree.HTML(response.text)

        msg1 = "城市: " + self.ui.weatherComboBox_2.currentText() + '\n'
        # msg2 = "日期: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0] + '\n'
        # msg3 = "天气: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[2]')[0] + '\n'
        # msg4 = "温度: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[3]')[0] + '\n'

        time = "日期: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0]
        weather ="天气:" + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[2]')[0]
        temper = "温度:" + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[3]')[0]


        content = msg1+ '\n' + time + '\n' + weather + '\n' + temper

        return content

    
    def clearResult(self):
        print('清除文本框。。。')
        self.ui.resultText_2.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.setObjectName("MainWindow")  # 为主窗口设置对象名 为了在下面设置背景颜色
    win.setStyleSheet("#MainWindow{border-image:url(./img/weather.jpg);}")  # 这个图片路径是我自己的，你可以这一张你自己的图片。或者把这两行都给注释掉
    win.show()
    sys.exit(app.exec_())

