import requests
import time

import config


def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
    """ Выполнить GET-запрос
    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    delay = 0.1
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, params, str(timeout))
            response.raise_for_status()
            if response.status_code == 200:
                return response
        except requests.exceptions.RequestException:
            time.sleep(delay)
            delay = delay * backoff_factor + random.uniform(0, 0.1)
            retries += 1
    return False


def get_friends(user_id, fields):
    """ Вернуть данных о друзьях пользователя
    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    domain = "https://api.vk.com/method"
    access_token = '4aa71efaa650dd89e199d377912d463d6289c41c509a286a783328fb449c474a3fc696731a2d7f965c85e'
    user_id = user_id
    fields = fields
    v = '5.103'
    query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
    response = requests.get(query)
    r = response.json()
    return r['response']['items']
    
