import requests
import user_agent
from bs4 import BeautifulSoup
import fake_useragent

ssn = requests.Session()

link = 'http://vsdesk/site/login'

data = {
     'YII_CSRF_TOKEN': 'aUcwVTMyblk2N1hlSm5zdjZnaThOVklLWX4xb042VjNGkZt8cW2Cs482yAYPIoQLjFv4K04QEPY1sHPRQp7SKg==',
     'username': 'strike',
     'password': 'Rfhfv,jkm86',
     'rememberMe': '0'
}
ssn.post(url=link, data=data)

# new_req = str(ssn.cookies.set_policy).split()
# id = []
# for i in new_req:
#      if i[:6] == "value=":
#           id.append(i[7:-2])

headers = {
     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
     'Accept - Encoding': 'gzip, deflate',
     'Accept - Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
     'Cache - Control': 'max - age = 0',
     'Connection': 'keep - alive',
     'Content - Length': '204',
     'Content - Type': 'application / x - www - form - urlencoded',
     'Cookie': 'ajRTTEg0YkVvVUxXQW0wZkVDV1NkbnRJdXdNM25ZTFkJBJ-CxQzgC_9-hHpbYJzixIe9jHZ-o8UBmGI1w5OCHg%3D%3D; NAVCOLLAPSE=2; PHPSESSID=qgfc3pj5iu3g0o27oa8sri0ut4',
     'Host': 'vsdesk',
     'Origin': 'http://vsdesk',
     'Referer': 'http://vsdesk/site/login',
     'Upgrade-Insecure-Requests': '1',
     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
}

next_page = 'http://vsdesk/request/index?ajax=request-grid-full&Request_page=2'
url = 'http://vsdesk/request/'

def request_number_one_page(url): # Функция заходит на страницу vsdesk и собирает номера заявок
     number_list = []
     req = ssn.get(url=url, headers=headers, cookies=ssn.cookies)
     tbody_soup = BeautifulSoup(req.content, 'lxml')
     tbody = tbody_soup.findAll('tr')
     for odd in tbody:
          body_number = odd.find('td', class_="checkbox-column")
          if body_number is not None:
               number_list.append(body_number.find('input').get('value'))
     return number_list
request_number = []
page_list = []
req_page = ssn.get(url=url, data=data, headers=headers)

li_soup = BeautifulSoup(req_page.content, 'lxml')
li_page = li_soup.findAll('li', class_= 'page')
for odd in li_page:
     next_page = odd.find('a').get('href')
     page_list.append(url + next_page)

for i in page_list:
     request_number += request_number_one_page(i)

print(request_number)
print(page_list)
