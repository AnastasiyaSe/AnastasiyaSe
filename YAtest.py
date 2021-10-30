token = ''
import requests
import unittest

class YaMaker:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def make_link(self, disk_file_path):
        make_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.put(make_url, headers=headers, params=params)
       
        return response


maker = YaMaker(token=token)





class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")
    def tearDown(self):
        print("method tearDown")
    def test_maker(self):
        self.assertEqual(str(maker.make_link('name')), '<Response [201]>')


if __name__ == '__main__':
    unittest.main()