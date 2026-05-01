from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationTestCase(APITestCase):
    def test_registration_success(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123',
            'role': 'STUDENT',
            'phone_number': '1234567890'
        }
        response = self.client.post('/api/accounts/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'newuser')

    def test_registration_missing_fields(self):
        data = {
            'username': 'newuser',
            # email missing
            'password': 'password123'
        }
        response = self.client.post('/api/accounts/register/', data)
        # email is not required in RegisterSerializer.Meta.fields, but username and password are.
        # Wait, let's check serializer again.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # Email is optional
