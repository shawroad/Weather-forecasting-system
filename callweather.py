from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from father import Ui_MainWindow
from child1 import Ui_Form
import requests
from child2 import Ui_Form2
from child3 import Ui_Form3
from child4 import Ui_Form4
from child5 import Ui_Form5
from lxml import etree
from xpinyin import Pinyin

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()


        self.setWindowIcon(QIcon('./img/sign.ico'))
        self.setupUi(self)
        self.setWindowTitle('天气预报的查询')

        self.child1 = ChildrenForm1()

        self.child2 = ChildrenForm2()

        self.child3 = ChildrenForm3()

        self.child4 = ChildrenForm4()

        self.child5 = ChildrenForm5()

        self.father = Ui_MainWindow()

        self.searchWeather.triggered.connect(self.openFindWeather)
        self.WorldWeather.triggered.connect(self.searchWordgraph)
        self.sanWeather.triggered.connect(self.find_san_weather)
        self.kongqisort.triggered.connect(self.kongqizhiliang)
        self.kongqibiaozhun.triggered.connect(self.kqzl)



    def openFindWeather(self):

        self.child2.close()
        self.child3.close()
        self.child4.close()
        self.child5.close()
        self.gridLayout.addWidget(self.child1)
        self.child1.show()

    def searchWordgraph(self):

        self.child1.close()
        self.child3.close()
        self.child4.close()
        self.child5.close()
        self.gridLayout.addWidget(self.child2)
        self.child2.show()
    def find_san_weather(self):
        self.child1.close()
        self.child2.close()
        self.child4.close()
        self.child5.close()
        self.gridLayout.addWidget(self.child3)
        self.child3.show()
    def kongqizhiliang(self):
        self.child1.close()
        self.child2.close()
        self.child3.close()
        self.child5.close()
        self.gridLayout.addWidget(self.child4)
        self.child4.show()

    def kqzl(self):
        self.child1.close()
        self.child2.close()
        self.child3.close()
        self.child4.close()
        self.gridLayout.addWidget(self.child5)
        self.child5.show()
        
class ChildrenForm1(QWidget, Ui_Form):
    def __init__(self):
        super(ChildrenForm1, self).__init__()
        self.setupUi(self)
        self.clearBtn.clicked.connect(self.clearResult)
        self.queryBtn.clicked.connect(self.queryWeather)

    def queryWeather(self):
        print("天气查询。。。")
        # 获取当前选择的文本内容
        cityName = self.weatherComboBox_2.currentText()
        # 将文本内容转换为拼音
        pinyin = self.hanzi2pinyin(cityName)

        content = self.spider(pinyin)

        self.resultText_2.setText(content)

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

        msg1 = "城市: " + self.weatherComboBox_2.currentText()
        # # //*[@id="weather"]/div[1]/div[1]/text()[1]
        # msg2_1 = "日期: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0] + '\n'
        # msg2.replace('(', '')
        # # //*[@id="weather"]/div[1]/div[1]/text()[3]
        # msg3 = "天气: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[3]')[0] + '\n'
        # # //*[@id="weather"]/div[1]/div[1]/text()[4]
        # msg4 = "温度: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[4]')[0] + '\n'

        # time1 = selector.xpath('//*[@id="weather"]/div[1]/div[1]/strong/text()')[0]

        # time11 = selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0]
        # time22 = selector.xpath('//*[@id="weather"]/div[1]/div[1]/span/text()[1]')[0]
        # time2 = time11 + time22 + ')'
        # weather = selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[3]')[0]
        # temper = selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[4]')[0]
        # item1 = time1 + '\n' + msg1  + '\n' + time2 + '\n' + weather + '\n' + temper + '\n'


        time = "日期: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0]
        time = time.replace('(', " ")

        weather ="天气:" + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[3]')[0]
        temper = "温度:" + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[4]')[0]


        item1 = msg1 + '\n' + time  + '\n' + weather + '\n' + temper

        # content = msg1 + msg2 + msg3 + msg4

        return item1

    def clearResult(self):
        print('清除文本框。。。')
        self.resultText_2.clear()


