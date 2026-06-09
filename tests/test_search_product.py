import pytest
from jsonschema import validate
from schemas.schema_all_products_list import ALL_PRODUCT_LIST_SCHEMA

ENDPOINT = "/searchProduct"


def test_post_to_search_product(api_client):
    response = api_client.post(ENDPOINT, data={"search_product" : "top"})
    assert response.status_code == 200
    validate(response.json(), ALL_PRODUCT_LIST_SCHEMA)


@pytest.mark.xfail
def test_post_to_search_product_without_search_prod_parameter(api_client):
    response = api_client.post(ENDPOINT, data={"search_product" : ""})
    response_json = response.json()
    assert response.status_code == 400
    assert response_json['responseCode'] == 400 # == 200!
    assert response_json['message'] == 'Bad request, search_product parameter is missing in POST request.' # list of all products