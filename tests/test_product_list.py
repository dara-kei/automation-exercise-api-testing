import pytest
from jsonschema import validate
from schemas.schema_all_products_list import ALL_PRODUCT_LIST_SCHEMA

ENDPOINT = "/productsList"

def test_get_all_products_list(api_client):
    response = api_client.get(ENDPOINT)
    assert response.status_code == 200
    response_json = response.json()
    validate(response_json, ALL_PRODUCT_LIST_SCHEMA)


@pytest.mark.xfail
def test_post_to_all_product_list(api_client):
    response = api_client.post(ENDPOINT)
    response_json = response.json()
    assert response_json['responseCode'] == 405
    assert response_json['message'] == 'This request method is not supported.'
    assert response.status_code == 405 # status code == !
