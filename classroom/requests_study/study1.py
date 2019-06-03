import requests
import os


def getHtml(url):
    try:
        w = {'wd': 'java'}
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        r = requests.get(url, headers=headers, params=w)
        print(r.status_code)
        print(r.request.headers)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r.text
        else:
            print('请求失败')
    except:
        print('Error')


def parseHtml(html):
    try:
        pass
    except:
        print('Error')


def saveData(data):
    try:
        with open('study1.html', 'w', encoding='utf-8') as f:
            f.write(data)
    except:
        print('Error')


url = 'https://www.baidu.com/s?'
html = getHtml(url)
#print(html)
data = parseHtml(html)
saveData(html)

os.system('pause')