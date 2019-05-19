import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests
from PyQt5.QtGui import QIcon
from child3 import Ui_Form3
from lxml import etree
from xpinyin import Pinyin

class MainWindow(QMainWindow, Ui_Form3):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.findBtn.clicked.connect(self.findinfo)
        self.clearBtn.clicked.connect(self.clearinfo)

    def findinfo(self):

        text = self.lineEdit.text()
        print(text)
        pin = self.hanzi2pinyin(text)
        print(pin)
        content = self.spider(pin)

        self.textEdit_1.setText(content[0])
        self.textEdit_2.setText(content[1])
        self.textEdit_3.setText(content[2])


    def clearinfo(self):
        self.textEdit_1.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()

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

        # 当天
        time1 = selector.xpath('//*[@id="weather"]/div[1]/div[1]/strong/text()')[0]
        time2 = selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0]
        #//*[@id="weather"]/div[1]/div[1]/string(br[1])
        weather = selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[2]')[0]
        temper = selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[3]')[0]
        item1 = time1 + '\n' + time2 + '\n' + weather + '\n' + temper + '\n'



        # 明天
        time21 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/strong/text()')[0]
        time22 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[1]')[0]
        weather2 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[2]')[0]
        temper2 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[3]')[0]
        clody2 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[4]')[0]
        item2 = time21 + '\n' + time22 + '\n' + weather2 + '\n' + temper2 + '\n' + clody2 + '\n'

        # 后天
        time31 = selector.xpath('//*[@id="weather"]/div[1]/div[3]/strong/text()')[0]
        time32 = selector.xpath('//*[@id="weather"]/div[1]/div[3]/text()[1]')[0]
        weather3 = selector.xpath('//*[@id="weather"]/div[1]/div[3]/text()[2]')[0]
        temper3 = selector.xpath('//*[@id="weather"]/div[1]/div[3]/text()[3]')[0]
        clody3 = selector.xpath('//*[@id="weather"]/div[1]/div[3]/text()[4]')[0]
        item3 = time31 + '\n' + time32 + '\n' + weather3 + '\n' + temper3 + '\n' + clody3 + '\n'

        content = [item1, item2, item3]
        return content

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

