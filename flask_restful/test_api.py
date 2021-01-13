import unittest

from json import dumps
from requests import get, post

host='http://localhost:3030'

class TestApi(unittest.TestCase):
    def hello_world_get(self):
        url= f'{host}'
        res=get(url).json()
        return res

    def user_get(self):
        url= f'{host}/users/1'
        res=get(url).json()
        return res

    def user_post(self):
        data={}
        pass

    def test_all(self):
        print(self.hello_world_get())
        print(self.user_get())

if __name__ == "__main__":
    unittest.main()
