import requests
import user_agent
from bs4 import BeautifulSoup
import fake_useragent

ssn = requests.Session()

agent = fake_useragent.UserAgent().random
link = 'http://vsdesk/site/login'

data = {
     'YII_CSRF_TOKEN': 'WVU1RE1rNzBjd2pYcXlCWHpQbGt-MEg3aEg4M3RObG85JCTfLrG3umoBQOusI7QSvPcDyjF4Md6Svd1B0yiDoQ%3D%3D',
     'LoginForm[username]': 'strike',
     'LoginForm[password]': 'Rfhfv,jkm86',
     'LoginForm[rememberMe]': '0'
}
ssn.request(method='POST', url=link, data=data)
headers = {
     'Host': 'vsdesk',
     'Cookie': 'YII_CSRF_TOKEN=OVJNSVFSMjZOSmY4ZHNrcVBhaWl5VHZhZ2tmX1N-VWfE7ZG72Bar48KPlydPLVG_9sDRDAAJWTb59e2MUvqSDQ%3D%3D; NAVCOLLAPSE=2; PHPSESSID=h7er4g235p9tadmmcrupc5glj0',
     'Referer': 'http://vsdesk/',
}
next_page = 'http://vsdesk/request/index?ajax=request-grid-full&Request_page=2'
url = 'http://vsdesk/request/'
req = ssn.get(url=url)
print(req.text)
# def request_number_one_page(url): # Функция заходит на страницу vsdesk и собирает номера заявок
#      number_list = []
#      req = ssn.get(url=url, data=data)
#      tbody_soup = BeautifulSoup(req.content, 'lxml')
#      tbody = tbody_soup.findAll('tr')
#      for odd in tbody:
#           body_number = odd.find('td', class_="checkbox-column")
#           if body_number is not None:
#                number_list.append(body_number.find('input').get('value'))
#      return number_list
# request_number = []
# page_list = []
# req_page = ssn.get(url=url, data=data, cookies=ssn.cookies)
# print(req_page)
# li_soup = BeautifulSoup(req_page.content, 'lxml')
# li_page = li_soup.findAll('li', class_= 'page')
# for odd in li_page:
#      next_page = odd.find('a').get('href')
#      page_list.append(url + next_page)
#
# for i in page_list:
#      request_number += request_number_one_page(i)
#
# print(request_number)
# print(page_list)
