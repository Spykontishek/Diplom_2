import requests
from constants import Constants

class Helpers:
    accessToken = None

    def delete_user(self, accessToken):
        self.accessToken = accessToken
        headers={'Authorization': accessToken}
        requests.delete(Constants.URL+Constants.DEL_PATH, headers = headers)




