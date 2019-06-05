import requests
import os


def getHtml(url):
    try:
        headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        cookie = {
            'cookie':
            '_zap=37afb37a-e7b7-43dd-abaa-10cc35092a93; _xsrf=9ZFCosJZl8N3ZlodDTrkI5ASA8WV0fD0; d_c0="AKDqeo5ViQ-PTllgxPxXAdBEKGniPo5oCmc=|1559694380"; capsion_ticket="2|1:0|10:1559694399|14:capsion_ticket|44:NmEwNDVkNTRmODgzNGUzOWJjMzgyMTMzYzE4YmU0YjI=|7095f47c1810a74200307061518b6865f263294835b12527da18f122de1c044a"; z_c0="2|1:0|10:1559694407|4:z_c0|92:Mi4xMEpEUUJnQUFBQUFBb09wNmpsV0pEeVlBQUFCZ0FsVk5SbHJrWFFBMFNNeG16cEMwMTRwZGc5RDkwTHNxbTJLcHNR|bea4c88de127533963494ccf1ef45967d3ea6f3f93f1c15493ff9f454d89a134"; tst=r; tgw_l7_route=116a747939468d99065d12a386ab1c5f'
        }
        zh = requests.get(
            url,
            headers=headers
        )
        zh.encoding = 'utf-8'
        if zh.status_code == 200:
            return zh.text
        else:
            print('Error: status_code')
    except:
        print('Error: getHtml()')
        return ''


def parseHtml(html):
    pass


def saveData(data):
    try:
        with open('study3.html', 'w', encoding='utf-8') as f:
            f.write(data)
    except:
        print('Error: savaData()')


url = 'https://www.zhihu.com/'
html = getHtml(url)
saveData(html)
