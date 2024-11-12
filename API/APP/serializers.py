from rest_framework import serializers
from .models import Book



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"