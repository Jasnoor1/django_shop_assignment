from rest_framework import serializers
from .models import Category,SubCategory,Product

class ProductFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'