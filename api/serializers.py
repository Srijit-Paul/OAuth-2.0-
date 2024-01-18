from rest_framework import serializers
from .models import Product, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'locationName']

class ProductSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='location', write_only=True)

    class Meta:
        model = Product
        fields = ['product_id', 'ItemName', 'price', 'location', 'location_id']
        # Explicitly list the fields you want to include

    def create(self, validated_data):
        location = validated_data.pop('location', None)
        product = Product.objects.create(**validated_data)
        return product
