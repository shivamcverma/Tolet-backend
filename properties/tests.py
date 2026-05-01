from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from properties.models import Property

User = get_user_model()

class PropertyAPITestCase(APITestCase):
    def setUp(self):
        self.owner_user = User.objects.create_user(
            username='owner', password='password123', role='PROPERTY_OWNER'
        )
        self.student_user = User.objects.create_user(
            username='student', password='password123', role='STUDENT'
        )
        self.property = Property.objects.create(
            owner=self.owner_user,
            title='Test PG',
            description='A nice PG',
            rent=5000,
            city='Delhi',
            area='South Delhi',
            latitude=28.5355,
            longitude=77.2410,
            property_type='PG'
        )
        
        # Another property to test search
        self.property_2 = Property.objects.create(
            owner=self.owner_user,
            title='Test Room',
            description='A nice Room',
            rent=3000,
            city='Mumbai',
            area='Andheri',
            latitude=19.1136,
            longitude=72.8697,
            property_type='ROOM'
        )

    def test_list_properties(self):
        response = self.client.get('/api/properties/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should be paginated (so we check response.data['results'])
        self.assertEqual(len(response.data['results']), 2)

    def test_create_property_as_owner(self):
        self.client.force_authenticate(user=self.owner_user)
        data = {
            'title': 'New Flat',
            'description': 'Description here',
            'rent': 15000,
            'city': 'Delhi',
            'area': 'Vasant Kunj',
            'latitude': 28.53,
            'longitude': 77.16,
            'property_type': 'FLAT'
        }
        response = self.client.post('/api/properties/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Property.objects.count(), 3)

    def test_create_property_as_student(self):
        self.client.force_authenticate(user=self.student_user)
        data = {
            'title': 'My Fake Flat',
            'description': 'Description here',
            'rent': 15000,
            'city': 'Delhi',
            'area': 'Vasant Kunj',
            'latitude': 28.53,
            'longitude': 77.16,
            'property_type': 'FLAT'
        }
        response = self.client.post('/api/properties/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_search_and_filter(self):
        response = self.client.get('/api/properties/?city=Mumbai&property_type=ROOM')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['city'], 'Mumbai')

    def test_distance_filter(self):
        # Coordinates near the Delhi property (28.5355, 77.2410)
        response = self.client.get('/api/properties/?latitude=28.5350&longitude=77.2400&radius=5')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test PG')
        
        # Test far away (e.g., Chennai coordinates)
        response_far = self.client.get('/api/properties/?latitude=13.0827&longitude=80.2707&radius=10')
        self.assertEqual(response_far.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_far.data['results']), 0)
