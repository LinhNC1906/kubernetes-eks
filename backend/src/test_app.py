import os
import unittest
from dotenv import load_dotenv
import json
import requests
from database.models import setup_db
from flask import Flask
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.app_context().push()
setup_db(app)
app.app_context().push()
CORS(app)
app.app_context().push()

class PaintTestCase(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = "http://localhost:5000/api"
        
    def test_get_paints(self):
        response = requests.get(f"{self.BASE_URL}/paints")
        
        # Check if the request was successful
        self.assertEqual(response.status_code, 200)
        
        # Parse the JSON response
        data = response.json()
        
        # Check if the response contains the expected keys
        self.assertIn('paints', data)
        self.assertIn('success', True)
    
    def test_get_paints_detail(self):
        response = requests.get(f"{self.BASE_URL}/paints-detail")
        
        # Check if the request was successful
        self.assertEqual(response.status_code, 200)
        
        # Parse the JSON response
        data = response.json()
        
        # Check if the response contains the expected keys
        self.assertIn('paints', data)
        self.assertIn('success', True)
        
    def test_create_paint(self):
        # Define the paint data
        data = {
            "id": 1,
            "title": "title 1",
            "recipe": "recipe 1"
        }

        # Send a POST request to the API
        response = requests.post(f"{self.BASE_URL}/paints", json=data)
        
        # Check if the request was successful
        self.assertEqual(response.status_code, 200)
        
        # Verify the response message
        data = response.json()
        self.assertIn('success', True)
        self.assertIn('paints', data)
        
    def test_update_paint(self):
        # Assume a paint with ID 2 exists
        paint_id = 2
        data = {
            "recipe": "recipe 2"
        }
        
        # Send a PATCH request to the API
        response = requests.patch(f"{self.BASE_URL}/paints/{paint_id}", json=data)
        
        # Check if the request was successful
        self.assertEqual(response.status_code, 200)
        
        # Verify the response message
        data = response.json()
        self.assertIn('success', True)
        self.assertIn('paints', data)
        
    def test_delete_paint(self):
        # Assume a question with ID 2 exists
        paint_id = 2
        response = requests.delete(f"{self.BASE_URL}/paints/{paint_id}")
        
        # Check if the request was successful
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', True)
        self.assertIn('delete', 2)
        
        # Verify the question is deleted
        response = requests.get(f"{self.BASE_URL}/{paint_id}")
        self.assertEqual(response.status_code, 404)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()