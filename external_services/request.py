import requests
from bs4 import BeautifulSoup
from external_services.request_utilit import we_read_user_data_json


def get_session(headers, payload, cookie):
    session = requests.session()
    session.request("POST",
                    "http://vsdesk/site/login",
                    headers=headers,
                    data=payload,
                    cookies=cookie)
    return session


def get_content(link, headers, payload, cookie):
    session = get_session(headers, payload, cookie)
    request = session.request("GET",
                              link, headers, payload, cookie)
    return request


# Функция заходит на страницу vsdesk и собирает номера заявок
def all_request_dict(headers, payload, cookie):
    number_list = {}
    appeal_list_page_5000 = 'http://vsdesk/request?pageCount=5000'
    request = get_content(appeal_list_page_5000,
                          headers, payload, cookie)
    appeal_box = BeautifulSoup(request.content, 'lxml').find('tbody').findAll('tr')
    for odd in appeal_box:
        request_number = odd.findAll('td')[1].text
        request_name = odd.findAll('td')[9].text
        number_list[request_number] = f'{request_number} {request_name}'
    return number_list


#Собираем информацию со страницы заявки
#и формируем из нее сообщение
def request_data(number, headers, payload, cookie):
    appeal_page = 'http://vsdesk/request/' + str(number)
    request = get_content(appeal_page,
                          headers, payload, cookie)
    soup = BeautifulSoup(request.content, 'lxml')
    tstatus = soup.find(class_="view").findAll('div')[0].text
    tinfo = soup.findAll(class_='span4')[1].get_text(separator='\n', strip=True)
    tbody = soup.find(class_='mailbox-read-message').get_text(separator='\n',strip=True)
    return (f'Статус: {tstatus.lstrip('\n')}\n'
            f'{tinfo}\n\n'
            f'{tbody}')


# Функция заходит на страницу vsdesk и собирает номера заявок
def close_request_dict(headers, payload, cookie):
    number_list = {}
    close_request = we_read_user_data_json()["close_request"]
    request = get_content(close_request,
                          headers, payload, cookie)
    appeal_box = BeautifulSoup(request.content, 'lxml').find('tbody').findAll('tr')
    for odd in appeal_box:
        request_number = odd.findAll('td')[1].text
        request_name = odd.findAll('td')[9].text
        number_list[request_number] = request_number + ' ' + request_name
    return number_list
