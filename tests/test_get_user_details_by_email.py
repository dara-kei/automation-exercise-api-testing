from jsonschema import validate
from schemas.schema_user_details import USER_DETAILS_SCHEMA

ENDPOINT = "/getUserDetailByEmail"

def test_get_user_details_by_email(api_client, create_user):
    response = api_client.get(ENDPOINT, params={'email': create_user['email']})
    response_json = response.json()
    assert response.status_code == 200
    validate(response_json, USER_DETAILS_SCHEMA)