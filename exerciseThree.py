import requests
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.request("GET", url)


import unittest
import jsonschema

# Test methods
class Test(unittest.TestCase): 
    def setUp(self):
        self.url = "https://jsonplaceholder.typicode.com/todos/1"
        self.response = requests.get(self.url)
        self.data = self.response.json()
    
# Test sucess response    
    def test_success_response(self):
        self.assertEqual(self.response.status_code, 200)
    
# Test schema response    
    def test_schema_response(self):
        schema = {
            "type": "object",
            "properties": {
                "userId": {"type": "number"},
                "id": {"type": "number"},
                "title": {"type": "string"},
                "completed": {"type": "boolean"}
            },
            "required": ["userId", "id", "title", "completed"]
        }
        try:
# Response data validations
            jsonschema.validate(self.data, schema)
        except jsonschema.exceptions.ValidationError as e:
            self.fail(f"Schema validation failed: {e}")

if __name__ == '__main__':
    unittest.main()