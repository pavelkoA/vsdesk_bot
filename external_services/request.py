import requests
from bs4 import BeautifulSoup


payload = {
'YII_CSRF_TOKEN':'aUcwVTMyblk2N1hlSm5zdjZnaThOVklLWX4xb042VjNGkZt8cW2Cs482yAYPIoQLjFv4K04QEPY1sHPRQp7SKg==',
'LoginForm[username]': 'trener_sth',
'LoginForm[password]': '123',
'LoginForm[rememberMe]': 0
}
headers = {
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

cookie = {
    'NAVCOLLAPSE': '2',
    'PHPSESSID':'bfgr5w8ijndo81ne7u4ngdt863',
    'YII_CSRF_TOKEN':'aUcwVTMyblk2N1hlSm5zdjZnaThOVklLWX4xb042VjNGkZt8cW2Cs482yAYPIoQLjFv4K04QEPY1sHPRQp7SKg%3D%3D'
    }





def all_request_dict():  # Функция заходит на страницу vsdesk и собирает номера заявок
    number_list = {}
    ses = requests.session()
    ses.request("POST", "http://vsdesk/site/login", headers=headers, data=payload, cookies=cookie)
    request = ses.request("GET", 'http://vsdesk/request?pageCount=5000', headers=headers, data=payload, cookies=cookie)
    for odd in BeautifulSoup(request.content, 'lxml').find('tbody').findAll('tr'):
        request_number = odd.findAll('td')[1].text
        request_status = odd.findAll('td')[7].text
        request_date = odd.findAll('td')[8].text
        request_name = odd.findAll('td')[9].text
        request_executor_group = odd.findAll('td')[10].text
        request_customer = odd.findAll('td')[11].text

        number_list[request_number] = request_number + ' ' + request_name
        # number_list[request_number] = {'request_header': request_number + ' ' + request_name,
        #                                 'status': request_status,
        #                                 'request_name': request_name,
        #                                 'request_date': request_date,
        #                                 'request_executor_group': request_executor_group,
        #                                 'request_customer': request_customer
        #                                 }
    return number_list

def request_data(number):
    ses = requests.session()
    ses.request("POST", "http://vsdesk/site/login", headers=headers, data=payload, cookies=cookie)
    request = ses.request("GET", 'http://vsdesk/request/' + str(number), headers=headers, data=payload, cookies=cookie)
    soup = BeautifulSoup(request.content, 'lxml')

    tstatus = soup.find(class_="view").findAll('div')[0].text

    tinfo = soup.findAll(class_='span4')[1].get_text(separator='\n', strip=True)

    tbody = soup.find(class_='mailbox-read-message').get_text(separator='\n',strip=True)
    return 'Статус: ' + tstatus.lstrip('\n') + '\n' + tinfo + '\n\n' + tbody




def close_request_dict():  # Функция заходит на страницу vsdesk и собирает номера заявок
    number_list = {}
    ses = requests.session()
    close_request = 'http://vsdesk/request?Request%5Bid%5D=&Request%5Bslabel%5D%5B%5D=%D0%92%D1%8B%D0%BF%D0%BE%D0%BB%D0%BD%D0%B5%D0%BD%D0%B0&Request%5Bslabel%5D%5B%5D=%D0%97%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B0&Request%5BDate%5D=&Request%5BName%5D=&Request%5Bgroups_id%5D=&Request%5Bfullname%5D=&Request%5Bmfullname%5D=&Request%5Bservice_name%5D=&Request_page=1&ajax=request-grid-full&pageCount=5000'
    ses.request("POST", "http://vsdesk/site/login", headers=headers, data=payload, cookies=cookie)
    request = ses.request("GET", close_request, headers=headers, data=payload, cookies=cookie)
    for odd in BeautifulSoup(request.content, 'lxml').find('tbody').findAll('tr'):
        request_number = odd.findAll('td')[1].text
        request_status = odd.findAll('td')[7].text
        request_date = odd.findAll('td')[8].text
        request_name = odd.findAll('td')[9].text
        request_executor_group = odd.findAll('td')[10].text
        request_customer = odd.findAll('td')[11].text

        number_list[request_number] = request_number + ' ' + request_name
        # number_list[request_number] = {'request_header': request_number + ' ' + request_name,
        #                                 'status': request_status,
        #                                 'request_name': request_name,
        #                                 'request_date': request_date,
        #                                 'request_executor_group': request_executor_group,
        #                                 'request_customer': request_customer
        #                                 }
    return number_list
