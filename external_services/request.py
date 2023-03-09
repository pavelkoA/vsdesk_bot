import requests
from bs4 import BeautifulSoup

ssn = requests.Session()
link = 'http://vsdesk/site/login'

data = {
     'LoginForm[username]': 'strike',
     'LoginForm[password]': 'Rfhfv,jkm86',
     'LoginForm[rememberMe]': '0'
}

ssn.post(link, data=data)
cookies = ssn.cookies
headers = ssn.params
print(cookies)
print()
print(headers)
# # next_page = 'http://vsdesk/request/index?ajax=request-grid-full&Request_page=2'
# url = 'http://vsdesk/request/'
# req = ssn.get(url=url, headers=headers, cookies=cookies)
# print(req.text)