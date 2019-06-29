import requests
import bs4
import csv

url = 'http://sports.sina.com.cn/nba/finals.shtml'

r = requests.get(url)
r.encoding = 'utf-8'
soup = bs4.BeautifulSoup(r.text, features="html.parser")

all_tr = soup.find_all('tr')
all_td = soup.find_all('td', height="20")
for tr in all_tr:
    for td in tr:
        if isinstance(td, bs4.element.Tag):
            lis.append(td.string)
while None in lis:
    lis.remove(None)

one = []
for i in range(0, len(lis), 8):
    one.append([ lis[i], lis[i + 1], lis[i + 2], lis[i + 3], lis[i + 4],
               lis[i + 5], lis[i + 6], lis[i + 7] ])
head = ['年份', '日期', '冠军', '冠军教练', '亚军', '亚军教练', '比分', 'MVP']
with open('nba.csv', 'w', newline='', encoding='utf-8-sig') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    f_csv.writerows(one)
