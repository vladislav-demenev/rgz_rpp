import unittest
import json
from app import app  

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client() 
        self.app.testing = True

    def test_analyze_text(self):
        test_data = {"text": "hello world hello Flask"}

        response = self.app.post('/analyze', json=test_data)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.data)
        self.assertEqual(response_data['total_words'], 4)
        self.assertEqual(response_data['most_common_words'], [["hello", 2], ["world", 1], ["flask", 1]])

    def test_no_text(self):
        response = self.app.post('/analyze', json={})
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['error'], 'No text provided')

if __name__ == '__main__':
    unittest.main()
