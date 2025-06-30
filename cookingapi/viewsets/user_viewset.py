from rest_framework import viewsets
from cookingapi.models import CookingAPIUser
from cookingapi.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CookingAPIUser.objects.all()
    serializer_class = UserSerializer
