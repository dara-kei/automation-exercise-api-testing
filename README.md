Automation Exercise API Testing

API test automation framework for Automation Exercise API built with Python, Pytest and Requests.

Tech Stack:
- Python
- Pytest
- Requests
- Jsonschema
  
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

Several defects were found during API testing:
- Some endpoints return HTTP 200 instead of documented error status codes (400, 404, 405). These cases are marked with @pytest.mark.xfail.
- POST /api/searchProduct with an empty search_product parameter returns the complete products list instead of a validation error, which indicates incorrect search endpoint behavior.
  
Bug Tracking
Defects identified during testing were documented in Jira.

