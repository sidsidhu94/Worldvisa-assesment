from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product
from categories.models import Category

class CreateProductViewTest(APITestCase):
    
    def setUp(self):
        
        self.category = Category.objects.create(name="Jewelry", is_active=True)
        self.url = reverse('product-create')  

    def test_create(self):
        data = {
            "product_name": "Handmade Jewelry",
            "description": "A beautiful handmade jewelry piece.",
            "selling_price": "100.00",
            "category": self.category.name
        }
        
        response = self.client.post(self.url, data, format='json')
        

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        product = Product.objects.get()
        self.assertEqual(product.product_name, "Handmade Jewelry")
        self.assertEqual(product.description, "A beautiful handmade jewelry piece.")
        self.assertEqual(product.selling_price, 100.00)
        self.assertEqual(product.category, self.category)

    def test_missing_fields(self):
        data = {
            "product_name": "",
            "description": "A beautiful handmade jewelry piece.",
            "selling_price": "100.00",
            "category": self.category.name
        }
        
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('product_name', response.data)
        self.assertEqual(Product.objects.count(), 0)
    
    def test_invalid_category(self):
        data = {
            "product_name": "Handmade Jewelry",
            "description": "A beautiful handmade jewelry piece.",
            "selling_price": "100.00",
            "category": "NonExistentCategory"
        }
        
        response = self.client.post(self.url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('category', response.data)
        self.assertEqual(Product.objects.count(), 0)

    def test_invalid_price(self):
        data = {
            "product_name": "Handmade Jewelry",
            "description": "A beautiful handmade jewelry piece.",
            "selling_price": "invalid_price",
            "category": self.category.name
        }
        
        response = self.client.post(self.url, data, format='json')
        

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('selling_price', response.data)
        self.assertEqual(Product.objects.count(), 0)
