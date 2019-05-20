import os

from requests_html import HTMLSession
session = HTMLSession()

links = ['https://movie.douban.com/subject/1292052/',
		'https://movie.douban.com/subject/1962665/',
		'https://movie.douban.com/subject/26752088/']

links2 = ['http://stock.finance.sina.com.cn/usstock/quotes/aapl.html',
			'http://stock.finance.sina.com.cn/usstock/quotes/bidu.html',
			'http://stock.finance.sina.com.cn/usstock/quotes/msft.html']




for link in links:
    r = session.get(link)
    title = r.html.find('#content > h1 > span:nth-child(1)', first=True)
    year = r.html.find('#content > h1 > span.year', first=True)
    print(title.text, year.text)

for link in links2:
    r = session.get(link)
    r.html.render()
    title = r.html.find('#hqPrice', first=True)
    print(title.text, year.text)
os.system('pause')
