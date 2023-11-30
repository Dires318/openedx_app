"""
    Serializer for rest api.
"""

from rest_framework import serializers
from .models import Greating

class GreatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Greating
        fields = '__all__'

