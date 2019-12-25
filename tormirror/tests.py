from rest_framework.status import HTTP_200_OK
from rest_framework.test import APISimpleTestCase


class TestMirror(APISimpleTestCase):

    def test_google_search(self):

        response = self.client.post('/request/', data={
            'method': 'get',
            'args': [],
            'kwargs': {
                'url': 'https://google.com/search?q=hello'
            }
        }, format='json')

        self.assertEqual(response.status_code, HTTP_200_OK)
