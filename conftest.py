import pytest

from utils.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client():
    return ApiClient()

@pytest.fixture()
def create_user(api_client):
    user_data = {"name" : "test",
                 "email" : "big_email999@gmail.com",
                 "password" : "test",
                 "title" : "Mr",
                 "birth_date" : "1",
                 "birth_month" : "3",
                 "birth_year" : "2000",
                 "firstname" : "test",
                 "lastname" : "test",
                 "company" : "test",
                 "address1" : "test",
                 "address2" : "test",
                 "country" : "test",
                 "zipcode" : "test",
                 "state" : "test",
                 "city" : "test",
                 "mobile_number" : "test"}

    response = api_client.post("/createAccount", data=user_data)
    response_json = response.json()
    assert response_json["responseCode"] == 201
    yield {"name" : user_data["name"],
           "email" : user_data["email"],
           "password" : user_data["password"]}

    response_delete = api_client.delete("/deleteAccount", data={"email" : user_data["email"], "password" : user_data["password"]})
    delete_json = response_delete.json()
    assert delete_json["responseCode"] == 200

