import requests

def spider():
    cityName = input('请输入你要查找的城市名:')
    cityCode = transCityName(cityName)

    response = requests.get('http://www.weather.com.cn/data/sk/' + cityCode + '.html')
    # 因为请求下来的数据乱码 我们恢复utf-8的编码格式
    response.encoding = 'utf-8'
    # print(response.json())
    msg1 = '城市: %s' % response.json()['weatherinfo']['city'] + '\n'
    msg2 = '风向: %s' % response.json()['weatherinfo']['WD'] + '\n'
    msg3 = '温度: %s' % response.json()['weatherinfo']['temp'] + '\n'
    msg4 = '风力: %s' % response.json()['weatherinfo']['WS'] + '\n'
    msg5 = '湿度: %s' % response.json()['weatherinfo']['SD'] + '\n'
    result = msg1 + msg2 + msg3 + msg4 + msg5
    print("查询结果:\n", result)

def transCityName(cityName):
    cityCode = ''

    if cityName == '北京':
        cityCode = '101010100'
    elif cityName == '广州':
        cityCode = '101280101'
    elif cityName == '汕头':
        cityCode = '101280501'
    elif cityName == '西安':
        cityCode = '101110101'
    elif cityName == '上海':
        cityCode = '101020100'
    elif cityName == '天津':
        cityCode = '101030100'
    elif cityName == '杭州':
        cityCode = '101210101'
    elif cityName == '武汉':
        cityCode = '101200101'
    elif cityName == '南京':
        cityCode = '101190101'
    elif cityName == '深圳':
        cityCode = '101280601'
    elif cityName == '厦门':
        cityCode = '101230201'
    elif cityName == '长沙':
        cityCode = '101250101'
    elif cityName == '合肥':
        cityCode = '101220101'
    elif cityName == '太原':
        cityCode = '101100101'
    elif cityName == '郑州':
        cityCode = '101180101'
    elif cityName == '苏州':
        cityCode = '101190401'
    else:
        cityCode = '101280501'
    return cityCode

if __name__ == '__main__':
    spider()
