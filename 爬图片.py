
import requests

def graph_save(response, name):
    with open("./img/{}.jpg".format(name), 'wb') as f:
        f.write(response.content)  # 把图片内容写入

def spider():
    i = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

    url_high_wendu = 'http://pi.weather.com.cn/i/product/share/pic/l/PWCP_TWC_WEAP_S99_ETM_TWC_L88_P9_20190511020000000.JPG'
    url_low_wendu = 'http://pi.weather.com.cn/i/product/share/pic/l/PWCP_TWC_STFC_S99_ETN_TWC_L88_P9_20190511080000000.JPG'
    url_jiangshuiliang = 'http://pi.weather.com.cn/i/product/share/pic/l/PWCP_TWC_WEAP_SFER_EEO_TWC_L88_P9_20190511050000000.JPG'
    url_mean_wendu = 'http://pi.weather.com.cn/i/product/share/pic/l/PWCP_TWC_WEAP_S99_ETT1_TWC_L88_P9_20190510020000000.JPG'

    response1 = requests.get(url_high_wendu, headers=headers)
    name = '1'
    graph_save(response1, name)
    response2 = requests.get(url_low_wendu, headers=headers)
    name = '2'
    graph_save(response2, name)

    response3 = requests.get(url_jiangshuiliang, headers=headers)
    name = '3'
    graph_save(response3, name)

    response4 = requests.get(url_mean_wendu, headers=headers)
    name = '4'
    graph_save(response4, name)

if __name__ == '__main__':
    spider()