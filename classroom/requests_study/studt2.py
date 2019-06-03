import os
import requests


def getHtml(url):
    try:
        w = {'q': 'java'}
        r = requests.get(url, params=w)
        print(r.status_code)
        print(r.request.headers)
        if r.status_code == 200:
            return r.text
        else:
            print('Fail')
    except:
        print('Error: getHtml()')


def parseHtml(html):
    try:
        pass
    except:
        print('Error: parseHtml()')


def savaData(data):
    try:
        with open('study2.html', 'w', encoding='utf-8') as f:
            f.write(data)
    except:
        print('Error: savaData()')


url = 'https://www.so.com/s?'
html = getHtml(url)
savaData(html)
