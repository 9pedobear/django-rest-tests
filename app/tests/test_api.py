from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.models import Car
from app.serializers import CarSerializer
from pprint import pprint


class CarTests(APITestCase):
    # Test GET all cars
    def test_get_all_cars(self):
        car1 = Car.objects.create(name='Car 1', price=1000)
        car2 = Car.objects.create(name='Car 2', price=2000)
        car3 = Car.objects.create(name='Car 3', price=3000)
        url = reverse('car-list')
        response = self.client.get(url)
        serializer_data = CarSerializer([car1, car2, car3], many=True).data
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




