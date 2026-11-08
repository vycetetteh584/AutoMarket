from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "make", "model", "year", "price", "mileage"]
    def validate_year(self, value):
            if value < 1900 or value > 2027:
                 raise serializers.ValidationError("Invalid year")
            return value

    def validate_price(self, value):
         if value < 0 or value > 1000000:
              raise serializers.ValidationError("Invalid price")
         return value

    def validate_mileage(self, value):
         if value < 0 or value >  500000:
              raise serializers.ValidationError("Invalid mileage")
         return value