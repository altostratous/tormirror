import random
import requests
from django.conf import settings
from django.core.cache import cache


def get_new_session():
    session = requests.session()
    credentials = str(random.randint(10000, 0x7fffffff)) + ":" + "ahrefs"
    session.proxies = {
        'http': 'socks5h://{}@localhost:{}'.format(credentials, settings.TOR_PORT),
        'https': 'socks5h://{}@localhost:{}'.format(credentials, settings.TOR_PORT)}
    return session


def get_ok_response(method, *args, retry_count=10, **kwargs):
    cache_key = 'cached_google_ok_session'
    cached_session = cache.get(cache_key)
    if cached_session:
        response = request_from_session(cached_session, method, *args, **kwargs)
        if response.ok:
            return response
    ok = False
    while not ok and retry_count > 0:
        session = get_new_session()
        response = request_from_session(session, method, *args, **kwargs)
        if response.ok:
            cache.set(cache_key, session)
            return response
        retry_count -= 1
    return None


def request_from_session(session, method, *args, **kwargs):
    return getattr(session, method)(*args, **kwargs)
