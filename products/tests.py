from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

class ProductTests(APITestCase):
    def test_product_detail_endpoint(self):
        # Використовуємо reverse для побудови URL
        url = reverse('product_detail', kwargs={'productId': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 1, "name": "1 name"})