class ChildrenForm2(QWidget, Ui_Form2):
    def __init__(self, parent=None):
        super(ChildrenForm2, self).__init__()
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
        url_mean_wendu = 'http://pi.weather.com.cn/i/product/share/pic/l/PWCP_TWC_WEAP_S99_ETT1_TWC_L88_P9_20190319020000000.JPG'

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


class ChildrenForm3(QWidget, Ui_Form3):
    def __init__(self, parent=None):
        super(ChildrenForm3, self).__init__()
        self.setupUi(self)
        self.findBtn.clicked.connect(self.findinfo)
        self.clearBtn.clicked.connect(self.clearinfo)

    def findinfo(self):

        text = self.lineEdit.text()
        print(text)
        pin = self.hanzi2pinyin(text)
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
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        url = 'http://www.tianqi2345.com/yubao/{}.htm'
        response = requests.get(url.format(pin), headers=headers)
        selector = etree.HTML(response.text)

        # 当天
        #//*[@id="weather"]/div[1]/div[1]/text()[1]
        # //*[@id="weather"]/div[1]/div[1]/strong
        # time1 = selector.xpath('//*[@id="weather"]/div[1]/div[1]/strong/text()')[0]

        # time11 = selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0]
        # time22 = selector.xpath('//*[@id="weather"]/div[1]/div[1]/span/text()[1]')[0]
        # time2 = time11 + time22 + ')'
        # weather = selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[3]')[0]
        # temper = selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[4]')[0]
        # item1 = time1 + '\n' + time2 + '\n' + weather + '\n' + temper + '\n'
        # time = "日期: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0]
        # weather ="天气:" + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[2]')[0]
        
        # temper = "温度:" + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[3]')[0]

        # item1 = time  + '\n' + weather + '\n' + temper
        time = "日期: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0]
        time = time.replace('(', " ")

        weather ="天气:" + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[3]')[0]
        temper = "温度:" + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[4]')[0]


        item1 ='今天' + '\n' + time  + '\n' + weather + '\n' + temper


        # 明天
        time21 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/strong/text()')[0]
        time2_1 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[1]')[0]
        time2_2 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/span/text()[1]')[0]
        time22 = time2_1 + time2_2 + ')'

        weather2 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[3]')[0]
        temper2 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[4]')[0]
        clody2 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[5]')[0]
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

class ChildrenForm4(QWidget, Ui_Form4):
    def __init__(self, parent=None):
        super(ChildrenForm4, self).__init__()
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

class ChildrenForm5(QWidget, Ui_Form5):
    def __init__(self, parent=None):
        super(ChildrenForm5, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.showinfo)
        self.pushButton_2.clicked.connect(self.clearinfo)



    def showinfo(self):
        info = self.spider()
        str = ''
        for i, item in enumerate(info):
            if i == 1 or i == 2 or i == 0:
                str += item[0] + '\t' + item[1] + ' ' + ' ' + ' ' + '\t' + item[2] + '\n'
            else:
                str += item[0] + '\t' + item[1] + '\t' + item[2] + '\n'
        self.textEdit.setText(str)

    def clearinfo(self):

        self.textEdit.clear()

    def spider(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        url = 'https://www.tianqi.com/air/'
        response = requests.get(url, headers=headers)
        selector = etree.HTML(response.text)
        all_tr = selector.xpath('//*[@id="aqs-unit-fixed"]/div[2]/table/tbody/tr')
        title1 = all_tr[0].xpath('th[1]/text()')[0]
        title2 = all_tr[0].xpath('th[2]/text()')[0]
        title3 = all_tr[0].xpath('th[3]/text()')[0]
        item = [title1, title2, title3]
        info = []
        info.append(item)
        all_tr.remove(all_tr[0])

        for tr in all_tr:
            t1 = tr.xpath('td[1]/text()')[0]

            t2_1 = tr.xpath('td[2]/text()')[0]
            t2_2 = tr.xpath('td[2]/em/text()')[0]
            t2 = t2_1 + '=>' + t2_2

            t3 = tr.xpath('td[3]/text()')[0]

            item = [t1, t2, t3]
            info.append(item)
        return info

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.setObjectName("MainWindow")  # 为主窗口设置对象名 为了在下面设置背景颜色
    win.setStyleSheet("#MainWindow{border-image:url(./img/weather.jpg);}")
    win.show()
    sys.exit(app.exec_())