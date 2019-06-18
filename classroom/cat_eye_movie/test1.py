import os
import csv
import requests
from bs4 import BeautifulSoup

name = []
star = []
time = []
allst = []


def parseStar():
    try:
        global star
        for i in range(len(star)):
            star[i] = star[i][3:]
    except:
        print('Error: parseStar()')


def parseTime():
    try:
        global time
        for i in range(len(time)):
            time[i] = time[i][5:]
    except:
        print('Error: parseTime()')


def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('Error: getHtml()')


def parseBs4(soup, value):
    try:
        name = []
        alst = soup.find_all('p', {'class': value})
        for p in alst:
            name.append(p.string)
        return name
    except:
        print('Error: parseBs4()')


def parseHtml(html):
    try:
        global name
        global star
        global time
        global allst
        soup = BeautifulSoup(html, features="lxml")
        name = parseBs4(soup, 'name')
        star = parseBs4(soup, 'star')
        time = parseBs4(soup, 'releasetime')
        name = parseData(name)
        star = parseData(star)
        time = parseData(time)
        parseStar()
        parseTime()
        for i in range(10):
            allst.append([name[i], star[i], time[i]])
    except:
        print('Error: parseHtml()')


def parseData(data):
    try:
        name = []
        for st in data:
            st = st.replace('\n', '').replace(' ', '')
            name.append(st)
        return name
    except:
        print('Error: parseData()')


def savaData(data):
    try:
        with open('test1.html', 'w', encoding='utf-8') as f:
            f.write(data)
    except:
        print('Error: savaData()')


def savaCsv(allst):
    try:
        header = ['电影名', '主演', '上映时间']
        with open('test1.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for i in range(10):
                writer.writerow(allst[i])
    except:
        print('Error: savaVsc()')


url = 'https://maoyan.com/board/4'
html = getHtml(url)
parseHtml(html)
savaCsv(allst)