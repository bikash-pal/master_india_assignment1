from rest_framework import serializers

from .models import Catagories,SubCatagories,Products

class CatagoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagories
        fields = '__all__'