from rest_framework import serializers
from models import Venue, Category, Food


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ('id', 'name', 'gurunavi_id', 'gurunavi_url', 'address',
                  'latitude', 'longitude', 'images', 'description', 'budget', 'categories')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'name_jp', 'description', 'image', 'venue')