from rest_framework import serializers
from products.models import Product
from categories.models import Category

class ProductSerializer(serializers.ModelSerializer):
    
    category = serializers.CharField(required=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'selling_price', 'category']  

        extra_kwargs = {
            'product_name': {
                'required': True,
                'error_messages': {
                    'required': 'Product name is required.'
                }
            },
            'description': {
                'required': True,
                'error_messages': {
                    'required': 'Description is required.'
                }
            },
            'selling_price': {
                'required': True,
                'error_messages': {
                    'required': 'Selling price is required.'
                }
            },
            'category': {
                'required': True,
                'error_messages': {
                    'required': 'Category is required.'
                }
            }
        }

    def validate_category(self, value):
    
    
        try:
            category = Category.objects.get(name=value)
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category does not exist.")
        return category
