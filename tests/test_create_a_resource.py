import requests
import json
import logging
from jsonschema import validate
from config import BASE_URL

# Configure logging to show some info in the report details section
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Function to open the schema file
def load_schema(schema_file):
  with open(schema_file) as f:
    return json.load(f)

# Test script
def test_create_a_resource():
  payload = {
    "title": "recommendation",
    "body": "motorcycle",
    "userId": 1
  }
  response = requests.post(f"{BASE_URL}/posts", json=payload)
  response_body = response.json()
  
  # Assert response code
  assert response.status_code == 201
  logger.info("status_code is equal to 201 [Pass]")
  
  # Assert response body to match with the payload input
  assert response_body["title"] == payload["title"]
  assert response_body["body"] == payload["body"]
  assert response_body["userId"] == payload["userId"]
  logger.info("response has the same value as the inputted payload [Pass]")

  # Validate schema of response body (data type and required item)
  schema = load_schema("schemas/createResourceSchema.json")
  validate(instance=response_body, schema=schema)
  logger.info("validate schema and data-type [Pass]")
