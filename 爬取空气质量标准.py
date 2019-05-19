import requests
from lxml import etree



def spider():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
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
    spider()