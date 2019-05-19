from xpinyin import Pinyin
import requests
from lxml import etree

def hanzi2pinyin(city):

    pin = Pinyin()
    temp_pin = pin.get_pinyin(city)
    pin = temp_pin.replace('-', '')
    return pin

def spider(pin):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    url = 'http://www.tianqi2345.com/yubao/{}.htm'
    response = requests.get(url.format(pin), headers=headers)
    selector = etree.HTML(response.text)

    # 当天
    time1 = selector.xpath('//*[@id="weather"]/div[1]/div[1]/strong/text()')[0]
    time2 = selector.xpath('//*[@id="weather"]/div[1]/div[1]/text()[1]')[0]
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

    print(item1)
    print()
    print(item2)
    print()
    print(item3)





if __name__ == '__main__':

    city = input("请输入城市名:")
    pin = hanzi2pinyin(city)
    spider(pin)