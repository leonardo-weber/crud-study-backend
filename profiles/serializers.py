from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.serializer):
    class Meta:
        model = Profile
        fields = '__all__'