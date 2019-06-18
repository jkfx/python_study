import requests
from bs4 import BeautifulSoup
import os

allUniv = []  # 存储全部表格数据，二维列表


def fillUnivList(soup):
    data = soup.find_all('tr')  # 找到所有的tr标签
    print('zzzzz\n\n\n')
    print(data)
    for tr in data:
        ltd = tr.find_all('td')  # 找到每个tr标签中所有td标签
        if len(ltd) == 0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)  # 提前td标签中的信息
        allUniv.append(singleUniv)


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果发送了一个错误请求，则抛出异常
        r.encoding = 'utf-8'
        return r.text
    except:
        print('Error: getHTMLText()')
        return ''


# def printUnivList(num):
#     print('{:^5}{:^21}{:^11}{:^9}{:^15}'.format('排名', '学校名称', '省市', '总分',
#                                                '培养规模'))
#     for i in range(num):
#         u = allUniv[i]
#         print('{:^5}{:^21}{:^11}{:^9}{:^15}'.format(u[0], u[1], u[2], u[3],
#                                                    u[6]))


def main(num):
    ur1 = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(ur1)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    fillUnivList(soup)
    # printUnivList(num)


main(10)
os.system('pause')