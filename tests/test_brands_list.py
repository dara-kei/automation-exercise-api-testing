import pytest
from jsonschema import validate
from schemas.schema_all_brands_list import ALL_BRANDS_LIST_SCHEMA

ENDPOINT = "/brandsList"


def test_get_all_brands_list(api_client):
    response = api_client.get(ENDPOINT)
    assert response.status_code == 200
    validate(response.json(), ALL_BRANDS_LIST_SCHEMA)


@pytest.mark.xfail
def test_put_to_all_brands_list(api_client):
    response = api_client.put(ENDPOINT)
    response_json = response.json()
    assert response_json['responseCode'] == 405
    assert response_json['message'] == 'This request method is not supported.'
    assert response.status_code == 405