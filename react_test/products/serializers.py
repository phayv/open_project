from rest_framework import serializers
from .models import Product


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
