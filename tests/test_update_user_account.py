ENDPOINT = "/updateAccount"

def test_put_to_update_user_account(api_client, create_user):
    user_data = {"name": "testname",
                 "email": "big_email999@gmail.com",
                 "password": "test",
                 "title": "Mr",
                 "birth_date": "1",
                 "birth_month": "3",
                 "birth_year": "2000",
                 "firstname": "test",
                 "lastname": "testsurname",
                 "company": "test",
                 "address1": "test",
                 "address2": "test",
                 "country": "test",
                 "zipcode": "test",
                 "state": "test",
                 "city": "test",
                 "mobile_number": "test"}
    response = api_client.put(ENDPOINT, data=user_data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['responseCode'] == 200
    assert response_json['message'] == 'User updated!'
