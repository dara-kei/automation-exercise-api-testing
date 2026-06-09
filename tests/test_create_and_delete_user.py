import pytest

ENDPOINT = "/createAccount"


@pytest.mark.xfail
def test_create_and_delete_user(api_client):
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

    response = api_client.post(ENDPOINT, data=user_data)
    response_json = response.json()
    try:
        assert response.status_code == 201 #!
        assert response_json["responseCode"] == 201
        assert response_json["message"] == "User created!"
    finally:
        response_delete = api_client.delete("/deleteAccount",
                                        data={"email": user_data["email"],
                                              "password": user_data["password"]})

        delete_json = response_delete.json()
        assert response_delete.status_code == 200
        assert delete_json["responseCode"] == 200
        assert delete_json["message"] == "Account deleted!"