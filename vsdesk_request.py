import requests
url = 'http://vsdesk/requests/'
session = requests.Session()
session.post('http://vsdesk/requests/', {
     'username': 'strike',
     'password': 'Rfhfv,jkm86',
     'rememberMe': 0,
})
headars = {
     'username': 'strike',
     'password': 'Rfhfv,jkm86',
}

req = requests.request(method='GET', url=url, headers=headars)
print(req.text)
