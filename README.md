Automation Exercise API Testing

API test automation framework for Automation Exercise API built with Python, Pytest and Requests.

Tech Stack:
- Python
- Pytest
- Requests
- Jsonschema
- 
Project Structure
.
├── tests/
├── schemas/
├── utils/
│   └── api_client.py
├── conftest.py
├── requirements.txt
└── README.md

Features:
- Reusable API client
- Pytest fixtures
- JSON Schema validation
- Positive and negative test scenarios
- User creation and cleanup
- Validation of 14 API endpoints
- Detection of API inconsistencies and defects
  
Installation:
- pip install -r requirements.txt
  
Run Tests:
- pytest
- pytest -v

Defects Found

Several inconsistencies between API documentation and actual behavior were discovered.

1. Incorrect HTTP Status Codes

Documentation expects:
- 405 Method Not Allowed
- 400 Bad Request
- 404 Not Found

Actual response: HTTP/1.1 200 OK
while the real error code is returned inside JSON:
{
  "responseCode":405,
  "message":"This request method is not supported."
}

Affected endpoints:
- POST /productsList
- PUT /brandsList
- DELETE /verifyLogin
- Verify login with invalid credentials
- Verify login without required parameters

Tests are marked as @pytest.mark.xfail because the implementation does not match the API specification.

2. Search Product without parameter

Expected:
{
    "responseCode":400,
    "message":"Bad request, search_product parameter is missing in POST request."
}

Actual: API returns the complete product list.

3. User creation response

Documentation specifies:
HTTP Status Code: 201

Actual: HTTP response status is always: 200

while:
{
    "responseCode":201,
    "message":"User created!"
}
is returned inside response body.


