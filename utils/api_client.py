import requests

class ApiClient:
    BASE_URL = "https://automationexercise.com/api"

    def get(self, endpoint, params=None, headers=None):
        return requests.get(self.BASE_URL + endpoint, params=params, headers=headers)

    def post(self, endpoint, params=None, data=None, json=None, headers=None):
        return requests.post(self.BASE_URL + endpoint, params=params, data=data, json=json, headers=headers)

    def put(self, endpoint, params=None, data=None, json=None, headers=None):
        return requests.put(self.BASE_URL + endpoint, params=params, data=data, json=json, headers=headers)

    def delete(self, endpoint, params=None, data=None, json=None, headers=None):
        return requests.delete(self.BASE_URL + endpoint, params=params, data=data, json=json, headers=headers)


