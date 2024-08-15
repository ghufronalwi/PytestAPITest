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
def test_get_resources():
  response = requests.get(f"{BASE_URL}/posts")
  response_body = response.json()
    
  # Assert response code
  assert response.status_code == 200
  logger.info("status_code is equal to 200 [Pass]")
    
  # Assert response body to have 100 data
  assert len(response_body) == 100
  logger.info("length of the response body = 100 [Pass]")
    
  # Validate schema of response body (data type and required item)
  schema = load_schema("schemas/getResourcesSchema.json")
  validate(instance=response_body, schema=schema)
  logger.info("validate schema and data-type [Pass]")
