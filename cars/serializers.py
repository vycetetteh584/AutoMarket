from rest_framework import serializers
from .models import Car
from datetime import datetime

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "make", "model", "year", "price", "mileage"]
        read_only_fields = ["seller"]
    def validate_year(self, value):
            current_year = datetime.now().year
            if value < 1900 or value > current_year:
                 raise serializers.ValidationError("Invalid year")
            return value

    def validate_price(self, value):
         if value < 0:
              raise serializers.ValidationError("Invalid price")
         return value

    def validate_mileage(self, value):
         if value < 0:
              raise serializers.ValidationError("Invalid mileage")
         return value
    def validate(self, attrs):
         if self.instance:
              old_mileage = self.instance.mileage
              new_mileage = attrs.get("mileage", old_mileage)

              if new_mileage < old_mileage:
                   raise serializers.ValidationError("Mileage cannot be rolled back")
         return attrs