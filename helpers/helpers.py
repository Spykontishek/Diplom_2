import requests
from data import Data

class Helpers:
    def delete_user(self, token):
        self.token = token
        headers={'Authorization': token}
        requests.delete(Data.URL+Data.DEL_PATH, headers = headers)




