from xpinyin import Pinyin
import requests
from lxml import etree
import sqlite3
import time



def hanzi2pinyin(city):

    # 汉字2拼音
    pin = Pinyin()
    temp_pin = pin.get_pinyin(city)
    pin = temp_pin.replace('-', '')
    return pin


def spider(pin, timedb, ct):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    url = 'http://www.tianqi2345.com/yubao/{}.htm'
    response = requests.get(url.format(pin), headers=headers)
    selector = etree.HTML(response.text)

    # 链接数据库   也就是指定数据库的名字  后面是一个目录
    conn = sqlite3.connect(r'.\{}.db'.format(timedb))

    c = conn.cursor()

    # 创建今天天气的表
    c.execute('''CREATE TABLE IF NOT EXISTS one_air (日期 text,城市 text, 天气 text, 温度 text)''')
    # 创建明天天气的表
    c.execute('''CREATE TABLE IF NOT EXISTS next_air (日期 text,城市 text, 天气 text, 温度 text, 风度 text)''')
    # 创建后天天气的表
    c.execute('''CREATE TABLE IF NOT EXISTS next_next_air (日期 text,城市 text, 天气 text, 温度 text, 风度 text)''')

    conn.commit()


    time = "日期: " + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0]
    time = time.replace('(', " ")

    weather ="天气:" + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[3]')[0]
    temper = "温度:" + selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[4]')[0]  


    c.execute("INSERT INTO one_air VALUES (?,?,?,?)", (time, ct, weather, temper))

    # 明天
    # time21 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/strong/text()')[0]
    time1 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[1]')[0]
    time1 = time1.replace('(', '')
    time22 = "明天:" + time1
    # time22 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[1]')[0]
    weather2 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[3]')[0]
    temper2 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[4]')[0]
    clody2 = selector.xpath('//*[@id="weather"]/div[1]/div[2]/text()[5]')[0]
    c.execute("INSERT INTO next_air VALUES (?,?,?,?,?)", (time22, ct, weather2, temper2, clody2))

    # 后天

    time32 ='后天：' + selector.xpath('//*[@id="weather"]/div[1]/div[3]/text()[1]')[0]
    weather3 = selector.xpath('//*[@id="weather"]/div[1]/div[3]/text()[2]')[0]
    temper3 = selector.xpath('//*[@id="weather"]/div[1]/div[3]/text()[3]')[0]
    clody3 = selector.xpath('//*[@id="weather"]/div[1]/div[3]/text()[4]')[0]
    c.execute("INSERT INTO next_next_air VALUES (?,?,?,?,?)", (time32, ct, weather3, temper3, clody3))
    conn.commit()  # 提交事务
    conn.close()



if __name__ == '__main__':

    # 建立一个城市列表，我们提前我这些城市的天气爬下来，存到数据库中
    city = ['北京', '西安', '上海', '汕头', '天津', '深圳', '洛阳']

    # 创建数据库。  每天爬一次，创建一个数据库，然后将数据存入
    timedb = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    for ct in city:
        pin = hanzi2pinyin(ct)
        spider(pin, timedb, ct)

