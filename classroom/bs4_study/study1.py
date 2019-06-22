from bs4 import BeautifulSoup
import requests
import os

r = requests.get('http://www.baidu.com')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, features="lxml")
print(type(soup))
print('class soup')
print(soup)
print('head')
print(soup.head)
print('title')
print(soup.title)
print('body')
print(soup.body)
print('p')
print(soup.p)
print('strings')
print(soup.strings)
print('stripped_strings')
print(soup.stripped_strings)

print('a')
print(soup.a)
print('a.name')
print(soup.a.name)
print('a.attrs')
print(soup.a.attrs)
print('a.string')
print(soup.a.string)

os.system('pause')
