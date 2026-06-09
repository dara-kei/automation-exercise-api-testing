import pytest

ENDPOINT = "/verifyLogin"

def test_post_to_verify_login_with_valid_details(api_client, create_user):
    response = api_client.post(ENDPOINT, data={"email" : create_user["email"],
                                               "password" : create_user["password"]})
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['responseCode'] == 200
    assert response_json['message'] == 'User exists!'


@pytest.mark.xfail
def test_post_to_verify_login_without_email_parameter(api_client, create_user):
    response = api_client.post(ENDPOINT, data={"password" : create_user["password"]})
    assert response.status_code == 400 #!
    response_json = response.json()
    assert response_json['responseCode'] == 400
    assert response_json['message'] == 'Bad request, email or password parameter is missing in POST request.'


@pytest.mark.xfail
def test_post_to_verify_login_without_password_parameter(api_client, create_user):
    response = api_client.post(ENDPOINT, data={"email" : create_user["email"]})
    assert response.status_code == 400 #!
    response_json = response.json()
    assert response_json['responseCode'] == 400
    assert response_json['message'] == 'Bad request, email or password parameter is missing in POST request.'


@pytest.mark.xfail
def test_delete_to_verify_login(api_client, create_user):
    response = api_client.delete(ENDPOINT)
    assert response.status_code == 405 #!
    response_json = response.json()
    assert response_json['responseCode'] == 405
    assert response_json['message'] == 'This request method is not supported.'


@pytest.mark.xfail
def test_post_to_verify_login_with_invalid_details(api_client, create_user):
    response = api_client.post(ENDPOINT, data={"email" : "dfgd@df.com", "password" : "dgd"})
    assert response.status_code == 404 #!
    response_json = response.json()
    assert response_json['responseCode'] == 404
    assert response_json['message'] == 'User not found!'