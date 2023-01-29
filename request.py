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

headers = {
     'Host': 'vsdesk',
     'Cookie': 'YII_CSRF_TOKEN=OVJNSVFSMjZOSmY4ZHNrcVBhaWl5VHZhZ2tmX1N-VWfE7ZG72Bar48KPlydPLVG_9sDRDAAJWTb59e2MUvqSDQ%3D%3D; NAVCOLLAPSE=2; PHPSESSID=h7er4g235p9tadmmcrupc5glj0',
     'Referer': 'http://vsdesk/',
}
ssn.request(method='POST', url=link, data=data, headers=headers)
print(ssn)

# next_page = 'http://vsdesk/request/index?ajax=request-grid-full&Request_page=2'
# url = 'http://vsdesk/request/'
# req = ssn.get(url=url)
# print(req)