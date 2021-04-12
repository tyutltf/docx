import unittest
from json import dumps

from requests import get, post, put, delete

host = 'http://localhost:3030'


class TestApi(unittest.TestCase):
    def hello_get(self):
        url = f'{host}'
        res = get(url).json()
        return res

    def hello_post(self):
        url = f'{host}'
        res = post(url).json()
        return res

    def user_get(self):
        url = f'{host}/users/1'
        data = {
            'userid': 1
        }
        res = get(url, data=data).json()
        return res

    def user_post(self):
        url = f'{host}/users/3'
        data = {
            "userid": 3,
            "username": "jack",
            "age": 17,
            "sex": "male",
        }
        res = post(url, data=data).json()
        return res

    def test_all(self):
        # print(self.hello_get())
        # print(self.hello_post())
        # print(self.user_get())
        print(self.user_post())


if __name__ == "__main__":
    unittest.main()
