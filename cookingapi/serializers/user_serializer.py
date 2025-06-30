from rest_framework import serializers
from cookingapi.models import CookingAPIUser

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CookingAPIUser
        fields = ['url', 'username', 'email', 'is_staff']
