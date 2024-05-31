from rest_framework import serializers

from useraccount.serializers import UserDetailsSerializer
from .models import Property, Reservation


class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id','title', 'price_per_night', 'image_url')


class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id','title', 'price_per_night', 'image_url')


class PropertiesDetailSerializer(serializers.ModelSerializer):
    landlord = UserDetailsSerializer(serializers.ModelSerializer)
    class Meta:
        model = Property
        fields = ('id',
              'title',
              'price_per_night',
              'image_url',
              'description',
              'bedrooms',
              'bathrooms',
              'guests',
              'landlord',
              )

class ReservationsListSerializer(serializers.ModelSerializer):
    property = PropertiesListSerializer(serializers.ModelSerializer)
    class Meta:
        model = Reservation
        fields = ('id', 'start_date', 'end_date', 'number_of_nights', 'total_price', 'property')
